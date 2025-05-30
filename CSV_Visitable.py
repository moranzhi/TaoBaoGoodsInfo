import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
file_path = 'data_2025-04-03_100g金条.csv'
data = pd.read_csv(file_path)

# 显示数据的前几行
print(data.head())

# 进行数据可视化

plt.figure(figsize=(10, 6))
plt.plot(data['title'], data['price'])
plt.title('100g金条价格走势')
plt.xlabel('title')
plt.ylabel('price')
plt.grid(True)
plt.show()
