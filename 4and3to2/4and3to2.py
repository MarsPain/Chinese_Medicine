import pandas as pd
import csv
import numpy as np
import re

data = pd.read_csv("data_init.csv", delimiter="\t")    #用\t而不是,做分隔符
length = data.shape[0]
data.insert(2, "Usage", None)

#对性味部分数据进行处理
for i in range(length):
    L = data["Taste"].loc[i].split("。")
    data["Taste"].loc[i] = re.split("[，、]", L[0])
    data["Usage"].loc[i] = re.split("[，、]", L[1])
# print(data)
data.to_csv("data_treat.csv")