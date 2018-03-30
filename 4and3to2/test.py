# s = "123我，456你"
# import re
#
# s = re.sub('，', ' ',s)
# s = re.sub('我', ' ' , s)
# s = re.sub()
# s = re.split('\s+', s)
# print(s)
# print(type(s))
#
# s = {1, 2}
# s2 = {1}
# s3 = ["a", "s"]
# s4 = {'a', 's'}
#
# # temp1 = s2.isdisjoint((s))
# # print(temp1)
# # s.add(1)
# # print(s)
# set = set(s3)
# print(type(set))
# print(set)
# print(s4)

# import jieba.posseg as pseg
# words = "祛风湿"
# for i in words:
#     word = pseg.cut(i)
#     for w in word:
#         print(w.word, w.flag)
#         print(type(w.flag))

# s = "祛风寒"
# for i in s:
#     print(i)
#
# l1 = ['我', '是']
# l2 = ['我', '是']
# print(l1 == l2)

# import re
# s = "我，1你23，"
# # s = re.split("[，]", s)
# s = re.sub("，", "", s)
# print(s)

import difflib
# def difflib_leven(str1, str2):
#     len_str1 = len(str1) + 1
#     len_str2 = len(str2) + 1
#     #create matrix
#     matrix = [0 for n in range(len_str1 * len_str2)]
#     #init x axis
#     for i in range(len_str1):
#       matrix[i] = i
#     #init y axis
#     for j in range(0, len(matrix), len_str1):
#       if j % len_str1 == 0:
#           matrix[j] = j // len_str1
#
#     for i in range(1, len_str1):
#       for j in range(1, len_str2):
#           if str1[i-1] == str2[j-1]:
#               cost = 0
#           else:
#               cost = 1
#           matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1+i]+1,
#                                       matrix[j*len_str1+(i-1)]+1,
#                                       matrix[(j-1)*len_str1+(i-1)] + cost)
#     return matrix[-1]
#
# s1 = "补益元气"
# s2 = "补元气"
# distance = difflib_leven(s1, s2)
# print(distance)

# s = {1, 2, 3}
# for i in s:
#     print(i)

# s1 = {'我','和'}
# s2 = 'asd'
# set2 = {s2}
# temp = s1.isdisjoint(set2)
# print(temp)
# print(s2 in s1)

# s1 = {"A":1, "B":2}
# s2 = "C"
# temp = s2 in s1
# # s1['A'] += s1['A']
# # print(s1)
# # s1['C'] = 1
# # print(s1)
# # s1[s2] =3
# # print(s1)
# # s1['D']
# # print(s1)
# s1['E'] = (s1['E'] if 'E' in s1 else 0) + 1
# print(s1)

# import pandas as pd
# s = {"a": 1, "b": 7, "c": 5, "d": 2, "e": 6, "f": 4}
# s = sorted(s.items(), key=lambda item:item[1])
# print(s)
# df = pd.DataFrame(s)
# print(df)

# import re
# s = "我知道或者"
# s = re.sub("我|者", "", s)
# print(s)

# num1 = 15
# num2 = 10
# num1 = (num1 >= num2)
# print(num1)

# num = 2
# num = 2**3
# print(num)

# num = 234
# print(len(str(num)))

# for i in range(10, 0,-1):
#     print(i)

# import pandas as pd
# import jieba.posseg as pseg
# import re
# data = pd.read_csv("rexing1.csv")
# data = data.fillna("missing")
# print(data.info())
# length = data.shape[0]
# print(length)

# s = ["asd", "sdsa"]
# s = str(s)
# print(s)
# s = None
# s = str(s)
# print(s)
# print(len("asd"))

# import pandas as pd
# dict = {'shanghai':{0: [1,2], 1: None},'beijing':{0: [1, 2], 1: [1, 2]}}
# data = pd.DataFrame(dict)
# print(data)
# # print(data.info())
#
# data["shanghai"].loc[0]
#
# for i in range(2):
#     length = len(data["shanghai"].loc[i])
#     print(length)
#
# matrix = [0 for n in range(5 * 5)]
# print(type(matrix))

# def test1(self, n):
#     self.res = []
#     self.test2(n)
#
# def test2(self, n)

s = {"asd":1, "sad":2}
print(len(s))