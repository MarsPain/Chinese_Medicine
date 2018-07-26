from medicine_similarity.function_cluster_entropy import ClusterEntropy
from medicine_similarity.taste_cluster_various import cluster_various_main


def cluster_main():
    cluster_various_main()  # 利用kmodes针对性味归经的聚类结果
    cluster_entropy = ClusterEntropy()  # 初始化复杂系统熵聚类
    function_to_medicine = cluster_entropy.cluster_entropy_main()   # 获取利用复杂系统熵、基于功效团的聚类结果

if __name__ == "__main__":
    cluster_main()
