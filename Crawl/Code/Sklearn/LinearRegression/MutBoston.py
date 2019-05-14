import numpy as np
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

boston = load_boston()

# 划分数据
x_train, x_test, y_train, y_test = train_test_split(boston.data,boston.target,test_size=0.3)

# 建模
LineR = LinearRegression()
LineR.fit(x_train,y_train)

# 检测模型好坏
x_predict = LineR.predict(x_test)

print("预测的均方误差：", np.mean(x_predict - y_test)**2)
print("模型的分数：",LineR.score(x_test, y_test))

# 画图
x = boston.data[:,12].reshape(-1,1)
y = boston.target

plt.figure(figsize=(10,6))
plt.scatter(x,y)

LineR2 = LinearRegression()
LineR2.fit(x,y)
y_pred=LineR2.predict(x)
plt.plot(x,y_pred,'r')
plt.show()
