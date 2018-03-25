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

import jieba.posseg as pseg
words = pseg.cut("祛")
for i in words:
    print(i.word, i.flag)
    print(type(i.flag))

# s = "祛风寒"
# for i in s:
#     print(i)
#
# l1 = ['我', '是']
# l2 = ['我', '是']
# print(l1 == l2)