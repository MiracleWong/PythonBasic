#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import random

__author__ = "Miracle Wong"


class SelectBall(object):

    """开始打印9X9的乘法表"""

    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = input('请输入测试的次数')
            try:
                num = int(numStr)
            except ValueError:
                print('按照要求输入一个整数')
                continue
            else:
                break
        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for x in range(num):
            n = random.randint(1, 10)
            ball[n-1] = 1
        for i in range(1, 11):
            print('获取第%d号球的概率为%f' % (i, ball[i-1]*1.0/num))


if __name__ == '__main__':
    pt = SelectBall()
