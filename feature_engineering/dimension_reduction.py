import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

def get_data():
    data = pd.read_csv("feature_vector.csv")
    print(data.info())
    # print(data)
    length = data.shape[0]
    data = np.array(data)
    feature_vector_array = data[:, 1:]   #用切片获取所有样本的特征向量并从每个特征向量的第二个特征值开始截取
    # print(feature_vector_list)
    # print(feature_vector_list.shape[0], feature_vector_list.shape[1])

    return feature_vector_array

def pca(feature_vector_array):
    feature_vector_array = feature_vector_array
    # print(feature_vector_list.shape)

    pca = PCA(n_components=0.95)    #指定降维后的主成分方差和的比例
    feature_vector_array_reduction = pca.fit_transform(feature_vector_array)    #拟合并转换
    # print(pca.explained_variance_ratio_)    #各主成分的方差值，越大越是重要的主成分
    # print(pca.explained_variance_)
    print(pca.n_components_)    #降维后剩下的维度
    # print(feature_vector_array_reduction.shape)

    return feature_vector_array_reduction

    #将得到的特征向量矩阵转换成pandas的DataFrame格式并导出到CSV文件
def data_to_pandas(data):
    data = pd.DataFrame(data)
    # print(data)
    data.to_csv("feature_vector_pca.csv")

if __name__ == "__main__":
    feature_vector_list = get_data()
    feature_vector_array_reduction = pca(feature_vector_list)
    data_to_pandas(feature_vector_array_reduction)