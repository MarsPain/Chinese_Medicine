import numpy as np
from kmodes.kmodes import KModes
import pandas as pd
from sklearn.cluster import KMeans

# 生成随机数据
# data = np.random.choice(20, (100, 10))
# data = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0],
#         [1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],[1,0,0],
#         [0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
# print(data)
# km = KModes(n_clusters=3, init="Huang", n_init=5, verbose=1)
# clusters = km.fit_predict(data)
# print(km.cluster_centroids_)
# kmeans = KMeans(n_clusters=3)
# clusters = kmeans.fit_predict(data)
# print("聚类性能", kmeans.inertia_)
# print("每个样本点所属类别索引", clusters)
# print("簇中心", kmeans.cluster_centers_)
# 中药数据
# data = pd.read_csv("feature_vector.csv")
# data = np.asarray(data)
# data = data[:,1:]
# km = KModes(n_clusters=20, init="Huang", n_init=5, verbose=1)
# clusters = km.fit_predict(data)
# print(km.cluster_centroids_)
# 高维数据可视化
# data = np.random.randint(0, 255, size=[40, 40, 40])
# print("data", data)
# x, y, z = data[0], data[1], data[2]
# print("x", x, "y", y, "z", z)
# ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
# #  将数据点分成三部分画，在颜色上有区分度
# ax.scatter(x, y, z, c='y')  # 绘制数据点，每一个轴坐标可以是同样长度的数组
# ax.set_zlabel('Z')  # 坐标轴
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()
