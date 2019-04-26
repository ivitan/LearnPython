from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

# 读取数据集
boston = load_boston()

# 划分训练集与测试集
#随机擦痒25%的数据构建测试样本，剩余作为训练样本
x_train,x_test,y_train,y_test = train_test_split(boston.data,boston.target,test_size=0.3) #random_state：是随机数的种子

x = x_train[:,12].reshape(-1,1)
poly= PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

# 建立多项式回归模型
lrp = LinearRegression()
lrp.fit(x_poly,y_train)

lr = LinearRegression()
lr.fit(x,y_train)
w = lr.coef_
b = lr.intercept_

# 预测
x_poly2 = poly.transform(x_test[:, 12].reshape(-1,1))
y_ploy_predict = lrp.predict(x_poly2)

# 画图
plt.scatter(x_test[:,12], y_test)
plt.plot(x, w * x + b, 'g')
plt.scatter(x_test[:,12], y_ploy_predict, c='r')
plt.show()
