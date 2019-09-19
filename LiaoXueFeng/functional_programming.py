#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

# 1 高阶函数 (Higher-order function)

# Notes
# 函数本身也可以赋值给变量，即：变量可以指向函数。
# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。


# def add(x, y, f):
#     return f(x) + f(y)


# x = -5
# y = 6
# print(add(-5, 6, abs))


# # 1.2 map/reduce
# def f(x):
#     return x * x


# r = map(f, [1, 2, 4, 5, 6, 7, 8, 9])
# print(list(r))
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# def add(x, y):
#     return x + y


# print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# def fn(x, y):
#     return x * 10 + y


# print(reduce(fn, [1, 3, 5, 7, 9]))


# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]


# print(reduce(fn, map(char2num, '13579')))


# # 整理代码
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
#           '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y

#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))


# def char2num(s):
#     return DIGITS[s]


# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# print(str2int('24689'))


# # 1.2 filter
# def is_odd(n):
#     return n % 2 == 1


# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))


# def not_empty(s):
#     return s and s.strip()


# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# # Notes
# # filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list

# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n


# def _not_divisible(n):
#     return lambda x: x % n > 0


# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)


# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# 1.3 sorted
print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

# Notes
# sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
