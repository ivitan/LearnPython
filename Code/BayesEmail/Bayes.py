from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
iris = datasets.load_iris()

gnb = GaussianNB()
pred = gnb.fit(iris.data,iris.target)
y_pred = pred.predict(iris.data)

print(iris.data.shape[0],(iris.target != y_pred).sum())


from sklearn import datasets
from sklearn.naive_bayes import BernoulliNB
iris=datasets.load_iris()

gnb=BernoulliNB()#构造模型

pred=gnb.fit(iris.data,iris.target) #模型训练，拟合
y_pred=gnb.predict(iris.data) #分类预测
print(iris.data.shape[0],(iris.target!=y_pred).sum())


from sklearn import datasets
from sklearn.naive_bayes import MultinomialNB
iris = datasets.load_iris()

gnb = MultinomialNB()
pred = gnb.fit(iris.data,iris.target)
y_pred = pred.predict(iris.data)

print(iris.data.shape[0],(iris.target != y_pred).sum())


from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
iris = datasets.load_iris()

gnb = GaussianNB()
scores = cross_val_score(gnb,iris.data,iris.target,cv = 10)
print("Accuracy:%.3f"%scores.mean())

from sklearn import datasets
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()

gnb = MultinomialNB()
scores = cross_val_score(gnb,iris.data,iris.target,cv = 10)
print("Accuracy:%.3f"%scores.mean())

from sklearn import datasets
from sklearn.naive_bayes import BaseDiscreteNB
from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()

gnb = BernoulliNB()
scores = cross_val_score(gnb,iris.data,iris.target,cv = 10)
print("Accuracy:%.3f"%scores.mean())