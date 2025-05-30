import json
import csv
import os

import pandas
import re
from datetime import datetime, timedelta

import pandas as pd

# 定义CSV文件路径
csv_file_path = '商品价格.csv'
# 定义一部字典，用于存储商品名，而商品名又是另一部字典，用于存储日期和价格
allGoodsDict = {}

start_date = datetime(2024, 2, 29)
end_date = datetime(2025, 4, 16)
date_range = pd.date_range(start=start_date, end=end_date)
all_df = pd.DataFrame(date_range.strftime('%Y-%m-%d'), columns=['Date'])


while True:
    # 假设你的JSON格式字符串如下
    input_str = input("请输入json格式")
    if input_str == 'exit':
        break
    input_goodName = input("请输入商品名")

    # 将JSON字符串解析为Python对象
    matches = re.findall(r'\d+,\d+', input_str)

    result_dict = {}



    for match in matches:
        # 使用split()函数切割字符串
        key, value = match.split(',')
        timestamp = int(key) / 1000
        # 将键和值存储为字典的键和值
        date = pandas.to_datetime(timestamp, unit='s').strftime('%Y-%m-%d')
        print(date)
        print(value)
        result_dict[date] = value
    # 定义起始日期和结束日期
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 4, 16)

    # 创建一个空字典
    date_dict = {"Name":input_goodName}

    # 创建一个空列表
    price_list = []

    # 生成日期并添加到字典中
    current_date = start_date
    Loader = None


    while current_date <= end_date:
        # 如果存在于字典中，则写入装载器中,如果不存在与字典中，则不变
        if current_date.strftime("%Y-%m-%d") in result_dict:
            Loader = result_dict[current_date.strftime("%Y-%m-%d")]
        # 将装载器内容写入对应日期中
        date_dict[current_date.strftime("%Y-%m-%d")] = Loader
        # 将装载器内容添加到列表中
        price_list.append(Loader)

        current_date += timedelta(days=1)

    all_df = all_df.join(pd.DataFrame(price_list, columns=[input_goodName]))

all_df.to_csv(csv_file_path, index=False)