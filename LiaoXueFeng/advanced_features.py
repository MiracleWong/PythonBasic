#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'
import os
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


# 3 列表生成式
print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x*x)
print(L)

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


# Practice
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


# 4 生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(type(f))


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


for n in fib(6):
    print(n)

g = fib(6)

# 返回generator的返回值
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# Practice
# 他人示例：https://www.liaoxuefeng.com/discuss/969955749132672/1302345965109282
def triangles():
    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
