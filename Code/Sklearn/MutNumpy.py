import numpy as np

m = np.arange(24)
n = m.reshape(3,8)# 视图
print(m)
print('===================')
print(n)

m.shape = (2,3,1,4)# 直接改变形状
print(m)
print('===================')
print(m.resize(3,8))#直接改变形状
print('===================')
print(n.ravel())
print('===================')
print(n.flatten())#重新分配内在
print('===================')

a = np.random.random(10)  # (0,1)以内10个随机浮点数
b = np.random.randint(1,100,[5,5]) # (1,100）以内的5行5列随机整数
c = np.random.rand(2,3) # 产生2行3列均匀分布随机数组
d = np.random.randn(3,3) # 3行3列正态分布随机数据

print(a)
print('===================')
print(b)
print('===================')
print(c)
print('===================')
print(d)
print('===================')
print(np.max(a),np.min(a),np.mean(a),np.std(a),np.median(a))

