# -*- coding: UTF-8 -*-
# Author:Vitan
content = '''I walk these streets,searching to find The steps that we left behind Your lonely eyes stare back at mine In pictures from that time I hold my heart,closing my eyes I see your smile,lies behind In this place,you entered my life How I wish,you were still mine I know that if I see you again Beside that cafe we met I＇d forget about the past Lose track of time,with you Talking about our lives To show you a whole new side of me And see the changes we＇ve made,can we Be more than we have been Start our story again All I can say,is tell you just one thing  I hold my heart,closing my eyes I see your smile,lies behind In this place,you entered my life How I wish,you were still mine I know that if I see you again Beside that cafe we met I＇d forget about the past Lose track of time,with you Talking about our lives To show you a whole new side of me And see the changes we＇ve made,can we Be more than we have been Start our story again All I can say,is tell you just one thing 
'''

# 清洗数据
import string
content = content.lower()  # 格式化数据，转为小写
for i in string.punctuation:  # 去除所有标点符号
    content = content.replace(i, ' ')
wordList = content.split()  # 切片分词
# 统计单词数量
data = {}
for word in wordList:
    data[word] = data.get(word, 0) + 1
# 排序
hist = []
for key, value in data.items():
    hist.append([value, key])
hist.sort(reverse=True)  # 降序
# 前20个
for i in range(20):
    print(hist[i])