import csv

# 文件路径
file_path = "data_2025-04-03_steam充值卡100美金.csv"

# 打开CSV文件
with open(file_path, mode='r', encoding='utf-8') as file:
    # 创建CSV读取器
    csv_reader = csv.reader(file)

    # 跳过表头
    next(csv_reader)
    dict_data = {}
    # 逐行读取
    for row in csv_reader:
        print(row[1])
        if float(row[1]) > 550:
            dict_data[row[3]] = row[1]
            print(dict[row[3]])
        else:
            print("此数据不满足条件")