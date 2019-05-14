from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
iris = load_iris()
print(iris.data)

print(iris.data[95])

# 建立模型
gnb = GaussianNB()

# 训练
gnb.fit(iris.data,iris.target)

# 预测
print('贝叶斯结果:',gnb.predict([iris.data[95]]))
print(gnb.predict([[4.8, 3.5 , 4.2, 1.2]]))
print('贝叶斯结果:',gnb.predict(iris.data))


# KMeans 聚类
from sklearn.cluster import KMeans

# 配置，构建
est = KMeans(n_clusters = 4)

# 计算
est.fit(iris.data)

# 聚类结果
print('KMeans聚类:',est.labels_)
