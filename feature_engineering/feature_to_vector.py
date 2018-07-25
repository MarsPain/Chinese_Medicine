import pandas as pd
import re
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import numpy as np

file_path = "data_treat.csv"    # 需要进行特征向量化的数据


def get_data(path):
    """
    读取原数据并进行处理
    :param path:
    :return:
    """
    data = pd.read_csv(path)
    print(data.info())
    length = data.shape[0]
    # print(length)
    # print(data)
    for i in range(length):
        data["Taste"].loc[i] = re.split("、", data["Taste"].loc[i])
        data["Type"].loc[i] = re.split("、", data["Type"].loc[i])
        # data["Effect"].loc[i] = re.split("、", data["Effect"].loc[i])
    # print(data)
    return data, length


class FeatureToVectorSeq:
    """
    保留特征序列的向量化方法类,只有方剂的药物组成特征会用到，主要针对药物组成特征的向量化
    """
    def __init__(self, data, length):
        self.data = data
        self.length = length

    def max_length(self, featrue_name):
        """
        计算某特征的最大数量
        :param featrue_name:特征名称
        :return:
        """
        max_length = 0
        for i in range(self.length):
            if len(self.data[featrue_name].loc[i]) > max_length:
                max_length = len(self.data[featrue_name].loc[i])
        # print(max_length)
        return max_length

    def length_to_max(self, featrue_name):
        """
        各特征数量补全
        :param featrue_name:需要进行补全的特征名称
        :return:
        """
        max_length = self.max_length(featrue_name)
        for i in range(self.length):
            while len(self.data[featrue_name].loc[i]) < max_length:
                self.data[featrue_name].loc[i].append("missing")
        # print(data[str])
        return max_length

    def feature_to_vector(self):
        """
        对特征进行向量化
        :return:
        """
        feature_list = ["Taste", "Type", "Effect"]
        label_encoder = LabelEncoder()
        onehot_encoder = OneHotEncoder(sparse=False)
        onehot_encoded_all = []
        for f in feature_list:
            max_length = self.length_to_max(f)  # 将特征补全
            # 将所有药物的相应特征连接在一起，再转换成整数编码
            d = self.data[f].loc[0]
            # print("d:",np.shape(d))
            for i in range(1, self.length):
                d.extend(self.data[f].loc[i])
            # print(d)
            integer_encoded = label_encoder.fit_transform(d)
            # 转换成整数编码后按照max_length reshape成每个药物的特征数组
            integer_encoded = integer_encoded.reshape(-1, max_length)
            onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
            # print(onehot_encoded)
            # print(type(onehot_encoded))
            # print(np.shape(onehot_encoded))
            onehot_encoded_all.append(onehot_encoded)
        print(onehot_encoded_all)
        print(len(onehot_encoded_all))

        # 将多个特征数组拼接在一起
        onehot_encoded_all_joint = onehot_encoded_all[0]
        # print(onehot_encoded_all_joint)
        # print(np.shape(onehot_encoded_all_joint))
        # print(type(onehot_encoded_all_joint))
        for j in range(1, len(onehot_encoded_all)):
            onehot_encoded_all_joint = np.append(onehot_encoded_all_joint, onehot_encoded_all[j], axis=1)
        # print(onehot_encoded_all_joint)
        # print(np.shape(onehot_encoded_all_joint))
        # print(type(onehot_encoded_all_joint))
        return onehot_encoded_all_joint

    @staticmethod
    def data_to_pandas(data):
        """
        将得到的特征向量矩阵转换成pandas的DataFrame格式并导出到CSV文件
        :param data:
        :return:
        """
        data = pd.DataFrame(data)
        # print(data)
        data.to_csv("feature_vector_seq.csv")


