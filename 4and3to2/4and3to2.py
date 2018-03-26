import pandas as pd
import csv
import numpy as np
import re
import jieba.posseg as pseg


data = pd.read_csv("data_init.csv", delimiter="\t")    #用\t而不是,做分隔符
length = data.shape[0]
data.insert(2, "Usage", None)
data.insert(4, "Effect", None)

#对性味部分数据进行处理，
for i in range(length):
    L = data["Taste"].loc[i].split("。")
    data["Taste"].loc[i] = re.split("[，、]", L[0])
    data["Usage"].loc[i] = re.split("[，、]", L[1])
# print(data)

#对功用主治部分进行处理，仅留下功用部分数据
for i in range(length):
    L = data["Function"].loc[i].split("。")
    data["Function"].loc[i] = re.split("[，、]", L[0])
    data["Effect"].loc[i] = re.split("[，、]", L[1])
    data["Effect"].loc[i] = re.split("[，、]", L[1])

#对功用部分进行分词处理
set2 = set()
set3 = set()
set4 = set()
for i in range(length):
    listFunction = data["Function"].loc[i]
    length2 = len(listFunction)

    for j in range(length2):
        if len(listFunction[j]) == 2:
            set_temp = {listFunction[j]}
            temp = set2.isdisjoint(set_temp)
            if temp:
                pass
            else:
                set2.add(listFunction[j])

        elif len(listFunction[j]) == 3:
            word_list = []
            char_list = []
            for s in listFunction[j]:
                word = pseg.cut(s)
                for w in word:
                    word_list.append(w.word)
                    char_list.append(w.flag)
            # print(char_list)
            if char_list == ['v', 'n', 'n']:
                pass
            else:
                set3.add(listFunction[j])

        elif len(listFunction[j]) == 4:
            words = re.findall('.{2}', listFunction[j])
            set_temp = set(words)
            temp = set4.isdisjoint(set_temp)
            if temp:
                listFunction[j] = '%s %s' % (words[0], words[1])
                set2.add(words[0])
                set2.add(words[1])
            else:
                set4.add(listFunction[j])

#最小编辑距离计算方法
def difflib_leven(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    #创建矩阵
    matrix = [0 for n in range(len_str1 * len_str2)]
    #初始化X轴
    for i in range(len_str1):
      matrix[i] = i
    #初始化Y轴
    for j in range(0, len(matrix), len_str1):
      if j % len_str1 == 0:
          matrix[j] = j // len_str1

    for i in range(1, len_str1):
      for j in range(1, len_str2):
          if str1[i-1] == str2[j-1]:
              cost = 0
          else:
              cost = 1
          matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1+i]+1,
                                      matrix[j*len_str1+(i-1)]+1,
                                      matrix[(j-1)*len_str1+(i-1)] + cost)
    return matrix[-1]

data.to_csv("data_treat.csv")