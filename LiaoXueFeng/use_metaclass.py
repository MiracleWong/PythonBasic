#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# AOOP 之 使用元类
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017502939956896


# type()
# Notes: type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


h = Hello()
print(h.hello())
print(type(Hello))
print(type(h))