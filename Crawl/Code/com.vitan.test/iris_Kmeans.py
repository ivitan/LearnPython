#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-11-5 下午12:13
# @Author  : Vitan
# @File    : iris_Kmeans.py

#2. 鸢尾花花瓣长度数据做聚类并用散点图显示。
from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
iris = load_iris()
data = iris.data
iris_length = data[:,2]

x = np.array(iris_length)
y = np.zeros(x.shape[0])

flag = True
while flag:
    y = xclassify(x,y,kc)
    kc,flag = kcmean(x,y,kc,3)
print(kc,flag)
import matplotlib.pyplot as plt
plt.scatter(iris_length, iris_length, marker='D', c=y, alpha=0.5)  #散点图
plt.show()