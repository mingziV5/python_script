#!/usr/bin/python
#coding:utf-8
import sys
import re
def read_file(file_name):
    word_dict = {}
    with open(file_name) as f:
        counts = 1024
        line = f.read(counts)
        word = ''
        while line:
            line_list = list(word+line)
            flag = 0
            word = ''
            for i in range(len(line_list)):
                if re.match(r'[.\',!?:;\-|\s"]',line_list[i]):
                    if word:
                        word_dict[word] = word_dict.setdefault(word,0) + 1
                        word = ''
                        flag = i
                    else:
                        flag = 1023
                else:
                    word += line_list[i]
            line = f.read(flag+1)
    word_dict_sort = sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    return word_dict_sort[1:20]


if __name__ == '__main__':
    read_file("xxx.txt")
