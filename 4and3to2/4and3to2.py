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

        for j in range(length2):
            if len(listFunction[j]) == 3:
                word= word_cut_3(set3, listFunction[j])
                listFunction[j] = word

        for j in range(length2):
            if len(listFunction[j]) == 4:
                word = word_cut_4(set2, set3, set4, listFunction[j])
                listFunction[j] = word

    # print("需要人工处理的3字词")
    # for i in set3:
    #     print(i)
    # print("需要人工处理的4字词")
    # for i in set4:
    #     print(i)

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
    #判断3字词中每个字的词性
    for s in word:
        #每个word_jieba是一个生成器，包含单字及其词性
        word_jieba = pseg.cut(s)
        for w in word_jieba:
            word_list.append(w.word)
            char_list.append(w.flag)
    # print(char_list)
    #根据三字词中每个字的词性进行进一步处理
    if char_list == ['v', 'n', 'n']:
        # print(word_list)
        word1 = '%s%s' % (word_list[0], word_list[1])
        word2 = '%s%s' % (word_list[0], word_list[2])
        word = '%s%s' % (word1, word2)
        return word
    else:
        set3.add(word)
        return word

def word_cut_4(set2, set3, set4, word):
    set4 = set()
    #与set2中的2字词进行对比并处理
    #按照长度2进行分割
    word_list = re.findall('.{2}', word)
    set_temp = set(word_list)
    # print(set2)
    temp = set2.isdisjoint(set_temp)
    # print(temp)
    if temp:
        set4.add(word_list[0])
        set4.add(word_list[1])
        word = '%s%s' % (word_list[0], word_list[1])
        return word
    else:
        #与set3中的3字词进行对比并处理
        for word_3 in set3:
            dis = difflib_leven(word_3, word)
            if dis == 1:
                word = word_cut_3(set3, word_3)
                return word
            else:
                set4.add(word)
                return word


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