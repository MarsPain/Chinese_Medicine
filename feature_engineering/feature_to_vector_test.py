# import re
# s = ['a', '测试', '测试看看']
# print(len(s))
# for i in range(3):
#     s[i] = re.sub("测", "", s[i])
# print(type(s))
# print(s)

# s = ['a', '测试', '测试看看']
# print(s)
# print(type(s))
# s = str(s)
# print(s)
# print(type(s))

# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)

# import numpy as np
# a = [[1, 2, 3], [1, 2, 3]]
# b = [[4, 5, 6, 7, 8], [4, 5, 6, 7, 8]]
# print("a.shape", np.shape(a))
# print("b.shape", np.shape(b))
# # for i in range(2):
#     # print(np.shape(a[i]), np.shape(b[i]))
# a.extend(b)
# print("a.shape", np.shape(a))

# import numpy as np
# n = np.zeros((4, 1))
# print(n)

# a = np.arange(15).reshape(3, 5)
# b = np.arange(15).reshape(3, 5)
# c = np.append(a, b, axis=1)
# print(c)

# import numpy as np
# s = [1, 2, 3,4]
# b = np.array(s)
# print(1 in s)

# # 无法通过内部函数直接修改变量的值，所以需要用return
# def test(s):
#     s = s + 1
#     print(s)
# s = 1
# test(s)
# print(s)
# #可以通过内部函数直接对列表进行修改
# def test_list(s):
#     s.append(2)
# s = []
# test_list(s)
# print(s)

# for i in range(10):
#     print(i)
#     if i == 5:
#         break

#将数组array转换为DataFrame
# import numpy as np
# import pandas as pd
# s = [[1, 2, 3, 4],
#      [1, 2, 3, 4],
#      [1, 2, 3, 4],
#      [1, 2, 3, 4]]
# s = np.array(s)
# # print(s)
# # print(type(s))
# data = pd.DataFrame(s)
# print(data)

#说明这种报错是由于缺失值
# s = None
# import re
# s = re.split("、", s)
# print(s)