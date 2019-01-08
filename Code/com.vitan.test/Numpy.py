# -*- coding: utf-8 -*-
# author by : Vitan

'''
a = a1,a2,a3,·····,an
b = b1,b2,b3,·····,bn
求：
c = a12+b13,a22+b23,a32+b33,·····+an2+bn3
1.用列表+循环实现，并包装成函数
2.用numpy实现，并包装成函数
3.对比两种方法实现的效率，给定一个较大的参数n，用运行函数前后的timedelta表示。
'''

# 用列表+循环实现，并包装成函数
def lsSum(n):
    a = list(range(n))
    b = list(range(0,5*n,5))
    c = []
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**3)
    return (c)
print(lsSum(10))

# 用numpy实现，并包装成函数
import numpy
def npSum(n):
    a = numpy.arange(n)
    b = numpy.arange(0,5*n,5)
    c = a**2 + b**3
    return (c)
print(npSum(10))

# 对比两种方法实现的效率，给定一个较大的参数n，用运行函数前后的timedelta表示。
from datetime import datetime
start = datetime.now()
lsSum(100000)
time = datetime.now()-start
print(time)

start = datetime.now()
npSum(100000)
time = datetime.now()-start
print(time)

# 三、尝试把a,b定义为三层嵌套列表和三维数组，求相对应元素的ai2+bi3
import numpy
def liSum(n):
    a = numpy.arange(n)
    b = numpy.arange(0,5*n,5)
    c = numpy.array([[a,b],[a**2,b**3]])
    return (c)
print(npSum(10))

# 对比两种数据类型处理方法及效率的不同。
start = datetime.now()
liSum(100000)
time = datetime.now()-start
print(time)