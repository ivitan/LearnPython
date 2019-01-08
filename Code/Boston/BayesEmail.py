import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# 预处理
def preprocessing(text):
    text=text.decode("utf-8")
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    stops = stopwords.words('english')
    tokens = [token for token in tokens if token not in stops]

    tokens = [token.lower() for token in tokens if len(token) >= 3]
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(token) for token in tokens]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

file_path = r'C:\Users\Administrator\Desktop\sms.txt'
sms = open(file_path,'r',encoding='utf-8')
sms=open(file_path,'r',encoding='utf-8')
sms_data=[]
sms_label=[]
csv_reader=csv.reader(sms,delimiter='\t')
for line in csv_reader:
    sms_label.append(line[0])
    sms_data.append(preprocessing(line[1]))
sms.close()


#按0.7：0.3比例分为训练集和测试集，再将其向量化
sms_data=np.array(sms_data)
sms_label=np.array(sms_label)

x_train,x_test,y_train,y_test = train_test_split(sms_data,sms_label,test_size=0.3,random_state=0,stratify=sms_label)
print(len(sms_data),len(x_train),len(x_test))
print('x_train',x_train)
print('y_train',y_train)


# 将其向量化
vectorizer=TfidfVectorizer(min_df=2,ngram_range=(1,2),stop_words='english',strip_accents='unicode',norm='l2')
X_train = vectorizer.fit_transform(x_train)
X_test = vectorizer.transform(x_test)

#朴素贝叶斯分类器
clf = MultinomialNB().fit(X_train,y_train)
y_nb_pred = clf.predict(X_test)

# 分类结果显示
print(y_nb_pred.shape,y_nb_pred) # x-test预测结果
print('nb_confusion_matrix:')
cm = confusion_matrix(y_test,y_nb_pred) #混淆矩阵
print(cm)
print('nb_classification_repert:')
cr = classification_report(y_test,y_nb_pred) # 主要分类指标的文本报告
print(cr)

feature_names=vectorizer.get_feature_names() # 出现过的单词列表
coefs=clf.coef_ # 先验概率 p(x_ily),6034 feature_log_preb
intercept = clf.intercept_ # P(y),class_log_prior : array,shape(n...
coefs_with_fns=sorted(zip(coefs[0],feature_names)) #对数概率P(x_i|y)与单词x_i映射

n=10
top=zip(coefs_with_fns[:n],coefs_with_fns[:-(n+1):-1])
for (coef_1,fn_1),(coef_2,fn_2) in top:
    print('\t%.4f\t%-15s\t\t%.4f\t%-15s' % (coef_1,fn_1,coef_2,fn_2))
