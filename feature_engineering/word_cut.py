import pandas as pd
import re
import jieba.posseg as pseg
import matplotlib.pyplot as plt

#数据预处理
# 示例原始数据是药名、性味+归经、功效+主治，这部分代码根据具体数据进行调整
def get_data():
    #若文件读取错误只要在记事本或者编辑器中打开以utf-8的编码格式重新打开即可
    data = pd.read_csv("data_init.csv", delimiter="\t")    #delimiter指定分隔符，根据数据调整
    length = data.shape[0]
    #插入列，分别保存“归经”和“主治”的数据
    data.insert(2, "Type", None)
    data.insert(4, "Effect", None)

    #对性味部分数据进行处理，分为性味和归经两列并以，、作为分隔符返回列表
    for i in range(length):
        L = data["Taste"].loc[i].split("。")
        data["Taste"].loc[i] = re.split("[，、]", L[0])
        data["Type"].loc[i] = re.split("[，、]", L[1])

    #对功用主治部分进行处理,分为功用和主治两列并以，、作为分隔符返回列表
    for i in range(length):
        L = data["Function"].loc[i].split("。")
        data["Function"].loc[i] = re.split("[，、]", L[0])
        data["Effect"].loc[i] = re.split("[，、]", L[1])

    return data, length

#对性味和归经部分的数据进行清洗
class word_clean:
    def __init__(self, data, length):
        print("对性味和归经部分的数据进行清洗")
        self.data = data
        self.length = length

    def word_clean_taste(self, data, length):
        for i in range(self.length):
            list_taste = data["Taste"].loc[i]
            length2 = len(list_taste)
            for j in range(length2):
                list_taste[j] = re.sub("性|味", "", list_taste[j])
            # print(type(list_taste))
            #列表转为字符串，以便后续利用数据
            s = list_taste[0]
            for j in range(1, length2):
                s = "%s%s%s" % (s, "、", list_taste[j])
            data["Taste"].loc[i] = s

    def word_clean_type(self, data, length):
        for i in range(self.length):
            list_type = data["Type"].loc[i]
            # print(type(list_type))
            length2 = len(list_type)
            for j in range(length2):
                list_type[j] = re.sub("归|经|入", "", list_type[j])
            #列表转为字符串，以便后续利用数据
            s = list_type[0]
            for j in range(1, length2):
                s = "%s%s%s" % (s, "、", list_type[j])
            data["Type"].loc[i] = s

