#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-13 下午6:18
# @Author  : Vitan
# @File    : PolynomialBoston.py

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
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
X = X_train[:,12].reshape(-1,1)
y = boston.target

LineR2 = LinearRegression()
LineR2.fit(X,y)
y_predict = LineR2.predict(X)

poly = PolynomialFeatures(degree=2)
X_ploy = poly.fit_transform(X)

lrp = LinearRegression()
lrp.fit(X_ploy,y)
y_predict_p = lrp.predict(X_ploy)

plt.scatter(X,y)
plt.plot(X,y_predict_p,'r')
plt.show()

poly = PolynomialFeatures(degree=2)
X_ploy = poly.fit_transform(X)

lrp = LinearRegression()
lrp.fit(X_ploy,y)
plt.scatter(X,y_predict)
plt.scatter(X,y_predict_p)
plt.show()
