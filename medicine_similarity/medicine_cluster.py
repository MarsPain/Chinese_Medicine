import numpy as np
from kmodes.kmodes import KModes
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

def get_data(filename):
    data = pd.read_csv(filename)
    # print(data.info())
    # print(data)
    data = np.asarray(data) #dataframe转array
    data = data[:,1:]
    # print(data, data.shape)
    return data

#kmodes聚类方法，处理离散的one-hot特征向量
def cluster_kmodes(n_clusters):
    data = get_data("../data/feature_vector.csv")
    kmodes = KModes(n_clusters=n_clusters, init="Huang", n_init=10, verbose=1)
    clusters = kmodes.fit_predict(data)
    print("每个样本点所属类别索引", clusters) #输出每个样本的类别
    print("簇中心",kmodes.cluster_centroids_)    #输出聚类结束后的簇中心

#kmeans聚类方法，处理经过PCA处理的特征向量
def cluster_kmeans(n_clusters):
    data = get_data("../data/feature_vector_pca.csv")
    kmeans = KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(data)
    print("聚类性能", kmeans.inertia_)
    print("每个样本点所属类别索引", clusters)
    print("簇中心", kmeans.cluster_centers_)

if __name__ == "__main__":
    n_clusters = 10
    # cluster_kmodes(n_clusters)
    cluster_kmeans(n_clusters)