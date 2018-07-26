from medicine_similarity.function_cluster_entropy import ClusterEntropy
from medicine_similarity.taste_cluster_various import cluster_various_main
from medicine_similarity.data_utils import get_data
import pickle
import re

medicine_path = 'data/data_labeld_kmodes.csv'    # 药物数据的路径（该药物数据已根据性味归经的聚类结果打上标签）
is_cluster = False
function_to_medicine_path = "data/function_to_medicine.pkl"

def cluster():
    """
    对两种聚类算法进行整合
    :return:
    """
    cluster_various_main()  # 利用kmodes针对性味归经的聚类结果，将聚类结果作为标签输出到原药物数据中
    cluster_entropy = ClusterEntropy()  # 初始化复杂系统熵聚类
    function_to_medicine = cluster_entropy.cluster_entropy_main()   # 基于上一次的聚类结果，获取利用复杂系统熵、基于功效团的聚类结果
    return function_to_medicine


def search_relatives(function_to_medicine, medicine_index):
    """
    基于聚类结果寻找药物的相似药物
    :param function_to_medicine:基于功效团的聚类结果
    :param medicine_index:需要寻找相似药物的目标药物所在索引
    :return:
    """
    relatives_list = []  # 用于保存相似药物的列表
    data, series = get_data(medicine_path)  # data为完整药物数据，series为功效数据
    medicine_label = data["Label"].loc[medicine_index]  # 获取目标药物在性味归经聚类结果中的标签
    function_list = re.split("、|；", data["Function"].loc[medicine_index])   # 获取目标药物的功效列表
    function_set = set(function_list)
    print("function_set:", function_set)
    for group in function_to_medicine.keys():   # 遍历字典中的功效团
        # 若功效团是目标药物功效的子集或者目标药物功效是功效团的子集，则认为该药物属于该功效团，与该功效图案中的药物有相似的可能性
        if set(group).issubset(function_set) or function_set.issubset(set(group)):
            medicine_list = function_to_medicine[tuple(group)]  # 获取属于该功效团的药物列表
            # print("medicine_list:", medicine_list)
            # 遍历属于功效团的药物列表，若基于性味归经的聚类结果的标签相同，则认为目标药物和该药物相似
            for i in medicine_list:
                if data["Label"].loc[i] == medicine_label:
                    relatives_list.append(i)
    print("relatives_list:", relatives_list)

if __name__ == "__main__":
    if is_cluster:  # 若需要进行聚类
        function_to_medicine = cluster()
        with open(function_to_medicine_path, "wb") as f:
            pickle.dump(function_to_medicine, f)    # 将聚类结果保存

    else:   # 若需要进行相似药物寻找
        with open(function_to_medicine_path, 'rb') as f:
            function_to_medicine = pickle.load(f)   # 加载聚类结果
        print("function_to_medicine:", function_to_medicine)
        medicine_index = 62  # 需要寻找的药物在总药物数据中的索引
        search_relatives(function_to_medicine, medicine_index)  # 寻找药物的相似药物
