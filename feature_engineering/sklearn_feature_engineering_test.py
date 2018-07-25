# 测试用sklearn进行特征工程
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Imputer
from sklearn.feature_selection import VarianceThreshold
import numpy as np
iris = load_iris()  # 导入数据集
# print("iris.data:", iris.data)  # 特征矩阵
# print(np.shape(iris.data))
# print(iris.target) # 类别label矩阵
# print("标准化：", StandardScaler().fit_transform(iris.data)) #标准化
# print("定量二值化：", Binarizer(threshold=3).fit_transform(iris.data))  #定量二值化

# 将类别型特征转换为one-hot向量
# data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'cold', 'warm', 'warm', 'hot']
data = ['冷', '冷', '温', '哦', '热', '热', '冷', '温', '温', '热']
# data = [['cold', 'cold', 'warm'], ['cold', 'hot', 'hot'], ['cold', 'warm', 'hot']]
# data = ['a', 'c', 'b', 'b', 'b', 'c','a', 'b', 'c']
# values = np.array(data)
# print(values)
# 将类别性特征值转换为数值型的整数编码
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(data)
# print(integer_encoded)    #由首字母决定每个类别具体数值
# 将整数编码转换为one-hot向量
onehot_encoder = OneHotEncoder(sparse=False)
# print(len(integer_encoded))
# 将integer_encoded reshape成len(integer_encoded)行1列的数据
integer_encoded = integer_encoded.reshape(-1, 1)
# print(integer_encoded)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
print(onehot_encoded)
# onehot_encoder.fit(integer_encoded)
# print(onehot_encoder.transform([[0, 1]]))
# #将one-hot向量转换回原类别型特征
# inverted = label_encoder.inverse_transform([np.argmax(onehot_encoded[0, :])])
# print(inverted)

# 测试将数组转成one-hot（数组排序和不排序两种情况）
# integer_encoded = integer_encoded.reshape(-1, 2)
# new_integer_encoded = []
# for i in integer_encoded:
#     # print(i)
#     j = sorted(i)
#     # print(j)
#     new_integer_encoded.append(j)
# print(integer_encoded)
# print(new_integer_encoded)
# onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
# print(onehot_encoded)
# onehot_encoded = onehot_encoder.fit_transform(new_integer_encoded)
# print(onehot_encoded)
# print(onehot_encoder.transform([[2, 2]]))
# 本段测试的结论：当特征类别的序列不重要的时候，将整数编码进行排序，以免多余的特征维度

# 将fit和transform拆开
# onehot_encoder.fit([[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]])
# print(onehot_encoder.transform([[0, 1, 3]]))

# 回到iris数据
# 参数sparse=False禁止返回稀疏类型数据，reshape中的-1参数表示根据剩余维度自动计算该维度的数值
# 比如这里就是设定为1列后自动计算有多少行
# one_hot = OneHotEncoder(sparse=False).fit_transform(iris.target.reshape((-1,1)))
# print(one_hot)
# print(np.shape(one_hot))
# 填补缺失值
# new_data = np.array([1, 1, 1, 1])
# print(np.shape(new_data))
# iris.data = Imputer().fit_transform(np.vstack((new_data, iris.data)))   #np.vstack(（a,b）)，别忘了第二个括号
# print(np.shape(iris.data))

# 特征选择
# print("方差选择法：", VarianceThreshold(threshold=3).fit_transform(iris.data)) #方差选择法

# 测试用sklearn进行特征工程——end


