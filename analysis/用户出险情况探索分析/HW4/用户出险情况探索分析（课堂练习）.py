
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
auto = #将auto_ins.csv读取进来,命名为auto

# In[134]:
#定义codeMy(x)函数，其作用是对auto里的loss重新编码为1/0，有数值为1，命名为loss_flag
def codeMy(x):
      
    
 #对auto里的loss重新编码为1/0，有数值为1，命名为loss_flag
#%%
auto["loss_flag1"]= #应用匿名函数的方法对loss重新编码为1/0，有数值为1，命名为loss_flag1


# In[116]:

#对loss_flag列进行描述分析（计数计频次）


#对loss_flag出险情况进行百分比统计


#绘制是否出险柱形图



# In[116]:
# ### 3、分析是否出险和年龄、驾龄、性别、婚姻状态等变量之间的关系

fig =#设置画布fig
ax1 = #将画布设计成1行2列结构，增加第一个子图层ax1
ax2 = #将画布设计成1行2列结构，增加第二个子图层ax2
#是否出险和年龄关系：绘制箱形图（盒须图），分析出险和年龄的关系


#是否出险和驾龄：绘制箱形图（盒须图），分析出险和驾龄的关系


# In[120]:
#是否出险和性别：绘制面积堆积柱形图，分析出险和性别的关系
from stack2dim import *


# In[121]:
#是否出险和婚姻状态：绘制面积堆积柱形图，分析出险和婚姻的关系

# In[126]:



