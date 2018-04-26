import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets.samples_generator import make_blobs
from sklearn.decomposition import PCA

X, y = make_blobs(n_samples=10000, n_features=3, centers=[[3,3,3], [0,0,0], [1,1,1], [2,2,2]],
                  cluster_std=[0.2, 0.1, 0.2, 0.2],random_state =9)
fig = plt.figure()
ax = Axes3D(fig, rect=[0, 0, 1, 1], elev=30, azim=20)
plt.scatter(X[:, 0], X[:, 1], X[:, 2], marker="o")
plt.show()
#先不降维，对数据进行投影，并查看方差分布
pca = PCA(n_components=3)
pca.fit(X)
print(pca.explained_variance_ratio_)    #各主成分的方差值，越大越是重要的主成分
print(pca.explained_variance_)  #各成分的方差值占总方差值，越大越是重要的主成分
#降维后，再次查看方差分布
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
#对比两次方差分布，三维投影到二维后，放弃了方差值最小的第三维
#降维后再次查看数据分布
X_new = pca.transform(X)
plt.scatter(X_new[:, 0], X_new[:, 1],marker='o')
plt.show() #可以发现降维后的数据依然可以很清楚地看到之前三维图中的4个簇
#指定降维后的主成分方差和的比例
pca = PCA(n_components=0.95)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print(pca.n_components_)    #第一个维度的方差比例高达98%，只选择第一维即可以满足05%的阈值
pca = PCA(n_components=0.99)
pca.fit(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_)
print(pca.n_components_)    #前两个维度的方差比例加起来才达到99%，所以取前两维度
# pca = PCA(n_components='mle')   #让MLE算法自己选择降低维度的方式，但是不知道为何会报错
# pca.fit(X)
# print(pca.explained_variance_ratio_)
# print(pca.explained_variance_)
# print(pca.n_components_)
