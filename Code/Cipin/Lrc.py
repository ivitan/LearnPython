# -*- coding: UTF-8 -*-
# Author:Vitan

lrc = '''I walk these streets,searching to find The steps that we left behind Your lonely eyes stare back at mine In pictures from that time I hold my heart,closing my eyes I see your smile,lies behind In this place,you entered my life How I wish,you were still mine I know that if I see you again Beside that cafe we met I＇d forget about the past Lose track of time,with you Talking about our lives To show you a whole new side of me And see the changes we＇ve made,can we Be more than we have been Start our story again All I can say,is tell you just one thing  I hold my heart,closing my eyes I see your smile,lies behind In this place,you entered my life How I wish,you were still mine I know that if I see you again Beside that cafe we met I＇d forget about the past Lose track of time,with you Talking about our lives To show you a whole new side of me And see the changes we＇ve made,can we Be more than we have been Start our story again All I can say,is tell you just one thing '''
lrc = lrc.lower() #转换为小写
# 替换所有符号
import string
for i in string.punctuation:
    lrc = lrc.replace(i,' ')
lrc = lrc.split()
lrcSet = set(lrc)
lrclist = list(lrcSet)
result = {}
for item in lrclist :
    result[item] = lrclist.count(item)
print(result)