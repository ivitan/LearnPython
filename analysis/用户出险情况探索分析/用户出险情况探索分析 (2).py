
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os

#以下是相关分析步骤与过程
#1、将Hw4文件导入

#2、使用auto_ins作如下分析

# ### 1、首先对loss重新编码为1/0，有数值为1，命名为loss_flag
# ###2、对loss_flag列进行描述分析（计数计频次）
# ###3、分析是否出险和年龄、驾龄、性别、婚姻状态等变量之间的关系

# In[132]:

#Hw4文件导入
os.chdir(r'G:\Python\Python\HW4')
#将auto_ins.csv读取进来,命名为auto
auto = pd.read_csv('auto_ins.csv',encoding='gbk')

# In[134]:
#定义codeMy(x)函数，其作用是对auto里的loss重新编码为1/0，有数值为1，命名为loss_flag
def codeMy(x):
    if x > 0:
        return 1
    else:
        return 0
     
 #对auto里的loss重新编码为1/0，有数值为1，命名为loss_flag
auto.loss_flag = auto.Loss.map(codeMy)
#%%
#应用匿名函数的方法对loss重新编码为1/0，有数值为1，命名为loss_flag1
auto["loss_flag1"]= auto.Loss.map(lambda x:1 if x > 0 else 0)


# In[116]:

#对loss_flag列进行描述分析（计数计频次）
auto.loss_flag.value_counts()

#对loss_flag出险情况进行百分比统计
auto.loss_flag.value_counts()/auto.loss_flag.count()

#绘制是否出险柱形图
auto.loss_flag.value_counts().plot(kind="bar")



# In[116]:
# ### 3、分析是否出险和年龄、驾龄、性别、婚姻状态等变量之间的关系

#设置画布fig
fig = plt.figure()
#将画布设计成1行2列结构，增加第一个子图层ax1
ax1 = fig.add_subplot(1,2,1)
#将画布设计成1行2列结构，增加第二个子图层ax2
ax2 = fig.add_subplot(1,2,2)
#是否出险和年龄关系：绘制箱形图（盒须图），分析出险和年龄的关系
sns.boxplot(x="loss_flag",y="Age",data=auto,ax =ax1)

#是否出险和驾龄：绘制箱形图（盒须图），分析出险和驾龄的关系
sns.boxplot(x="loss_flag",y="exp",data=auto,ax =ax2)


# In[120]:
#是否出险和性别：绘制面积堆积柱形图，分析出险和性别的关系
from stack2dim import *
stack2dim(auto,"Gender","loss_flag")


# In[121]:
#是否出险和婚姻状态：绘制面积堆积柱形图，分析出险和婚姻的关系
stack2dim(auto,"Marital","loss_flag")

# In[126]:



