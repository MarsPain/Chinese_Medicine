import pandas as pd
import re
import jieba.posseg as pseg

def get_data():
    data = pd.read_csv("data_treat.csv")
    # print(data.info())
    length = data.shape[0]
    # print(length)

    for i in range(length):
        data["Taste"].loc[i] = re.split("、", data["Taste"].loc[i])
        data["Type"].loc[i] = re.split("、", data["Type"].loc[i])
        data["Function"].loc[i] = re.split("、", data["Function"].loc[i])
        data["Effect"].loc[i] = re.split("、", data["Effect"].loc[i])

    return data, length

class word_to_vector:
    def __init__(self, data, length):
        self.data = data
        self.length = length

    #计算各特征的最大数量
    def max_length(self, str):
        max_length = 0
        for i in range(self.length):
            if len(data[str].loc[i]) > max_length:
                max_length = len(data[str].loc[i])
        # print(max_length)
        return max_length

    # 各特征数量补全
    def length_to_max(self, str):
        max_length = self.max_length(str)
        for i in range(self.length):
            while len(data[str].loc[i]) < max_length:
                data[str].loc[i].append(None)
        # print(data[str])

if __name__ == "__main__":
    data, length = get_data()
    word_to_vector = word_to_vector(data, length)
    word_to_vector.length_to_max("Taste")