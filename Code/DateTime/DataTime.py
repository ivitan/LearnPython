# -*- coding: utf-8 -*-
# author by : Vitan

# 一、处理日期时间
# 取系统时间
from datetime import datetime,timedelta
now = datetime.now()
print(now)

# 转换成‘2017年9月30日星期六10时28分56秒’格式字符串
dateStr = datetime.strftime(now,"%Y-%m-%d %H:%M:%S")
date = '{0:%Y}年{0:%m}月{0:%d}日{0:%H}时{0:%M}分{0:%S}秒'.format(now)
print(date)

# 2018-10-25 22:00 转换成一个日期时间变量
end = datetime.strptime('2018-10-25 22:00','%Y-%m-%d %H:%M')
time = end - now
print(time.days,'天')