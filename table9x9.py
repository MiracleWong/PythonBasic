#!/usr/local/bin/python
# -*- coding: utf-8 -*-

__author__ = "MiracleWong"


class PrintTable(object):

    """开始打印9X9的乘法表"""

    def __init__(self):
        print('开始打印9X9的乘法表')
        self.print99()

    def print99(self):
        for i in range(1, 10):
            for j in range(1, i+1):
                print('%dX%d=%2s ' % (j, i, i*j), end='')
            print('\n')


if __name__ == '__main__':
    pt = PrintTable()
