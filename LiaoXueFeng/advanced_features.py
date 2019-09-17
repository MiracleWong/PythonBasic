#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'
from collections import Iterable


# 1 切片
# 切片的区间是左闭右开的[)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L)
print(L[:])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-1])
print(L[-2:-1])

L1 = list(range(100))
print(L1[:10])
print(L1[-10:])
print(L1[10:20])
print(L1[:10:2])
print(L1[::5])
print(L1[:])

print((0, 1, 2, 3, 4, 5)[:3])  # tuple 的切片还是 tuple
print('ABCDER'[:3])
print('ABCDER'[::2])


# Practice
# 实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
def trim(s):
    while len(s) > 0 and s[:1] == ' ':
        s = s[1:]
    while len(s) > 0 and s[-1:] == ' ':
        s = s[0:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


# 2 迭代

# dict 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)

for ch in 'ABC':
    print(ch)

print(isinstance('ABC', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))


"""
list 实现下表循环，enumerate实现索引-元素树
"""
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# Practice
def findMinAndMax(L):
    if not L:
        # L是空
        return (None, None)

    # L不是空
    min = max = L[0]
    for i in L:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
