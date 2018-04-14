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

import numpy as np
a = [[1, 2, 3], [4, 5, 6]]
b = [[1, 2, 3], [4, 5, 6]]
print("a.shape", np.shape(a))
print(a, b)
for i in range(2):
    a[i].extend(b[i])
print(a)

# import numpy as np
# n = np.zeros((4, 1))
# print(n)