import pandas as pd
import os

# 删除标注数据中的词性
# path = "effect_data_all/combine_sentence_annotation_test.txt"
# path_new = "effect_data_all_new/combine_sentence_annotation_test.txt"
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
# path = "effect_all/test.test"
# path_new = "effect_all_new/test.test"
# with open(path, "r", encoding="utf-8") as f:
#     for line in f.readlines():
#         # print(line)
#         word_list = re.split("\t", line)
#         # print(word_list)
#         if word_list[0] != "":
#             with open(path_new, "a", encoding="utf-8") as f_new:
#                 f_new.write(line)

# 对公司提供的《方剂数据集-妇科》中的主治信息进行提取并等量划分
path_source = "方剂数据集-妇科.csv"
path_target = "prescription_need_token"
with open(path_source, "r", encoding="utf-8") as f_source:
    data = pd.read_csv(f_source)
    # print(data["主治"])
    len_data = data.shape[0]
    print(len_data)
    string = ""
    for i in range(len_data):
        string += data["主治"].loc[i] + "\n"
        if i != 0 and i % 100 == 0:
            # print(i, i//100, string)
            file = os.path.join(path_target, str(i//100) + ".txt")
            with open(file, "w", encoding="utf-8") as f_target:
                f_target.write(string)
                string = ""
        if i == len_data - 1:
            file = os.path.join(path_target, str((i//100)+1) + ".txt")
            with open(file, "w", encoding="utf-8") as f_target:
                f_target.write(string)
                string = ""
