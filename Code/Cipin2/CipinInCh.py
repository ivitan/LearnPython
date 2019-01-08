# -*- coding: UTF-8 -*-
# Author:Vitan
import jieba
import matplotlib.pyplot as plt
from  wordcloud import WordCloud

# 读取文件内容
with open('ch.txt','r',encoding = 'UTF-8') as f:
    content = f.read()

# 结巴分词
wordList = jieba.cut(content)

# 词频统计
data = {}
for word in wordList:
    if len(word)==1:
        continue
    else:data[word]=data.get(word,0)+1

# 匿名函数获取每个单词的次数项统，降序
result = list(data.items())
result.sort(key=lambda x:x[1],reverse=True) # 排序
for i in range(20):
    print(result[i])

# 设置词云
wordSplit = " ".join(dict(result))
wc = WordCloud(background_color="black",  # 设置背景颜色
               # mask = "图片",  #设置背景图片
               max_words=2000,  # 设置最大显示的字数
               # stopwords = "", #设置停用词
               font_path="/usr/share/fonts/noto-cjk/NotoSansCJK-Medium.ttc",
               # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
               max_font_size=50,  # 设置字体最大值
               random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
               )
mywc = wc.generate(wordSplit)  # 生成词云

# 展示词云图
plt.imshow(mywc)
plt.axis("off")
plt.show()
wc.to_file('mywor.png')  # 保存图片文件