class FeatureToVector:
    """
    不保留序列特征的向量化（此方法过于冗余和复杂，已废弃）
    """
    def __init__(self, data, length):
        self.data = data
        self.length = length

    def max_length(self, featrue_name):
        """
        计算各特征的最大数量
        :param featrue_name:特征名
        :return:
        """
        max_length = 0
        for i in range(self.length):
            if len(self.data[featrue_name].loc[i]) > max_length:
                max_length = len(self.data[featrue_name].loc[i])
        # print(max_length)
        return max_length

    def length_to_max(self, featrue_name):
        """
        各特征数量补全
        :param featrue_name:特征名
        :return:
        """
        max_length = self.max_length(featrue_name)
        for i in range(self.length):
            while len(self.data[featrue_name].loc[i]) < max_length:
                self.data[featrue_name].loc[i].append("missing")
        # print(data[str])
        return max_length

    def feature_to_vector(self):
        feature_list = ["Taste", "Type", "Effect"]
        label_encoder = LabelEncoder()
        onehot_encoder = OneHotEncoder(sparse=False)
        onehot_encoded_all = []
        for f in feature_list:
            # 将特征补全
            max_length = self.length_to_max(f)
            # print(max_length)
            # 将所有药物的相应特征连接在一起，再转换成整数编码
            d = self.data[f].loc[0]
            # print("d:",np.shape(d))
            for i in range(1, self.length):
                d.extend(self.data[f].loc[i])
            # print(d)
            integer_encoded = label_encoder.fit_transform(d)
            # 转换成整数编码后再将每个特征转换为one-hot
            integer_encoded = integer_encoded.reshape(-1, 1)
            onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
            # print(onehot_encoded)
            # print(np.shape(onehot_encoded))
            # 将每个样本的单独的one-hot向量整合到一个数组中
            vector_length = np.shape(onehot_encoded[0])
            onehot_encoded_list = []
            onehot_encoded_temp = np.zeros(vector_length)
            temp = 0
            for i in range(len(onehot_encoded)):
                if temp < max_length:
                    index = np.argmax(onehot_encoded[i])
                    onehot_encoded_temp[index] = 1
                    temp += 1
                else:
                    onehot_encoded_list.append(onehot_encoded_temp)
                    onehot_encoded_temp = np.zeros(vector_length)
                    index = np.argmax(onehot_encoded[i])
                    onehot_encoded_temp[index] = 1
                    temp = 1
            # print(onehot_encoded_list)
            # print(len(onehot_encoded_list))
            onehot_encoded_all.append(onehot_encoded_list)

        # 将多个特征数组拼接在一起
        onehot_encoded_all_joint = onehot_encoded_all[0]
        # print(onehot_encoded_all_joint)
        # print(np.shape(onehot_encoded_all_joint))
        for j in range(1, len(onehot_encoded_all)):
            onehot_encoded_all_joint = np.append(onehot_encoded_all_joint, onehot_encoded_all[j], axis=1)
        # print(onehot_encoded_all_joint)
        print(np.shape(onehot_encoded_all_joint))
        return onehot_encoded_all_joint

    def data_to_pandas(self, data):
        """
        将得到的特征向量矩阵转换成pandas的DataFrame格式并导出到CSV文件
        :param data:one-hot特征向量
        :return:
        """
        data = pd.DataFrame(data)
        # print(data)
        data.to_csv("feature_vector.csv")


class FeatureToVector2:
    """
    #特征one-hot向量化（不保留序列特征）：
    """
    def __init__(self, data, length):
        self.data = data
        self.length = length
        self.feature_name = ["Taste", "Type"]

    def feature_to_id(self):
        """
        获取所有样本的所有特征
        :return:
        """
        feature_all = []
        for i in range(self.length):
            for f in self.feature_name:
                feature_all.append(self.data[f][i])
        # print(np.asarray(feature_all).shape)
        # 将所有特征转换为字典，key为特征名，value为出现次数
        feature_dict = {}
        for feature_list in feature_all:
            for f in feature_list:
                feature_dict[f] = feature_dict[f]+1 if f in feature_dict else 0
        # print(feature_dict)
        # 根据特征字典feature_dict创建特征映射字典
        feature_dict_sorted = sorted(feature_dict.items(), key=lambda x: (-x[1], x[0]))  # 根据特征出现频次进行排序
        # print(feature_dict_sorted, len(feature_dict_sorted))
        id_to_feature = {i: v[0] for i, v in enumerate(feature_dict_sorted)}  # id（根据词频排序从0开始）到word的映射字典
        feature_to_id = {v: k for k, v in id_to_feature.items()}  # 反转上一个映射字典，得到word到id的映射字典
        # print(feature_to_id)
        return feature_to_id

    def feature_to_vector(self):
        feature_to_id = self.feature_to_id()
        feature_length = len(feature_to_id)
        # print(feature_length)
        feature_vector = np.zeros((self.length, feature_length))
        # print(feature_to_vector)
        for i in range(self.length):
            for f in self.feature_name:
                for j in self.data[f].loc[i]:
                    # print(j)
                    feature_vector[i][feature_to_id[j]] = 1
        return feature_vector

    def data_to_pandas(self):
        feature_vector = self.feature_to_vector()
        data = pd.DataFrame(feature_vector)
        data.to_csv("../data/feature_vector.csv")

if __name__ == "__main__":
    data_treat, length_treat = get_data(file_path)

    # 保留特征序列的向量化
    # feature_to_vector_seq = FeatureToVectorSeq(data, length)
    # onehot_encoded_all_joint = feature_to_vector_seq.feature_to_vector()
    # feature_to_vector_seq.data_to_pandas(onehot_encoded_all_joint)

    # 不保留特征序列的向量化
    # feature_to_vector = FeatureToVector(data, length)
    # onehot_encoded_all_joint = feature_to_vector.feature_to_vector()
    # feature_to_vector.data_to_pandas(onehot_encoded_all_joint)

    # 特征one-hot向量化（不保留序列特征）
    feature_to_vector_2 = FeatureToVector2(data_treat, length_treat)
    feature_to_vector_2.data_to_pandas()
