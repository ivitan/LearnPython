import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 读取数据集
boston = load_boston()

print(boston.keys())
print(boston.target)# 房价数据
print(boston.feature_names) # 数据集特征

# 划分训练集与测试集
#随机擦痒25%的数据构建测试样本，剩余作为训练样本
X_train,X_test,y_train,y_test = train_test_split(boston.data,boston.target,test_size=0.3) #random_state：是随机数的种子
print(X_train.shape,y_train.shape)

# 建立模型
LineR = LinearRegression()
LineR.fit(X_train,y_train)

# 检查模型好坏
x_predict = LineR.predict(X_test)
print("各列权重",LineR.coef_)
print("测试集上的评分：",LineR.score(X_test, y_test))
print("训练集上的评分：",LineR.score(X_train, y_train))
print("预测的均方误差：", np.mean(x_predict - y_test)**2)
print("最小目标值:",np.min(boston.target))
print("平均目标值:",np.mean(boston.target))

# 画图
X = boston.data[:,12].reshape(-1,1)
y = boston.target

plt.scatter(X,y)

LineR2 = LinearRegression()
LineR2.fit(X,y)
y_predict = LineR2.predict(X)
plt.plot(X,y_predict,'r')
plt.show()
