#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: cq

'''
基于文件完成敏感词替换
'''

class Input(object):
#class def  init的执行策略
    def __init__(self):
        #定义list存储待过滤字符串
        self.filtered_words = list()
        self.in_string = ''
        self.out_string = '--------'
        #py中调用函数时,传参和函数实际参数之间的关系?
        self.load_filtered_words()

    def load_filtered_words(self, filename='filtered_words.txt'):
        with open(filename, 'r', encoding='utf8') as file:
            for line in file.readlines():
                #strip 剥离
                #list中添加元素
                self.filtered_words.append(line.strip())

    def filter_words(self):
        for word in self.filtered_words:
            #输入字符串在list中存在
            if self.in_string.find(word) != -1:
                self.out_string = '******'
                return
            else:
                #编码字符串防止 乱码?
                self.out_string =self.in_string


    def user_input(self):
        #交互显示: >
        self.in_string = input('>')

    def std_output(self):
        self.filter_words()
        print(self.out_string)

if __name__ == '__main__':
    #标准输入
    i = Input()
    i.user_input()
    i.std_output()
