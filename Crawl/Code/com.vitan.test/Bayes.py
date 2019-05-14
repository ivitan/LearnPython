#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-11-19 上午10:12
# @Author  : Vitan

import pandas as pd
import numpy as np
import xlrd

# data = pd.read_excel('心脏病患者临床数据.xlsx')
data = xlrd.open_workbook('心脏病患者临床数据.xlsx')
table = data.sheets()[0] # 打开第一张表
nrows = table.nrows # 获取表的行数
sex,age,drink,smoke,day=[],[],[],[],[]
for i in range(nrows): # 循环逐行打印
    people = table.row_values(i)[1:]
    # if i[1] == '男':
    #     sex.append(1)
    # else:
    #     sex.append(2)
    # print(sex)
    print(people)
print('======================================')

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


#处理后的数据
data1=data
data1['性别'] = sex
data1['年龄'] = age
data1['住院天数'] = day

#将数据转成数组
data_arr = np.array(data1)
print(data_arr)


# 利用贝叶斯算法对给定的组别进行分类
def Bayes(sex, age, KILLP, drink, smoke, day):
    # 初始化值
    x1_y1, x2_y1, x3_y1, x4_y1, x5_y1, x6_y1 = 0, 0, 0, 0, 0, 0
    x1_y2, x2_y2, x3_y2, x4_y2, x5_y2, x6_y2 = 0, 0, 0, 0, 0, 0
    y1 = 0
    y2 = 0
    # 计算为心梗的概率
    for a in data_arr:
        if a[6] == '心梗':
            y1 += 1
            if a[0] == sex:
                x1_y1 += 1
            if a[1] == age:
                x2_y1 += 1
            if a[2] == KILLP:
                x3_y1 += 1
            if a[3] == drink:
                x4_y1 += 1
            if a[4] == smoke:
                x5_y1 += 1
            if a[5] == day:
                x6_y1 += 1
        else:  # 计算患有不稳定性心绞痛的概率
            y2 += 1
            if a[0] == sex:
                x1_y2 += 1
            if a[1] == age:
                x2_y2 += 1
            if a[2] == KILLP:
                x3_y2 += 1
            if a[3] == drink:
                x4_y2 += 1
            if a[4] == smoke:
                x5_y2 += 1
            if a[5] == day:
                x6_y2 += 1

    # 计算每种症状在心梗下的概率
    x1_y1, x2_y1, x3_y1, x4_y1, x5_y1, x6_y1 = x1_y1 / y1, x2_y1 / y1, x3_y1 / y1, x4_y1 / y1, x5_y1 / y1, x6_y1 / y1

    # 计算每种症状在不稳定性心绞痛的概率
    x1_y2, x2_y2, x3_y2, x4_y2, x5_y2, x6_y2 = x1_y2 / y2, x2_y2 / y2, x3_y2 / y2, x4_y2 / y2, x5_y2 / y2, x6_y2 / y2

    # 多个症状在心梗下的概率
    x_y1 = x1_y1 * x2_y1 * x3_y1 * x4_y1 * x5_y1 * x6_y1

    # 多个症状在不稳定性心绞痛下的概率
    x_y2 = x1_y2 * x2_y2 * x3_y2 * x4_y2 * x5_y2 * x6_y2

    ##初始化各个特征x的值
    x1, x2, x3, x4, x5, x6 = 0, 0, 0, 0, 0, 0
    for a in data_arr:
        if a[0] == sex:
            x1 += 1
        if a[1] == age:
            x2 += 1
        if a[2] == KILLP:
            x3 += 1
        if a[3] == drink:
            x4 += 1
        if a[4] == smoke:
            x5 += 1
        if a[5] == day:
            x6 += 1
    lens = len(data_arr)
    # 所有x的可能性
    x = x1 / lens * x2 / lens * x3 / lens * x4 / lens * x5 / lens * x6 / lens
    # 分别计算心梗和不稳定性心绞痛的概率
    y1_x = (x_y1) * (y1 / lens) / x
    print(y1_x)
    y2_x = (x_y2) * (y2 / lens) / x
    print(y2_x)

    # 判断是哪中疾病的可能更大
    if y1_x > y2_x:
        print('病人患心梗的可能更大，可能性为：', y1_x)
    else:
        print('病人患不稳定性心绞痛的可能更大，可能性为：', y2_x)


# 判断：性别=‘男’，年龄<70, KILLP=1，饮酒=‘是’，吸烟=‘是”，住院天数<7
Bayes(0, 1, 1, '是', '是', 1)