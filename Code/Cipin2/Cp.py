# -*- coding: UTF-8 -*-
# Author:Vitan
with open('cp.txt','r') as f:
    content = f.read()

# 清洗数据
import string
content = content.lower()  # 格式化数据，转为小写
for i in string.punctuation:  # 去除所有标点符号
    content = content.replace(i, ' ')
wordList = content.split()  # 切片分词

# 排除语法型词汇，代词、冠词、连词等无语义词
noMean = {'a','an','the','i','do','am','you','no','t','m','d','ve'}
wordSet = set(wordList) - noMean
wordList = list(wordSet)

# 统计单词数量
data = {}
for word in wordList:
    #data[word] = data.get(word, 0) + 1
    data[word] = wordList.count(word)

for key in data:
    print(key,data[key],'次')
print("============")

# list.sort() 排序
wordList = list(data.items())
# 函数定义
'''
def takeSecond(elem): # 定义函数，获取每个单词的次数项
    return elem[1]
wordList.sort(key = takeSecond,reverse = True)
'''
# 匿名函数
wordList.sort(key = lambda x:x[1],reverse = True)
print(wordList)
print("============")

# 排序
hist = []
for key, value in data.items():
    hist.append([value, key])
hist.sort(reverse = True)  # 降序

# 前20个
for i in range(20):
    print(hist[i])