s = "123我，456你"
import re

s = re.sub('，', ' ',s)
s = re.sub('我', ' ' , s)
s = re.sub()
s = re.split('\s+', s)
print(s)
print(type(s))