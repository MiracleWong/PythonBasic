#!/usr/local/bin/python
#-*- coding: utf-8 -*-

__author__ = "Miracle Wong"

class Fibonacci(object):
    """返回一个Fibonacci数列"""
    def __init__(self):
        self.fList = [0,1] #设置初始数列
        self.main()
    def main(self):
        listLen = raw_input('请输入Fibonacci数列的长度（3-50）：')
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1] + self.fList[-2])
        print('得到的Fibonacci数列为：\n %s ' %self.fList)

    def checkLen(self, lenth):
        lenList = map(str, xrange(3,51))
        if lenth in lenList:
            print('输入的长度符合标准，继续运行')
        else:
            print('只能输入3-50，太长了不是算不出，只是没有必要')
            exit()


if __name__ == '__main__':
    pt = Fibonacci()