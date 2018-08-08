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
# path = "data/function_all_token/5000.train"
# path_new = "data/function_all_token_new/5000.train"
# with open(path, "r", encoding="utf-8") as f:
#     for line in f.readlines():
#         # print(line)
#         word_list = re.split("\t", line)
#         # print(word_list)
#         if word_list[0] != "":
#             with open(path_new, "a", encoding="utf-8") as f_new:
#                 f_new.write(line)
#         else:
#             with open(path_new, "a", encoding="utf-8") as f_new:
#                 f_new.write("\n")

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

# 将对2700个功效词条的标注转移到1800个功效词条中
# path = "data/dict_function/set4_true_dict.txt"
# path_source = "data/dict_function/set4_true_dict_labled_old.txt"
# path_target = "data/dict_function/set4_true_dict_labeld.txt"
# with open(path_source, "r", encoding="utf-8") as f_source:
#     lines = f_source.readlines()
#     # print(lines)
#     label_dict = {}
#     for line in lines:
#         line_list = re.split(" ", line.strip())
#         # print(line_list)
#         label_dict[line_list[0]] = line_list[1]
#     print(label_dict)
# with open(path, "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     string = ""
#     for line in lines:
#         line = line.strip()
#         if line in label_dict:
#             string = string + line + "  " + label_dict[line] + "\n"
#         else:
#             string = string + line + "  " + "\n"
#     print(string)
# with open(path_target, "w", encoding="utf-8") as f_target:
#     f_target.write(string)

# 对原总药物数据集进行分析，主要对性味归经功效特征词的数量以及词频进行统计
# path = "data/data_all_v4.csv"   # 原数据集
# data = pd.read_csv(path)
# print(data.info())
# data = data.fillna("missing")
# print(data.info())
# length = data.shape[0]
# # 分割数据
# for i in range(length):
#     l = data["Taste"].loc[i]
#     data["Taste"].loc[i] = re.split("、", l)
#     l = data["Type"].loc[i]
#     data["Type"].loc[i] = re.split("、", l)
#     data["Function"].loc[i] = re.split("[，、；]", data["Function"].loc[i])
# # 统计数据
# taste_num = 0
# taste_dict = {}
# type_num = 0
# type_dict = {}
# function_num = 0
# function_dict = {}
# for i in range(length):
#     for taste in data["Taste"].loc[i]:
#         # print(taste)
#         taste_num += 1
#         taste_dict[taste] = taste_dict[taste]+1 if taste in taste_dict else 1
#     for type in data["Type"].loc[i]:
#         # print(type)
#         type_num += 1
#         # if len(taste) == 2 or len(taste) == 3 or len(taste) == 4:
#         type_dict[type] = type_dict[type]+1 if type in type_dict else 1
#     for function in data["Function"].loc[i]:
#         # print(function)
#         function_num += 1
#         if len(function) == 2 or len(function) == 3 or len(function) == 4:
#             function_dict[function] = function_dict[function]+1 if function in function_dict else 1
# taste_dict_sorted = sorted(taste_dict.items(), key=lambda x: (-x[1], x[0]))  # 根据特征出现频次进行排序
# type_dict_sorted = sorted(type_dict.items(), key=lambda x: (-x[1], x[0]))
# function_dict_sorted = sorted(function_dict.items(), key=lambda x: (-x[1], x[0]))
# print("taste_dict_sorted:", taste_num, len(taste_dict_sorted), taste_dict_sorted)
# print("type_dict_sorted:", type_num, len(type_dict_sorted), type_dict_sorted)
# print("function_dict_sorted:", function_num, len(function_dict_sorted), function_dict_sorted)

# 对人工标注的分词结果进行统计
# path = "data/dict_function/set4_true_dict_labeld.txt"
# with open(path, "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     true_count, false_count = 0, 0
#     for line in lines:
#         line_list = re.split("  ", line.strip())
#         # print(line_list)
#         if line_list[-1] == "1":
#             true_count += 1
#         else:
#             false_count += 1
# print("true_count:", true_count, "false_count:", false_count, "accuracy:", true_count/(true_count+false_count))

# 对将功效进行分词后的功效词进行统计
# path = "../data/data_treat.csv"   # 将功效进行分词后的数据集
# data = pd.read_csv(path)
# print(data.info())
# data = data.fillna("missing")
# print(data.info())
# length = data.shape[0]
# # 分割数据
# for i in range(length):
#     data["Function"].loc[i] = re.split("[，、；]", data["Function"].loc[i])
# # 统计数据
# function_num = 0
# function_dict = {}
# for i in range(length):
#     for function in data["Function"].loc[i]:
#         # print(function)
#         function_num += 1
#         if len(function) == 2 or len(function) == 3 or len(function) == 4:
#             function_dict[function] = function_dict[function]+1 if function in function_dict else 1
# function_dict_sorted = sorted(function_dict.items(), key=lambda x: (-x[1], x[0]))   # 根据特征出现频次进行排序
# print("function_dict_sorted:", function_num, len(function_dict_sorted), function_dict_sorted)
