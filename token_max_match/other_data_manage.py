import numpy as np
import pandas as pd
import os
import re


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
# sort_dict()

# 将被标注了实体的单个txt文件整合为不同大小的训练集
def concat():
    path_source = "token"
    path_target = "function_all_token"
    data_size = [70]
    for size in data_size:
        path_data = os.path.join(path_target, str(size)+"00.train")
        string = ""
        for i in range(1, size+1):
            path_temp = os.path.join(path_source, str(i)+".txt")
            with open(path_temp, "r", encoding="utf-8") as f_temp:
                string_temp = f_temp.read()
            string += string_temp
        # print(string)
        with open(path_data, "w", encoding="utf-8") as f:
            f.write(string)
    path_test_data = os.path.join(path_target, "dev.dev")
    string_test = ""
    for i in range(71, 113):
        path_test_temp = os.path.join(path_source, str(i)+".txt")
        with open(path_test_temp, "r", encoding="utf-8") as f_temp:
            string_test_temp = f_temp.read()
        string_test += string_test_temp
        with open(path_test_data, "w", encoding="utf-8") as f:
            f.write(string_test)
concat()

# 删除标注数据中对空白字符进行O标注的行
def delete_zero():
    path = "function_all_token/7000.train"
    path_new = "function_all_token_new/7000.train"
    with open(path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            # print(line)
            word_list = re.split("\t", line)
            # print(word_list)
            if word_list[0] != "":
                with open(path_new, "a", encoding="utf-8") as f_new:
                    f_new.write(line)
            else:
                with open(path_new, "a", encoding="utf-8") as f_new:
                    f_new.write("\n")
delete_zero()
