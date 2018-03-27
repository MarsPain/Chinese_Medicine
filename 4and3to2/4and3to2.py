import pandas as pd
import re
import jieba.posseg as pseg
import matplotlib.pyplot as plt

def get_data():
    data = pd.read_csv("data_init.csv", delimiter="\t")    #用\t而不是,做分隔符
    length = data.shape[0]
    #插入列，分别保存“归经”和“主治”的数据
    data.insert(2, "Type", None)
    data.insert(4, "Effect", None)

    #对性味部分数据进行处理，分为性味和归经两列
    for i in range(length):
        L = data["Taste"].loc[i].split("。")
        data["Taste"].loc[i] = re.split("[，、]", L[0])
        data["Type"].loc[i] = re.split("[，、]", L[1])

    #对功用主治部分进行处理,分为功用和主治两列
    for i in range(length):
        L = data["Function"].loc[i].split("。")
        data["Function"].loc[i] = re.split("[，、]", L[0])
        data["Effect"].loc[i] = re.split("[，、]", L[1])
        data["Effect"].loc[i] = re.split("[，、]", L[1])

    return data, length

#对功效部分的数据进行分词处理
def word_cut_function(data, length):
    set2 = {}
    #保存可以拆分的3字词
    set3_true = {}
    # 保存不可拆分的3字词
    set3_false = {}
    # 保存可以拆分的4字词
    set4_true = {}
    # 保存不可拆分的4字词
    set4_false = {}

    for i in range(length):
        listFunction = data["Function"].loc[i]
        length2 = len(listFunction)

        #根据词长分别进行处理
        for j in range(length2):
            if len(listFunction[j]) == 2:
                word_cut_2(set2, listFunction[j])

        for j in range(length2):
            if len(listFunction[j]) == 3:
                word= word_cut_3(set2, set3_true, set3_false, listFunction[j])
                listFunction[j] = word

        for j in range(length2):
            if len(listFunction[j]) == 4:
                word = word_cut_4(set2, set3_true, set3_false, set4_true, set4_false, listFunction[j])
                listFunction[j] = word

    return data, set2, set3_true, set3_false, set4_true, set4_false

#对主治部分的数据进行分词处理
# def word_cut_effect(data, length):
#
#     for i in range(length):
#         listFunction = data["Effect"].loc[i]
#         length2 = len(listFunction)
#
#         #根据词长分别进行处理
#         for j in range(length2):
#             if len(listFunction[j]) == 2:
#                 word_cut_2(set2, listFunction[j])
#
#         for j in range(length2):
#             if len(listFunction[j]) == 3:
#                 word= word_cut_3(set2, set3, listFunction[j])
#                 listFunction[j] = word
#
#         for j in range(length2):
#             if len(listFunction[j]) == 4:
#                 word = word_cut_4(set2, set3, set4, listFunction[j])
#                 listFunction[j] = word
#
#     return data, set2, set3, set4

def word_cut_2(set2, word):
    #保存到词库并计数
    set2[word] = (set2[word] if word in set2 else 0) + 1

def word_cut_3(set2, set3_true, set3_false, word):
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
        set3_true[word] = (set3_true[word] if word in set3_true else 0) + 1
        #字符串拼接
        word1 = '%s%s' % (word_list[0], word_list[1])
        word2 = '%s%s' % (word_list[0], word_list[2])
        word = '%s %s' % (word1, word2)
        #词库中词出现次数的计数
        set2[word1] = (set2[word1] if word1 in set2 else 0) + 1
        set2[word2] = (set2[word2] if word2 in set2 else 0) + 1
        return word
    else:
        #无法拆分，先分配到set3_false词库中
        set3_false[word] = (set3_false[word] if word in set3_false else 0) + 1
        return word

def word_cut_4(set2, set3_true, set3_flase, set4_true, set4_false, word):
    #与set2中的2字词进行对比并处理
    #按照长度2进行分割
    word_list = re.findall('.{2}', word)
    temp = False
    for i in word_list:
        if i in set2:
            temp = True
        else:
            pass

    if temp:
        # 若22拆分后的单词在2字词库中出现过
        set4_true[word] = (set4_true[word] if word in set4_true else 0) + 1
        set2[word_list[0]] = (set2[word_list[0]] if word_list[0] in set2 else 0) + 1
        set2[word_list[1]] = (set2[word_list[1]] if word_list[1] in set2 else 0) + 1
        word = '%s %s' % (word_list[0], word_list[1])
        return word
    else:
        #若22拆分后的单词在2字词库中未出现过，则先与set3_true中的3字词进行对比
        for word_3 in set3_true:
            dis = difflib_leven(word_3, word)
            if dis == 1:
                # 若与set3_true中某个3字词只有一个编辑距离
                word = word_cut_3(set2, set3_true, set3_flase, word_3)
                return word
            else:
                set4_false[word] = (set4_false[word] if word in set4_false else 0) + 1
                return word

#用动态规划对字符串间的编辑距离进行计算
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

def data_analyse(set2, set3_true, set3_false, set4_true, set4_false):
    print("==========2字词库==========")
    for i in set2:
        print(i, set2[i])
    print("==========被拆分的3字词库==========")
    for i in set3_true:
        print(i, set3_true[i])
    print("==========未被拆分的3字词库==========")
    for i in set3_false:
        print(i, set3_false[i])
    print("==========被拆分的4字词==========")
    for i in set4_true:
        print(i, set4_true[i])
    print("==========未被拆分的4字词==========")
    for i in set4_false:
        print(i, set4_false[i])

    #各字典按照值的大小进行排序得到相应元祖，然后转换为DataFrame并导出到CSV，最后绘图
    # set2 = sorted(set2.items(), key=lambda item:item[1], reverse = True)
    # df_2 = pd.DataFrame(set2)
    # df_2.to_csv("data_words_2.csv")
    # words_2 = df_2.iloc[0:15]
    # words_2.plot(kind = 'bar')
    # plt.title("words_2")
    # plt.show()

if __name__ == "__main__":
    print("读取数据并进行预处理")
    data, length = get_data()
    print("进行分词处理")
    data, set2, set3_true, set3_false, set4_true, set4_false = word_cut_function(data, length)
    print("结果数据处理")
    data_analyse(set2, set3_true, set3_false, set4_true, set4_false)
    data.to_csv("data_treat.csv")