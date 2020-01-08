#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python的列表和元组功能
import sys
l = [1, 2, 'hello', 'world']
tup = ('jason', 22)
new_tup = tup + (5, )
print(l)
print(tup)
print(new_tup)
l.append(5)
print(l)

# 支持切片，左开右闭[)
print(l[1:3])
print(new_tup[1:3])


# 可以随意嵌套：
l = [[1, 2, 3], [4, 5]]  # 列表的每一个元素也是一个列表

tup = ((1, 2, 3), (4, 5, 6))  # 元组的每一个元素也是一元组
print(l)
print(tup)

print(list((1, 2, 3)))
print(tuple([1, 2, 3]))

# 列表和元组的异同

# 列表和元组都是有序的，可以存储任意数据类型的集合，区别主要在于下面这两点


# 列表是动态的，长度可变，可以随意的增加、删减或改变元素。列表的存储空间略大于元组，性能略逊于元组。

# 元组是静态的，长度大小固定，不可以对元素进行增加、删减或者改变操作。元组相对于列表更加轻量级，性能稍优。
