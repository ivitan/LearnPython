# a+b+c=100,a**2+b**2=c**2,a,b,c为自然数,求a,b,c
# 每台机器的总时间不同,但是执行基本运算数大体相同
#T(n) = n^3 * 2
import time

start_time = time.time()

# 枚举a,b,c
# 时间复杂度 T = 1000 * 1000 * 1000 * 2
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c==1000 and a**2+b**2==c**2:
#                 print("a,b,c:%d,%d,%d" % (a,b,c))
# 枚举a,b
# 时间复杂度 T = 1000 * 1000 * 2
for a in range(0,1001):
    for b in range(0,1001):
        c = 1000 - a- b
        if a+b+c==1000 and a**2+b**2==c**2:
            print("a,b,c:%d,%d,%d" % (a,b,c))

end_time = time.time()
print("time:%d" % (end_time - start_time))