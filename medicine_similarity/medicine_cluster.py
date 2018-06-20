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

def cluster_kmodes():
    data = get_data("../data/feature_vector.csv")
    kmodes = KModes(n_clusters=20, init="Huang", n_init=10, verbose=1)
    clusters = kmodes.fit_predict(data)
    print(clusters) #输出每个样本的类别
    print(kmodes.cluster_centroids_)    #输出聚类结束后的簇中心

def cluster_kmeans():
    data = get_data("../data/feature_vector_pca.csv")
    kmeans = KMeans(n_clusters=20)
    clusters = kmeans.fit_predict(data)
    print(kmeans.inertia_)
    print(clusters)
    print(kmeans.cluster_centers_)

if __name__ == "__main__":
    # cluster_kmodes()
    cluster_kmeans()