#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017063413904832

# Python基础
print('包含中文的str')
# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(chr(66))
print(chr(25191))

# 编码

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# list 和 tuple
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))  # 长度
print(classmates[0])
print(classmates[-1])
classmates.append('Adam')  # 追加
print(classmates)
classmates.insert(1, 'Jack')  # 插入到指定位置
print(classmates)
classmates.pop(1)  # 移除指定位置
print(classmates)
classmates[1] = 'Sarah'
print('classmates =', classmates)

# 不同类型的list
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
L1 = []

# 元组tuple
t = (1, 2)
print(t)
t1 = (1, )  # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
print(t1)

# 可变tuple
t2 = ('a', 'b', ['A', 'B'])
# print(t2[2])
t2[2][0] = 'X'
t2[2][1] = 'Y'
print(t2)

# 条件判断

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# 循环

# for
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in range(0, 101):
    sum = sum + x
    print(sum)

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

# continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# dict
# set

# s = set([1, 2, 3])
s = set([1, 1, 2, 2, 3, 3])  # 在set中，没有重复的key。
print(s)
""" set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作： """
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 练习Practice

L = [['Apple', 'Google', 'Microsoft'], ['Java', 'Python', 'Ruby', 'PHP'],
     ['Adam', 'Bart', 'Lisa']]

print(L[0][0])
print(L[1][1])
print(L[2][2])
