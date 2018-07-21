#!/usr/bin/env python
# -*- coding:utf-8 -*-
L1 = [1, 2, 3, 4, 5]
L2 = [1, 'spam', [2.3, 4]]
L3 = []
print(L1)
print(L2)
print(L3)

L = [1, 2, 3, 4, 5]
L.append(5)
print(L)

L = [4, 5, 6, 7, 8]
L[1:3] = ["aa", "bb", "cc", "dd"]
print(L)

L = [1, 5, 3, 8, 3, 2, 10]
L.sort()
print(L)
L.reverse()
print(L)

D = {
    'name': {'first':'Bob', 'last':'Smith'},
    'job': ['dev','mgr'],
    'age': 0.5,
    'addr': 'BeiJing'
}
print(D)

## 生成字典
D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
print(D)

key_list = ['a','b','c']
value_list = [11,22,33]
D = dict(zip(key_list, value_list))
print(D)

D = {'a': 11, 'b': 22, 'c': 33, 'd': 44, 'e': 55}
print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))

# 元组
