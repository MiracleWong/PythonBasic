#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

# 1 高阶函数 (Higher-order function)

# Notes
# 函数本身也可以赋值给变量，即：变量可以指向函数。
# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。


def add(x, y, f):
    return f(x) + f(y)


x = -5
y = 6
print(add(-5, 6, abs))


# 1.2 map/reduce
def f(x):
    return x * x


r = map(f, [1, 2, 4, 5, 6, 7, 8, 9])
print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(reduce(fn, map(char2num, '13579')))


# 整理代码
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('24689'))
