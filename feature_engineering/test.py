# 测试用sklearn进行特征工程
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Imputer
import numpy as np
iris = load_iris()  #导入数据集
# print(iris.data)  # 特征矩阵
# print(np.shape(iris.data))
# print(iris.target) # 类别label矩阵
# print(StandardScaler().fit_transform(iris.data)) #标准化
# print(Binarizer(threshold=3).fit_transform(iris.data))  #定量二值化

# 将类别型特征转换为one-hot向量
# data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
# # data = ['a', 'c', 'b', 'b', 'b', 'c','a', 'b', 'c']
# values = np.array(data)
# # print(values)
# #将类别性特征值转换为数值型的整数编码
# label_encoder = LabelEncoder()
# integer_encoded = label_encoder.fit_transform(values)
# # print(integer_encoded)    #由首字母决定每个类别具体数值
# # 将整数编码转换为one-hot向量
# onehot_encoder = OneHotEncoder(sparse=False)
# # print(len(integer_encoded))
# #将integer_encoded reshape成len(integer_encoded)行1列的数据
# integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
# # print(integer_encoded)
# onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
# # print(onehot_encoded)
# #将one-hot向量转换回原类别型特征
# inverted = label_encoder.inverse_transform([np.argmax(onehot_encoded[0, :])])
# # print(inverted)

#回到iris数据
#参数sparse=False禁止返回稀疏类型数据，reshape中的-1参数表示根据剩余维度自动计算该维度的数值
# 比如这里就是设定为1列后自动计算有多少行
# print(OneHotEncoder(sparse=False).fit_transform(iris.target.reshape((-1,1))))
# 填补缺失值
# new_data = np.array([1, 1, 1, 1])
# print(np.shape(new_data))
# iris.data = Imputer().fit_transform(np.vstack((new_data, iris.data)))   #np.vstack(（a,b）)，别忘了第二个括号
# print(np.shape(iris.data))

#测试用sklearn进行特征工程——end


