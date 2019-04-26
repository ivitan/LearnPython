#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-14 下午2:52
# @Author  : Vitan
# @File    : me.vitan.NewsClass.py

import os
import jieba
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

contents, class_list = [], []
# 文件数据路径的构建、读取、导入
def txt_processing(folder_path):
    folder_list = os.listdir(folder_path)

    # 遍历文件夹
    for folder in folder_list:
        new_folder_path = os.path.join(folder_path,folder) # 拼接路径
        files = os.listdir(new_folder_path) # 258/分类

        j = 1
        for file in files:
            # if j > 1000000000000000: # 要读的每个分类的文件个数
            #     break
            if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
                TxtPath = os.path.join(new_folder_path, file)
                with open(TxtPath,'r',encoding='UTF-8') as fp:
                    Txt = (fp.read())
                    # content.append(Txt.replace("\r\n", "").strip())  # 去掉换行符、空格后追加
                contents.append(drop_stopwords(Txt)) # 分词
                class_list.append(folder)
            # j += 1
    print(class_list)
    print(contents)

# 停用词的处理
def drop_stopwords(contents):
    # 导入中文停用词
    with open('stopwords.txt', 'r') as fp:
        stopwords = fp.read().split('\n')

    # jieba 分词
    contents = "".join([word for word in contents if word.isalpha()])  # 去掉英文单词
    contents = [txt for txt in jieba.cut(contents, cut_all=True) if len(txt) >= 2]
    # 去掉停用词
    contents = " ".join([txt for txt in contents if txt not in stopwords])
    print(contents)
    return contents

def main():
    path = '258'
    txt_processing(path)

if __name__=='__main__':
    main()

tfidf = TfidfVectorizer()
x_train, x_test, y_train, y_test = train_test_split(contents, class_list, test_size=0.2)

# # 保存数组
# np.save('conttnes.npy',contents)
# np.save('class_list.npy',class_list)

X_train = tfidf.fit_transform(x_train)
X_test = tfidf.transform(x_test)

# 贝叶斯模型
mulp = MultinomialNB()
mulp_NB = mulp.fit(X_train, y_train)

# 模型预测
y_predict = mulp.predict(X_test)

print('准确率：', mulp.score(X_test, y_test))
print('报告:\n', classification_report(y_test, y_predict))