#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-11-19 下午1:09
# @Author  : Vitan
# @File    : xrld.py

import xlrd
def read_file(url):
    data = xlrd.open_workbook(url)
    table = data.sheets()[0] # 打开第一张表
    nrows = table.nrows # 获取表的行数
    for i in range(nrows): # 循环逐行打印
        print(table.row_values(i)[1:])

def main():
    read_file('心脏病患者临床数据.xlsx')

if __name__ == '__main__':
    main()