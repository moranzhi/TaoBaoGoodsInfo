import matplotlib.pyplot as plt
import numpy
import numpy as np
from keras import Sequential
from keras.src.layers import MaxPooling2D, Conv2D, Dense, Flatten
import pandas as pd
import chardet
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers


def cnn_pipeline(x_train, y_train, x_test, y_test, epochs=3, validation_split=0.1, num_samples=10):
    # 定义卷积神经网络
    def build_model():
        model = Sequential()
        model.add(layers.Embedding(input_dim=1000, output_dim=64))
        model.add(LSTM(64, input_shape=(x_train.shape[1], x_train.shape[2])))
        model.add(Dense(1))
        # 编译模型

        return model

    model = build_model()

    # 训练模型
    def train_model(model, x_train, y_train, epochs, validation_split):
        history = model.fit(x_train, y_train, epochs=epochs, validation_split=validation_split)
        return history

    history = train_model(model, x_train, y_train, epochs, validation_split)

    # 评估模型
    def evaluate_model(model, x_test, y_test):
        loss, accuracy = model.evaluate(x_test, y_test)
        print(f"Test accuracy: {accuracy}")

    evaluate_model(model, x_test, y_test)

    # 预测
    def predict_model(model, x_test, num_samples):
        predictions = model.predict(x_test[:num_samples])
        return predictions

    predictions = predict_model(model, x_test, num_samples)

    # 可视化
    # 绘制训练和验证集的准确率和损失
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # 显示前10个测试样本的预测结果
    def plot_samples(x_test, predictions, num_samples):
        fig, axes = plt.subplots(1, num_samples, figsize=(num_samples * 2, 2))
        for i in range(num_samples):
            ax = axes[i]
            ax.imshow(x_test[i].reshape(28, 28), cmap='gray')
            ax.set_title(f"Predicted: {np.argmax(predictions[i])}")
            ax.axis('off')
        plt.show()

    plot_samples(x_test, predictions, num_samples)

    return predictions


# 程序开始
# 检测文件编码
with open('商品价格.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

# 设置全局字体配置（例如在Linux或Mac上）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统中的黑体，Linux或Mac可能需要其他字体名如'STHeiti'等
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('商品价格.csv', encoding=encoding)
# 读取CSV数据
data = np.genfromtxt('商品价格.csv', delimiter=',')
X = data[1:, 1:].reshape(413, 6, 1)
y = []
for date in df["Date"]:
    # 将日期对象转换为时间戳，并将结果添加到 x 列表中
    date = pd.to_datetime(date)
    y.append(date.timestamp())
y = numpy.array(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# 调用cnn_pipeline函数进行卷积神经网络训练和预测
predictions = cnn_pipeline(X_train, y_train, X_test, y_test)
