#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-11-12 10:10
# @Author  : Vitan

from sklearn.datasets import load_sample_image
import matplotlib.image as img
from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt
import sys


picture = load_sample_image('china.jpg')
pic2 = img.imread('v.jpg')
# 根据图片的分辨率，可适当降低分辨率。
image = picture[::3,::3]# 横纵每三个点去一个颜色值
plt.imshow(image)
img.imsave('E://pure.jpg',image)
plt.show()

# 再用k均值聚类算法，将图片中所有的颜色值做聚类。
X = image.reshape(-1,3) #reshape为一维
mod = KMeans(n_clusters = 64)
labels = mod.fit_predict(X)  #每个点的颜色分类，0-63
colors = mod.cluster_centers_  #64个聚类中心，颜色值

# 还原颜色，维数，数据类型
new_img = colors[labels]
new_img = new_img.reshape(image.shape)
new_img = new_img.astype(np.uint8)
print(new_img)
plt.imshow(new_img)
img.imsave('E://zip.jpg',new_img)
size = sys.getsizeof('E://zip.jpg')
print(size)
plt.show()