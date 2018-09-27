import numpy as np
import pandas as pd
import os


# 对字典进行最大正向排序
def sort_dict():
    dir = "dic_all"
    name_list = ['diseases', 'pattern', 'treat', 'symptom']
    for index, name in enumerate(name_list):
        path = os.path.join(dir, name + "_test.txt")
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # print(type(lines))
            # lines.sort(reverse=True, key=lambda x:len(x))
            lines.sort(reverse=True, key=len)
            # print(lines)
        path_new = os.path.join(dir, name + "_test_new.txt")
        with open(path_new, "w", encoding="utf-8") as f:
            f.write("".join(lines))
sort_dict()
