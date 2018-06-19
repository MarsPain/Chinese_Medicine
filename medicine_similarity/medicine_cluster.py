import numpy as np
from kmodes.kmodes import KModes
import pandas as pd
import numpy as np

def get_data():
    data = pd.read_csv("feature_vector.csv")
    # print(data.info())
    # print(data)
    data = np.asarray(data) #dataframe转array
    data = data[:,1:]
    print(data, data.shape)
    return data

def cluster_kmodes():
    data = get_data()
    km = KModes(n_clusters=20, init="Huang", n_init=10, verbose=1)
    clusters = km.fit_predict(data)
    print(clusters) #输出每个样本的类别
    print(km.cluster_centroids_)    #输出聚类结束后的簇中心

if __name__ == "__main__":
    cluster_kmodes()