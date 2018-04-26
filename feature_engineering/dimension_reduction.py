import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def get_data():
    data = pd.read_csv("feature_vector.csv")
    print(data.info())
    # print(data)
    length = data.shape[0]
    data = np.array(data)
    feature_vector_list = data[:, 1:]   #用切片获取所有样本的特征向量并从每个特征向量的第二个特征值开始截取
    # print(feature_vector_list)
    # print(feature_vector_list.shape[0], feature_vector_list.shape[1])

    return feature_vector_list

def pca(feature_vector_list):
    pass

if __name__ == "__main__":
    feature_vector_list = get_data()