# -*- coding: UTF-8 -*-
# Author:Vitan
# 摄氏度转华氏度 华氏°F＝ ℃×9/5＋32
clesius = float(input('请输入摄氏温度：'))
fahrenheit = clesius * 9/5 +32
print("转换后的温度是{:.2f}°F".format(fahrenheit))
# 华氏转度摄氏度 摄氏 ℃＝5/9（°F－32
fahrenheit = float(input('请输入华氏温度:'))
celsius = 5/9*(fahrenheit - 32)
print("转换后的温度是{:.2f}°C".format(celsius))



# if 语句
a = int(input('摄氏度转华氏度请输入1\n华氏度转摄氏度请输入2\n'))

if a == 1:
    clesius = float(input('请输入摄氏温度：'))
    fahrenheit = clesius * 9 / 5 + 32
    print("{:.2f}摄氏温度转换华氏温度是{:.2f}°F".format(clesius,fahrenheit))
else:
    fahrenheit = float(input('请输入华氏温度:'))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("{:.2f}华氏温度转换后的温度是{:.2f}°C".format(fahrenheit,celsius))

    # while 语句
    while True:
        a = int(input('摄氏度转华氏度请输入1\n华氏度转摄氏度请输入2\n'))

    if a == 1:
        clesius = float(input('请输入摄氏温度：'))
        fahrenheit = clesius * 9 / 5 + 32
        print("{:.2f}摄氏温度转换华氏温度是{:.2f}°F".format(clesius,fahrenheit))
    elif a == 2:
        fahrenheit = float(input('请输入华氏温度:'))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("{:.2f}华氏温度转换后的温度是{:.2f}°C".format(fahrenheit,celsius))
    else:
        break
