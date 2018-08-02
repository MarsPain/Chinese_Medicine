import pandas as pd
import numpy as np

# 寻找两个元祖的交集大小，查看一个元祖被包括于另一个元祖
# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 4, 5, 6, 7]
# s1 = set(l1)
# s2 = set(l2)
# inter = s1 & s2
# print("inter:", type(inter))
#
# l3 = [1, 2, 3, 4, 5, 6, 7, 8]
# s3 = set(l3)
# if s1.issubset(s3):
#     print("YES!!!!")

# dict = {"1":[1, 2, 3]}
# print()

# data = pd.DataFrame(columns=["test1", "test2"])
# data["test1"].loc[0] = 0
# print(data)

# data = pd.DataFrame(np.zeros((2, 3)), columns=["a", "b", "c"])
# data["b"].loc[1] = 1
# print(type(data), data)
# data_new = pd.concat([data["a"], data["b"]], axis=1)
# print(type(data_new), data_new)
# data_new.to_csv()   # 为何拼接而成的DataFrame无法调用to_csv函数，与普通的DataFrame有什么区别
