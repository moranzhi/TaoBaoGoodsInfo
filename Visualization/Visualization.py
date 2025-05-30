import chardet
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# 检测文件编码
with open('商品价格.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

# 设置全局字体配置（例如在Linux或Mac上）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统中的黑体，Linux或Mac可能需要其他字体名如'STHeiti'等
plt.rcParams['axes.unicode_minus'] = False
# 读取CSV数据
df = pd.read_csv('商品价格.csv', encoding=encoding)

# 绘制柱状图
def plot_bar(df, column):
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Bar Chart of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

# 绘制箱型图
def plot_box(df, column):
    df[column].plot(kind='box')
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.ylabel('Value')
    plt.show()

# 绘制饼图
def plot_pie(df, column):
    df[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(f'Pie Chart of {column}')
    plt.ylabel('')
    plt.show()

# 绘制折线图
def plot_line(df, column):
    df[column].plot(kind='line')
    # 设置X轴的刻度格式为日期
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m%d|'))
    # 设置X轴的刻度间隔为1天
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
    plt.title(f'Line Chart of {column}')
    plt.xlabel(column)
    plt.ylabel('Value')
    plt.show()

# 绘制散点图
def plot_scatter(df, column1, column2):
    plt.figure(figsize=(26, 10))

    df.plot(kind='scatter', x=column1, y=column2)

    # 设置X轴的刻度格式为日期
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m%d|'))
    # 设置X轴的刻度间隔为1天
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=30))
    plt.title(f'Scatter Plot of {column1} vs {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

plot_pie(df, '金龙鱼菜籽油 外婆乡小榨食用油5L巴蜀风味非转基因压榨大桶家用')
plot_bar(df, '【新品】瑞幸咖啡元气弹速溶冻干咖啡粉生椰拿铁冰美式黑咖啡无??立顿茉莉花茶绿茶红茶柠檬片菊花茶玫瑰花茶茶包伯爵冷泡茶叶果茶')
plot_box(df, '【自营】茅台（MOUTAI）飞天茅??3??00ml 双瓶装海外版酱香白酒')
plot_line(df, '【自营】茅台（MOUTAI）飞天茅??3??00ml 双瓶装海外版酱香白酒')
plot_scatter(df, 'Date', '金龙鱼菜籽油 外婆乡小榨食用油5L巴蜀风味非转基因压榨大桶家用')
plot_bar(df, '金龙鱼菜籽油 外婆乡小榨食用油5L巴蜀风味非转基因压榨大桶家用')