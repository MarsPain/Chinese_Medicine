import numpy as np
from kmodes.kmodes import KModes
import pandas as pd

#生成随机数据
# data = np.random.choice(20, (100, 10))
# print(data)
# km = KModes(n_clusters=4, init="Huang", n_init=5, verbose=1)
# clusters = km.fit_predict(data)
# print(km.cluster_centroids_)
#中药数据
# data = pd.read_csv("feature_vector.csv")
# data = np.asarray(data)
# data = data[:,1:]
# km = KModes(n_clusters=20, init="Huang", n_init=5, verbose=1)
# clusters = km.fit_predict(data)
# print(km.cluster_centroids_)
