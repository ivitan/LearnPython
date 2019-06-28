# -*- coding: UTF-8 -*-
# Author:Vitan
# 解析身份证号地出生市区，生日，性别
s = input('请输入身份证号码：')
print('所在省市：{}'.format(s[:2]))
print('所在地区：{}'.format(s[2:4]))
print('所在县区：{}'.format(s[4:6]))
print('出生年月日：{}'.format(s[6:14]))
print('户口归属派出所：{}'.format(s[14:16]))
if int(s[-2]) % 2 == 0:
    print('性别：女')
else:
    print('性别：男')
print('校验位：{}'.format(s[-1]))
