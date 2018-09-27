# -*- coding: utf-8 -*-
import os

def write_tag(path,char_list,tag_list):
    with open(path, 'w', encoding='utf8') as file:
        for i,char in enumerate(char_list):
            if(tag_list[i]==[]):
                tag_list[i].append('O')
            if(char=='\n'):
                file.write('\t' + 'O' + '\n')
            else:
                file.write(char+'\t'+'\t'.join(tag_list[i])+'\n')
def ent():
    lists = os.listdir('prescription_need_token_t')
    name_list=['treat','pattern','diseases','symptom']
    for fi in lists:
        print(fi)
        line_list = []
        with open('prescription_need_token_t/'+fi,'r',encoding='utf8') as f:
            obj_list = []
            obj = {}
            str_list = f.readlines()
            for index,line in enumerate(str_list):
                row_list = line.strip().split()
                print(row_list)
                if(len(row_list)<2):
                    continue
                word = row_list[0]
                tag = row_list[1]
                if(tag.startswith('S')):
                    obj = dict()
                    obj['C']=word
                    obj['S']=index
                    obj['E']=index+1
                    obj['T']=tag.split('-')[1]
                    obj_list.append(obj)
                elif (tag.startswith('B')):
                    obj = dict()
                    obj['C']=word
                    obj['S']=index
                    obj['T']=tag.split('-')[1]
                elif (tag.startswith('I')):
                    obj['C']=obj['C']+word
                elif (tag.startswith('E')):
                    obj['C']=obj['C']+word
                    obj['E']=index+1
                    obj_list.append(obj)
        #obj_list写入
        with open('prescription_need_token_e/' + fi+'.ent', 'w', encoding='utf8') as f:
            for obj in obj_list:
                line = 'C='+obj['C']+' P='+ str(obj['S'])+':'+ str(obj['E'])+' T='+name_list[int(obj['T'])]+' L=null\n'
                f.write(line)


    pass
if __name__ == '__main__':
    lists = os.listdir('data_all')  # 列出文件夹下所有的目录与文件
    dic_list = []
    tags = []
    name_list=['diseases','pattern','treat','symptom']
    for i in [0,1,2,3]: #0：symptom,1:disease,2:pattern,3:treat
        with open('dic_all/'+name_list[i] + '_all.txt', 'r', encoding='utf8') as file_0:
            dic_0 = file_0.readlines()
            dic_0 = [item.strip('\n') for item in dic_0]
            dic_0 = sorted(dic_0,key=len,reverse=True)
            dic_list.append(dic_0)
        tags.append('B-'+str(i))
        tags.append('E-' + str(i))
        tags.append('I-' + str(i))
        tags.append('S-' + str(i))

    for num in range(1, 113):
        fi = str(num) + ".txt"
        print(fi)
        with open('data_all/'+fi,'r',encoding='utf8') as f:
            file_str = f.read()
            #测试是否有回车
            # o = tt.find('\n')
            # if(o!=-1):
            #     print(fi)
            char_list = list(file_str)
            tag_list = [[]for i in range(len(char_list))]
            for dic_num,dic in enumerate(dic_list):
                for word in dic:
                    start = 0
                    first = 1
                    word_len = len(word)
                    while(True):
                        if(first):
                            start = file_str.find(word)
                            first = 0
                        else:
                            start = file_str.find(word, start+word_len)
                        # if(start>-1):
                        #     print(fi)
                        #     print(word)
                        if(start==-1):
                            # print("YES!!!!!!!!")
                            break
                        #检查是否有本词典的其他标记
                        flag=0
                        for i in range(word_len):
                            for j in tag_list[start+i]:
                                if(j in tags):
                                    flag=1
                        if(flag):
                            break
                        if(word_len==1):
                            tag_list[start].append('S-' + str(dic_num))
                            break
                        tag_list[start].append('B-'+str(dic_num))
                        tag_list[start+word_len-1].append('E-'+str(dic_num))
                        if(word_len>2):
                            for i in range(1,word_len-1):
                                tag_list[start+i].append('I-'+str(dic_num))
        write_tag('token/'+fi,char_list,tag_list)
    # ent()