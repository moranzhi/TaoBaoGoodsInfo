import re
import requests
from DrissionPage import ChromiumPage
import json
import csv
import time

# 保存为csv
f = open('data.csv', mode='w', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '发货地', '销售量', '店铺', '价格'])
# 写入表头
csv_writer.writeheader()
# 打开浏览器
driver = ChromiumPage()
# 访问
driver.get('https://www.taobao.com/')
# 监听数据包→从网页中抓包，找到返回相应的网址，不要？后面的data包,记得url要截掉上面那个get的部分
driver.listen.start('h5/mtop.relationrecommend')
# 输入商品关键字
driver.ele('css:#q').input('ws')
# 进行搜索
driver.ele('css:.btn-search').click()
# 翻页
for page in range(10):
    # 设置延时
    time.sleep(2)
    # 滑动页面到最下方，使数据包加载
    driver.scroll.to_bottom()
    # 等待数据加载
    resp = driver.listen.wait()
    # 动态加载的话
    text = resp.response.body
    info = re.findall('mtopjsonp\d+\((.*)', text)[0].replace(')', '')

    json_data = json.loads(info)
    items = json_data['data']['itemsArray']
    dits = []

    for item in items:
        dit = {
            '标题': item['title'],
            '发货地': item['procity'],
            '销售量': item['realSales'],
            '店铺': item['shopInfo']['title'],
            '价格': item['priceShow']['price'],
        }
        dits.append(dit)
        csv_writer.writerow(dit)
    driver.ele('css:.next-next').click()
    # 写入数据
