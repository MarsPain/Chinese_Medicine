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

# s = {"asd":1, "sad":2}
# print(len(s))

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
# s1 = "beauty"
# s2 = "batyu"
# print(difflib_leven(s1, s2))

#测试修改GitHub上项目名后还能不能commit and push

#测试从GitHub上下载项目后还能不能commit and push

# l1 = [1, 2, 3, 5, 6, 7]
# l2 = [2, 3]
# length = len(l1)
# flag = False #保存是否删除过元素的信息
# temp = 0 #保存删除过多少次元素的信息
# for i in range(length):
#     if flag:
#         temp += 1
#         # length -= 1 #不影响迭代次数
#         flag = False
#     i -= temp
#     print("length:",length)
#     print("i:", i)
#     if l1[i] in l2:
#         print(l1[i])
#         l1.remove(l1[i])
#         flag = True
# print(l1)

# for i in range(10):
#     print(i)
#     i = i + 2

# for i in range(10):
#     i -= 1
#     print(i)

#
# L = 10
# flag = True
# for i in range(L):
#     if flag:
#         L = 3
#         flag = False
#     print(i)

# num = [1, 2, 3, 4]
# print(num[:2] + num[3:])
#
# nums1 = [1]
# nums2 = 4
# result = []
# result.append(nums1+nums2)
# print(result)

# s = "cda"
# s = sorted(s)
# print(s)

# s = "asd"
# res = sorted(s) #拆分成字符并重新排序
# print(res)
# res = ''.join(res)  #拼接字符
# print(res)

# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         dict = {}
#         for word in strs:
#             sortedword = "".join(sorted(word))
#             print(sortedword)
#             dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
#         result = []
#         for item in dict:
#             result.append(dict[item])
#         return result
#
# strs = ["eat","tea","tan","ate","nat","bat"]
# solution = Solution()
# result = solution.groupAnagrams(strs)
# print(result)

# s = ['asd']
# s2 = ['fgh']
# s = s + s2
# print(s)

# s = "a"
# s = s * 10
# print(s)

# s = [1, 2, 3, 4, 5, 6]
# for i in range(len(s)-1, -1, -1):
#     print(s[i])

# s = "asd"
# print(s[1])

# n = 4
# m = 2
# print(n // m)

# from keras.layers import Bidirectional

# s = [1, 2, 3]
# print(s)

# import re
# s = "妇人因出血多，心神不安，不得睡"
# s = re.sub("(出血)|神|安", "", s)
# print(s)
# s1 = "as,d;fg.hjk"
# s1 = re.sub(r"s|f|g|;", "", s1)
# print(s1)

# d1 = {"a":1, "b":2}
# d2 = {"c":3, "d":4}
# l = [d1, d2]
# l2 = []
# for dict in l:
#     for key, value in dict.items():
#         l2.append(value)
# print(l2)

import re
#利用字符串拼接创建正则表达式的pattern
# l = ["我", "你"]
# pattern_string = l[0]
# for i in l[1:]:
#     pattern_string = "%s%s%s" % (pattern_string, "|", i)
# # print(pattern_string)
# pattern = re.compile(pattern_string)
# s = "我和你"
# s = re.sub(pattern, "", s)
# print(s)
#说明前后多余的、不影响分割，
# 但依然需要去除前后多余的，不然会分割出多余的空字符，
# 用两种正则表达式+判断末尾是否是“、”进行处理
# s = "、解表、散寒、止痛、"
# l= re.split("、", s)
# print(l)

def a():
    param = 'b'  # 这里就会出现这样的提示，因为在main定义的param对象被重新指定了新的值
    print(param)
if __name__ == '__main__':
    param = 'a'
    a()