#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-11-19 上午10:12
# @Author  : Vitan

import pandas
import numpy as np

data = pandas.read_excel('心脏病患者临床数据.xlsx')

sex=[]
for s in data['性别']:
    if s == '男':
        sex.append(0)
    else:
        sex.append(1)

age = []
for a in data['年龄']:
    if a == '<70':
        age.append(1)
    elif a == '70-80':
        age.append(2)
    else:
        age.append(3)

drink = []
for dr in data['饮酒']:
    if dr == '是':
        drink.append(0)
    else:
        drink.append(1)

smoke = []
for s in data['吸烟']:
    if dr == '是':
        smoke.append(0)
    else:
        smoke.append(1)

day = []
for d in data['住院天数']:
    if d == '<7':
        day.append(1)
    elif d == '7-14':
        day.append(2)
    else:
        day.append(3)

ill = []
for i in data['疾病']:
    if i == '心梗':
        ill.append(0)
    else:
        ill.append(1)

#处理后的数据
data1=data
data1['性别'] = sex
data1['年龄'] = age
data1['住院天数'] = day

#将数据转成数组
data_arr = np.array(data1)
print(data_arr)