#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-11-12 09:10
# @Author  : Vitan

from sklearn.datasets import load_sample_image
from matplotlib import pyplot as plt

ChinaImage = load_sample_image('china.jpg')
print(ChinaImage)

plt.imshow(ChinaImage)
plt.show()

plt.imshow(ChinaImage[:,:,1])
plt.show()

plt.imshow(ChinaImage[:,:,2],plt.cm.gray)
plt.show()