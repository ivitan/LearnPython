from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

boston = load_boston()
data = boston.data
print(boston.keys())

x = data[:,5]
y = boston.target

plt.scatter(x,y)
plt.plot(x,9*x-30,c = 'r') # y = wx+b
plt.show()

# 使用LinearRegression 计算w，b的值
LineR = LinearRegression()
LineR.fit(x.reshape(-1,1),y)
w = LineR.coef_
b = LineR.intercept_

plt.scatter(x,y)
plt.plot(x,w*x+b,c = 'r') # y = wx+b
plt.show()
