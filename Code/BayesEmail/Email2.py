# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
import csv
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import tree
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier


# 预处理
def preprocessing(text):
    # # text=text.decode("utf-8")
    # tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    # stops = stopwords.words('english')
    # tokens = [token for token in tokens if token not in stops]
    #
    # tokens = [token.lower() for token in tokens if len(token) >= 3]
    # lmtzr = WordNetLemmatizer()
    # tokens = [lmtzr.lemmatize(token) for token in tokens]
    # preprocessed_text = ' '.join(tokens)
    preprocessed_text = text
    return preprocessed_text


# 读取数据集
file_path = r'C:\Users\Administrator\Desktop\SMSSpamCollectionjsn.txt'
sms = open(file_path, 'r', encoding='utf-8')
sms_data = []
sms_label = []
csv_reader = csv.reader(sms, delimiter='\t')
for line in csv_reader:
    sms_label.append(line[0])
    sms_data.append(preprocessing(line[1]))
sms.close()
# print(sms_data)

# 按0.7：0.3比例分为训练集和测试集，再将其向量化
dataset_size = len(sms_data)
trainset_size = int(round(dataset_size * 0.7))
print('dataset_size:', dataset_size, '   trainset_size:', trainset_size)
x_train = np.array([''.join(el) for el in sms_data[0:trainset_size]])
y_train = np.array(sms_label[0:trainset_size])

x_test = np.array(sms_data[trainset_size + 1:dataset_size])
y_test = np.array(sms_label[trainset_size + 1:dataset_size])

vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1, 2), stop_words='english', strip_accents='unicode', norm='l2')

X_train = vectorizer.fit_transform(x_train)
X_test = vectorizer.transform(x_test)

# 朴素贝叶斯分类器
clf = MultinomialNB().fit(X_train, y_train)
y_nb_pred = clf.predict(X_test)

print(y_nb_pred)
print('nb_confusion_matrix:')
cm = confusion_matrix(y_test, y_nb_pred)
print(cm)
print('nb_classification_report:')
cr = classification_report(y_test, y_nb_pred)
print(cr)

feature_names = vectorizer.get_feature_names()
coefs = clf.coef_
intercept = clf.intercept_
coefs_with_fns = sorted(zip(coefs[0], feature_names))
n = 10
top = zip(coefs_with_fns[:n], coefs_with_fns[:-(n + 1):-1])
for (coef_1, fn_1), (coef_2, fn_2) in top:
    print('\t%.4f\t%-15s\t\t%.4f\t%-15s' % (coef_1, fn_1, coef_2, fn_2))

# 决策树
clf = tree.DecisionTreeClassifier().fit(X_train.toarray(), y_train)
y_tree_pred = clf.predict(X_test.toarray())

print('tree_confusion_matrix:')
cm = confusion_matrix(y_test, y_tree_pred)
print(cm)
print('tree_classification_report:')
print(classification_report(y_test, y_tree_pred))

# SGD
clf = SGDClassifier(alpha=0.0001, n_iter=50).fit(X_train, y_train)
y_SGD_pred = clf.predict(X_test)
print('SGD_confusion_matrix:')
cm = confusion_matrix(y_test, y_SGD_pred)
print(cm)
print('SGD_classification_report:')
print(classification_report(y_test, y_SGD_pred))

# svm
clf = LinearSVC().fit(X_train, y_train)
y_svm_pred = clf.predict(X_test)
print('svm_confusion_matrix:')
cm = confusion_matrix(y_test, y_svm_pred)
print(cm)
print('svm_classification_report:')
print(classification_report(y_test, y_svm_pred))

# RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10)
clf.fit(X_train, y_train)
y_RF_pred = clf.predict(X_test)
print('RF_confusion_matrix:')
print(confusion_matrix(y_test, y_RF_pred))
print('RF_classification_report:')
print(classification_report(y_test, y_RF_pred))
