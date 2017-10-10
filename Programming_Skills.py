#!/usr/local/bin/python
# -*- coding:utf-8 -*-

## 技巧合集
num_list = [6, 2, 7, 4, 1, 3, 5]
print num_list
print sorted(num_list)
print sorted(num_list, reverse=True)

num = [1, 2, 3, 4, 5, 6]
name =["My", 'Real', 'Name', 'Is', 'Wang', 'Rui']
for a,b in zip(num, name):
    print "%s is %d " %(b, a)

# 列表推导式
b = [i for i in range(1,11)]
print b

import time
a = []
t0 = time.clock()
for i in range(1,20000):
    a.append(i)
print "%s seconds process time " %(time.clock() - t0)

t0 = time.clock()
b = [i for i in range(1,20000)]
print "%s seconds process time " %(time.clock() - t0)

a = [ i**2 for i in range(1,10)]
b = [ j+1 for j in range(1,10)]
k = [ n for n in range(1,10) if n%2 == 0]
z = [letter.lower() for letter in 'ABCDEFGHIJK']
print a
print b
print k
print z

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
for num,letter in enumerate(letters):
    print "%s is %d" %(letter, num+1)