import numpy as np
from kmodes.kmodes import KModes
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
    # visual_data(data)
    kmodes = KModes(n_clusters=n_clusters, init="Huang", n_init=10, verbose=1)
    clusters = kmodes.fit_predict(data)
    # print("每个样本点所属类别索引", clusters) #输出每个样本的类别
    # print("簇中心",kmodes.cluster_centroids_)    #输出聚类结束后的簇中心

#kmeans聚类方法，处理经过PCA处理的特征向量
def cluster_kmeans(n_clusters):
    data = get_data("../data/feature_vector_pca.csv")
    # visual_data(data)
    kmeans = KMeans(n_clusters=n_clusters)
    clusters = kmeans.fit_predict(data)
    # print("聚类性能", kmeans.inertia_)
    # print("每个样本点所属类别索引", clusters)
    # print("簇中心", kmeans.cluster_centers_)
    visual_cluster(n_clusters, data, clusters)

def visual_data(data):
    length = len(data[0])
    # print(type(data))
    x_length, y_length, z_length = length//3, 2*(length//3), 3*(length//3)
    #各个轴可以是同样长度的数组，不必须是单一的数值，尚不清楚数组如何转换为指定坐标的值
    x, y, z = data[:, :x_length], data[:, x_length:y_length], data[:, y_length:z_length]
    # print(x, y, z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, marker="o", c="y")  #如果要进行3D绘图，要用ax调用scatter才行
    plt.show()

#将聚类后的样本分别存入各标签数组中
def clusters_label_class(n_clusters, data, clusters):
    data_labeled_lists = []
    # print(data, clusters)
    length = len(data)
    for i in range(n_clusters):
        data_labeled_lists.append([])
    # print(data_labeled_lists)
    for i in range(length):
        data_labeled_lists[clusters[i]].append(data[i].tolist())
    #列表转数组
    for i in range(n_clusters):
        data_labeled_lists[i] = np.asarray(data_labeled_lists[i])
    data_labeled_lists = np.asarray(data_labeled_lists)
    print(data_labeled_lists)
    #验证是否所有样本均归类
    num_count = 0
    for data_labeled_list in data_labeled_lists:
        for data_labeled in data_labeled_list:
            num_count += 1
    # print("Yes!" if num_count==length else "Error!")
    return data_labeled_lists

def visual_cluster(n_clusters, data, clusters):
    data_labeled_lists = clusters_label_class(n_clusters, data, clusters)
    length = len(data[0])
    x_length, y_length, z_length = length//3, 2*(length//3), 3*(length//3)
    colors = ['b','g','r','k','c','m','y','#e24fff','#524C90','#845868']
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(n_clusters):
        x, y, z = data_labeled_lists[i][:, :x_length], data_labeled_lists[i][:, x_length:y_length], \
                  data_labeled_lists[i][:, y_length:z_length]
        # print(x, y, z)
        ax.scatter(x, y, z, marker="o", c=colors[i])
    plt.show()

if __name__ == "__main__":
    n_clusters = 10
    # cluster_kmodes(n_clusters)
    cluster_kmeans(n_clusters)