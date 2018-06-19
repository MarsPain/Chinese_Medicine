import numpy as np
from kmodes.kmodes import KModes

#生成随机数据
# data = np.random.choice(20, (100, 10))
data = np.random.rand(100, 10)
print(data)
km = KModes(n_clusters=4, init="Huang", n_init=5, verbose=1)
clusters = km.fit_predict(data)
print(km.cluster_centroids_)