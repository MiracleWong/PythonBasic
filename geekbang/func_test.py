#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from functools import reduce
#
# def func(a, b, c):
#     print("a = %s" % a)
#     print("b = %s" % b)
#     print("c = %s" % c)
#
# func(1, c=2, b=33)
#
# def howlong(first, *others):
#     print(1 + len(others))
#
# howlong(12, 3, 45, 67)
#
# var1 = 123
# def func1():
#     var1 = 456
#     print(var1)
#
# func1()
# print(var1)
#
# # range 不支持步长为小数
# for i in range(10, 20, 1):
#     print(i)
#
# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step
#
# for i in frange(10, 20, 0.5):
#     print(i)
#
# def true(): return True
# lambda : True
# b1 = [1, 2, 3, 4, 5, 6, 7]
# filter(lambda x: x > 2, b1)
#
# a = [1, 2, 3]
# print(map(lambda x:x, a))
# print(list(map(lambda x:x, a)))
# print(list(map(lambda x:x+1, a)))
# b = [4, 5, 6]
# print(list(map(lambda x, y: x+y, a, b)))
# print(reduce(lambda x, y: x+y, [2, 3, 4], 1))
#
# dicta = {"a": "aa", "b": "bb"}
# dictb = zip(dicta.values(), dicta.keys())
# print(dictb)
# print(dict(dictb))


def func():
    a = 1
    b = 2
    return a + b


def sum(a):
    def add(b):
        return a + b
    return add


num1 = func()
print(num1)
num2 = sum(1)
print(num2(4))

# print(type(num1))
# print(type(num2))


