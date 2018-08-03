import pandas as pd
import os
import re

# 删除标注数据中的词性
# path = "data/effect_data_all/combine_sentence_annotation_test.txt"
# path_new = "data/effect_data_all_new/combine_sentence_annotation_test.txt"
# with open(path, "r", encoding="utf-8") as f:
#     string_new = ""
#     for line in f.readlines():
#         word_list = re.split("    ", line)
#         # print(word_list)
#         if len(line.strip()) > 0:
#             string_temp = word_list[0] + "\t" + word_list[-1]
#             string_new = string_new + string_temp
#         else:
#             string_new += "\n"
#     # print(string_new)
#     with open(path_new, "w", encoding="utf-8") as f_new:
#         f_new.write(string_new)
#         with open(path_new, "a", encoding="utf-8") as f_new:
#             f_new.write(word_list[0] + "\t" + word_list[-1])

# 删除标注数据中对空白字符进行O标注的行
path = "data/function_all_token/5000.train"
path_new = "data/function_all_token_new/5000.train"
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

# 对公司提供的《方剂数据集-妇科》中的主治信息进行提取并等量划分
# path_source = "data/方剂数据集-妇科.csv"
# path_target = "data/prescription_need_token"
# with open(path_source, "r", encoding="utf-8") as f_source:
#     data = pd.read_csv(f_source)
#     # print(data["主治"])
#     len_data = data.shape[0]
#     print(len_data)
#     string = ""
#     for i in range(len_data):
#         string += data["主治"].loc[i] + "\n"
#         if i != 0 and i % 100 == 0:
#             # print(i, i//100, string)
#             file = os.path.join(path_target, str(i//100) + ".txt")
#             with open(file, "w", encoding="utf-8") as f_target:
#                 f_target.write(string)
#                 string = ""
#         if i == len_data - 1:
#             file = os.path.join(path_target, str((i//100)+1) + ".txt")
#             with open(file, "w", encoding="utf-8") as f_target:
#                 f_target.write(string)
#                 string = ""

# 将被标注了实体的单个txt文件整合为不同大小的训练集
# path_source = "data/token"
# path_target = "data/function_all_token"
# data_size = [30, 50, 70, 100]
# for size in data_size:
#     path_data = os.path.join(path_target, str(size)+"00.train")
#     string = ""
#     for i in range(1, size+1):
#         path_temp = os.path.join(path_source, str(i)+".txt")
#         with open(path_temp, "r", encoding="utf-8") as f_temp:
#             string_temp = f_temp.read()
#         string += string_temp
#     # print(string)
#     with open(path_data, "w", encoding="utf-8") as f:
#         f.write(string)
#
# path_test_data = os.path.join(path, "test.txt")
# string_test = ""
# for i in range(101, 113):
#     path_test_temp = os.path.join(path, str(i)+".txt")
#     with open(path_test_temp, "r", encoding="utf-8") as f_temp:
#         string_test_temp = f_temp.read()
#     string_test += string_test_temp
#     with open(path_test_data, "w", encoding="utf-8") as f:
#         f.write(string_test)
