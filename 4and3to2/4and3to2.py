import pandas as pd
import re
import jieba.posseg as pseg

def get_data():
    data = pd.read_csv("data_init.csv", delimiter="\t")    #用\t而不是,做分隔符
    length = data.shape[0]
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

#对功用和主治部分的数据进行分词处理
def word_cut(data, length):
    set2 = set()
    set3 = set()
    set4 = set()

    for i in range(length):
        listFunction = data["Function"].loc[i]
        length2 = len(listFunction)

        #根据词长分别进行处理
        for j in range(length2):
            if len(listFunction[j]) == 2:
                word_cut_2(set2, listFunction[j])

            elif len(listFunction[j]) == 3:
                word_cut_3(set3, listFunction[j])

            elif len(listFunction[j]) == 4:
                word1, word2 = word_cut_4(set4, listFunction[j])
                listFunction[j] = '%s %s' % (word1, word2)

    return data

def word_cut_2(set2, word):
    set_temp = {word}
    temp = set2.isdisjoint(set_temp)
    if temp:
        pass
    else:
        set2.add(word)

def word_cut_3(set3, word):
    #用两个列表记录单字及其词性
    word_list = []
    char_list = []

    for s in word:
        #每个word_jieba是一个生成器，包含单字及其词性
        word_jieba = pseg.cut(s)
        for w in word_jieba:
            word_list.append(w.word)
            char_list.append(w.flag)

    #根据三字词中每个字的词性进行进一步处理
    if char_list == ['v', 'n', 'n']:
        pass
    else:
        set3.add(word)

def word_cut_4(set4, word):
    set4 = set()
    #按照长度2进行分割
    word_list = re.findall('.{2}', word)
    set_temp = set(word_list)
    temp = set4.isdisjoint(set_temp)

    if temp:
        set4.add(word_list[0])
        set4.add(word_list[1])
        return word_list[0], word_list[1]
    else:
        set4.add(word)

#用动态规划对编辑距离进行计算的方法
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

if __name__ == "__main__":
    print("读取数据并进行预处理")
    data, length = get_data()
    print("进行分词处理")
    data = word_cut(data, length)
    data.to_csv("data_treat.csv")