#对功效和主治部分数据进行分词和存储
#建立一个类，便于管理数据
class word_cut:

    #引入语料库并创建词库
    def __init__(self, data, length):
        print("对功效和主治部分数据进行分词和存储")
        print("引入语料库并创建词库")
        self.data = data
        self.length = length
        self.set2 = {}
        #保存可以拆分的3字词
        self.set3_true = {}
        # 保存不可拆分的3字词
        self.set3_false = {}
        # 保存可以拆分的4字词
        self.set4_true = {}
        # 保存不可拆分的4字词
        self.set4_false = {}

    #对功效部分的数据进行分词处理
    def word_cut_function(self):
        print("对功用部分进行分词处理")
        #根据词长分别进行处理
        #先建立2字词库
        for i in range(self.length):
            listFunction = data["Function"].loc[i]
            length2 = len(listFunction)
            for j in range(length2):
                if len(listFunction[j]) == 2:
                    self.word_cut_2(listFunction[j])
            # print(type(listFunction))

        #对3字词进行处理并建立3字词库
        for i in range(self.length):
            listFunction = data["Function"].loc[i]
            length2 = len(listFunction)
            for j in range(length2):
                if len(listFunction[j]) == 3:
                    word= self.word_cut_3(listFunction[j])
                    listFunction[j] = word
            # print(type(listFunction))

        #对4字词进行处理并建立4字词库
        for i in range(self.length):
            listFunction = data["Function"].loc[i]
            length2 = len(listFunction)
            for j in range(length2):
                if len(listFunction[j]) == 4:
                    word = self.word_cut_4(listFunction[j])
                    listFunction[j] = word
            # print(type(listFunction))



        return self.data, self.set2, self.set3_true, self.set3_false, self.set4_true, self.set4_false

    #对主治部分的数据进行分词处理
    def word_cut_effect(self):
        print("对主治部分进行分词处理")
        #根据词长分别进行处理
        #先建立2字词库
        for i in range(self.length):
            listEffect = data["Effect"].loc[i]
            length2 = len(listEffect)
            for j in range(length2):
                #清理“主治、或”等停用词
                listEffect[j] = re.sub("主治|或", "", listEffect[j])
                if len(listEffect[j]) == 2:
                    self.word_cut_2(listEffect[j])

        #对3字词进行处理并建立3字词库
        for i in range(self.length):
            listEffect = data["Effect"].loc[i]
            length2 = len(listEffect)
            for j in range(length2):
                if len(listEffect[j]) == 3:
                    word= self.word_cut_3(listEffect[j])
                    listEffect[j] = word

        #对4字词进行处理并建立4字词库
        for i in range(self.length):
            listEffect = data["Effect"].loc[i]
            length2 = len(listEffect)
            for j in range(length2):
                if len(listEffect[j]) == 4:
                    word = self.word_cut_4(listEffect[j])
                    listEffect[j] = word

    def word_cut_2(self, word):
        #保存到词库并计数
        self.set2[word] = (self.set2[word] if word in self.set2 else 0) + 1

    def word_cut_3(self, word):
        #用两个列表记录单字及其词性
        word_list = []
        char_list = []
        #判断3字词中每个字的词性
        for s in word:
            #每个word_jieba是一个生成器，包含单字及其词性
            word_jieba = pseg.cut(s)
            for w in word_jieba:
                word_list.append(w.word)
                char_list.append(w.flag)
        #根据三字词中每个字的词性进行进一步处理
        if char_list == ['v', 'n', 'n']:
            #若满足“动名名”的规律，则分配到set3_true词库中
            self.set3_true[word] = (self.set3_true[word] if word in self.set3_true else 0) + 1
            #字符串拼接
            word1 = '%s%s' % (word_list[0], word_list[1])
            word2 = '%s%s' % (word_list[0], word_list[2])
            word = '%s%s%s' % (word1, "、", word2)
            #词库中词出现次数的计数
            self.set2[word1] = (self.set2[word1] if word1 in self.set2 else 0) + 1
            self.set2[word2] = (self.set2[word2] if word2 in self.set2 else 0) + 1
            return word
        else:
            #无法拆分，先分配到set3_false词库中
            self.set3_false[word] = (self.set3_false[word] if word in self.set3_false else 0) + 1
            return word

    def word_cut_4(self, word):
        #与set2中的2字词进行对比并处理
        #按照长度2进行分割
        word_list = re.findall('.{2}', word)
        temp = False
        for i in word_list:
            if i in self.set2:
                temp = True
            else:
                pass

        if temp:
            # 若22拆分后的单词在2字词库中出现过
            self.set4_true[word] = (self.set4_true[word] if word in self.set4_true else 0) + 1
            self.set2[word_list[0]] = (self.set2[word_list[0]] if word_list[0] in self.set2 else 0) + 1
            self.set2[word_list[1]] = (self.set2[word_list[1]] if word_list[1] in self.set2 else 0) + 1
            word = '%s%s%s' % (word_list[0], "、", word_list[1])
            # print(word)
            return word
        else:
            #若22拆分后的单词在2字词库中未出现过，则先与set3_true中的3字词进行对比
            for word_3 in self.set3_true:
                dis = self.difflib_leven(word_3, word)
                if dis == 1:
                    # print("true")
                    # 若与set3_true中某个3字词只有一个编辑距离
                    self.word = self.word_cut_3(word_3)
                    # print(word)
                    return word
                else:
                    self.set4_false[word] = (self.set4_false[word] if word in self.set4_false else 0) + 1
                    # print(word)
                return word

    #用动态规划对字符串间的编辑距离进行计算
    def difflib_leven(self, str1 , str2):
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

    #分词后将功效和主治的列表全部转换为字符串，方便后续处理，否则将数据写入csv时，列表会变成字符串，不利于处理
    def list_to_str(self):
        #功效
        for i in range(self.length):
            listFunction = data["Function"].loc[i]
            # print(type(listFunction))
            length2 = len(listFunction)
            # print(length2)
            s = listFunction[0]
            for j in range(1, length2):
                s = "%s%s%s" % (s, "、", listFunction[j])
            data["Function"].loc[i] = s

        #主治
        for i in range(self.length):
            listFunction = data["Effect"].loc[i]
            length2 = len(listFunction)
            s = listFunction[0]
            for j in range(1, length2):
                s = "%s%s%s" % (s, "、", listFunction[j])
            data["Effect"].loc[i] = s

    def data_analyse(self):
        print("结果数据处理")
        # pass
        print("========2字词数量=========：", len(self.set2))
        # for i in self.set2:
        #     print(i, self.set2[i])
        print("========被拆分的3字词数量==========：", len(self.set3_true))
        # for i in self.set3_true:
        #     print(i, self.set3_true[i])
        print("============未被拆分的3字词数量=========：", len(self.set3_false))
        # for i in self.set3_false:
        #     print(i, self.set3_false[i])
        print("=========被拆分的4字词数量============：", len(self.set4_true))
        # for i in self.set4_true:
        #     print(i, self.set4_true[i])
        print("=========未被拆分的4字词数量===========：", len(self.set4_false))
        # for i in self.set4_false:
        #     print(i, self.set4_false[i])

        #各字典按照值的大小进行排序得到相应元祖，然后转换为DataFrame并导出到CSV，最后绘图
        # self.set2 = sorted(self.set2.items(), key=lambda item:item[1], reverse = True)
        # df_2 = pd.DataFrame(self.set2)
        # df_2.to_csv("data_words_2.csv")
        # words_2 = df_2.iloc[0:15]
        # words_2.plot(kind = 'bar')
        # plt.title("words_2")
        # plt.show()

if __name__ == "__main__":
    # 读取数据并进行预处理
    data, length = get_data()
    # data.to_csv("data_treat.csv", encoding="utf-8")

    #创建数据清理类
    word_clean = word_clean(data,length)
    #对性味和归经部分的数据进行清洗
    word_clean.word_clean_taste(data, length)
    word_clean.word_clean_type(data, length)

    # 创建分词类
    word_cut = word_cut(data, length)
    # 对功用部分进行分词处理
    word_cut.word_cut_function()
    # 对主治部分进行分词处理
    word_cut.word_cut_effect()
    # 重复对功效和主治部分进行分词处理，使词库完整
    word_cut.word_cut_function()
    word_cut.word_cut_effect()
    #列表转为字符串
    word_cut.list_to_str()

    # 结果数据处理
    word_cut.data_analyse()
    # 结果导出
    data.to_csv("data_treat.csv", encoding="utf-8")