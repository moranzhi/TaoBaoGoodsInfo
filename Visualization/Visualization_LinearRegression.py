import numpy as np
import matplotlib.pyplot as plt
import chardet
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import datetime

from tensorflow.python.keras.losses import mean_squared_error
from tensorflow.python.ops.metrics_impl import mean_absolute_error

# 检测文件编码
with open('商品价格.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

# 设置全局字体配置（例如在Linux或Mac上）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统中的黑体，Linux或Mac可能需要其他字体名如'STHeiti'等
plt.rcParams['axes.unicode_minus'] = False
# 读取CSV数据
df = pd.read_csv('商品价格.csv', encoding=encoding)

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import datetime


def predict_data(df, column_name):
    # 获取数据
    x = []
    for date in df["Date"]:
        # 将日期对象转换为时间戳，并将结果添加到 x 列表中
        date = pd.to_datetime(date)
        x.append(date.timestamp())
    y = df.get(column_name)

    # 将 x 和 y 转换为 NumPy 数组
    X = np.array(x).reshape(-1, 1)
    Y = np.array(y).reshape(-1, 1)

    # 找到 NaN 值的位置
    nan_indices_X = np.isnan(X)
    nan_indices_Y = np.isnan(Y)
    # 找到包含 NaN 值的行
    nan_rows_X = np.any(nan_indices_X, axis=1)
    nan_rows_Y = np.any(nan_indices_Y, axis=1)
    # 删除包含 NaN 值的行
    X = np.delete(X, np.where(nan_rows_X)[0], axis=0)
    X = np.delete(X, np.where(nan_rows_Y)[0], axis=0)
    Y = np.delete(Y, np.where(nan_rows_X)[0], axis=0)
    Y = np.delete(Y, np.where(nan_rows_Y)[0], axis=0)

    # 创建线性回归模型
    model = LinearRegression()

    # 拟合模型
    model.fit(X, Y)

    # 生成新的 x 值，用于预测
    # 生成起始时间戳
    start_timestamp = datetime.datetime(2025, 4, 17).timestamp()

    # 生成结束时间戳
    end_timestamp = datetime.datetime(2025, 12, 1).timestamp()

    # 初始化时间戳列表
    timestamps = []

    # 循环生成时间戳
    while start_timestamp <= end_timestamp:
        timestamps.append(start_timestamp)
        start_timestamp += 86400  # 加一天的秒数

    # 将时间戳转换为二维数组
    timestamps = np.array(timestamps).reshape(-1, 1)

    # 预测
    y_pred = model.predict(timestamps)


    # 绘制原始数据
    plt.scatter(X, Y, label='Original Data')

    # 添加横轴标签
    plt.xlabel('时间戳')

    # 添加纵轴标签
    plt.ylabel('价格')

    # 添加标题
    plt.title(column_name)

    # 绘制预测结果
    plt.plot(timestamps, y_pred, label='Predicted Data')

    # 添加图例
    plt.legend()

    # 显示图形
    plt.show()


# 运行函数
predict_data(df, "余额代充充值卡 店铺回头客过万 12年老店代充充值卡11年2金冠 超快20/50/100美金")
predict_data(df, "【自营】茅台（MOUTAI）飞天茅??3??00ml 双瓶装海外版酱香白酒")
predict_data(df,
             "【新品】瑞幸咖啡元气弹速溶冻干咖啡粉生椰拿铁冰美式黑咖啡无??立顿茉莉花茶绿茶红茶柠檬片菊花茶玫瑰花茶茶包伯爵冷泡茶叶果茶")
predict_data(df, "七彩虹电脑电显卡 12年老店 ??0种颜色电显卡RTX5080/4080 super 16G华硕微星技嘉索泰影??080 S")
predict_data(df, "圣农嘟嘟翅饱满大号经典香烤翅中280g*3包空气炸锅半成品小食")