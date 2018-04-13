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

    return data, length

class word_to_vector:
    def __init__(self, data, length):
        self.data = data
        self.length = length

    #计算各药物的性味特征的最大数量
    def max_length_taste(self):
        self.max_length_taste = 0
        for i in range(self.length):
            if len(data['Taste'].loc[i]) > self.max_length_taste:
                print(i, len(data['Taste'].loc[i]))
                self.max_length_taste = len(data['Taste'].loc[i])
        print(self.max_length_taste)

    #计算各药物的归经特征的最大数量
    def max_length_type(self):
        self.max_length_type = 0
        for i in range(self.length):
            if len(data['Type'].loc[i]) > self.max_length_type:
                print(i, len(data['Type'].loc[i]))
                self.max_length_type = len(data['Type'].loc[i])
        print(self.max_length_type)

if __name__ == "__main__":
    data, length = get_data()
    word_to_vector = word_to_vector(data, length)
    word_to_vector.max_length_taste()
    word_to_vector.max_length_type()