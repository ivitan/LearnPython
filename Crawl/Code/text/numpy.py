#1.用列表+循环  实现，并包装成函数。

def pySum(n):
    a = list(range(n))
    b = list(range(0,5*n,5))
    c = []
    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 3)
    return(c)

print(pySum(10))

#2.用数组numpy实现，并包装成函数。

import numpy
def npSum(n):
    a = numpy.arange(n)
    b = numpy.arange(0, 5 * n, 5)
    c = a**2+b**3
    return(c)
print(npSum(10))

#3.对比两种方法实现的效率，给定一个较大的参数n，用运行函数前后的timedelta表示。

from datetime import datetime
start =datetime.now()
pySum(100000)
delta=datetime.now()-start
print(delta)

start =datetime.now()
npSum(100000)
delta=datetime.now()-start
print(delta)

#4.时间计算

#列表用的时间

from datetime import datetime
start=datetime.now()
pySum(100000)
now1=datetime.now()-start
print(now1)

#数组用的时间

start=datetime.now()
npSum(100000)
now2=datetime.now()-start
print(now2)
