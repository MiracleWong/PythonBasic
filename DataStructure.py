#!/usr/bin/env python
# -*- coding:utf-8 -*-

# List
Weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(Weekday[0])

## List正负索引的使用
periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])
print(periodic_table[:9])

# 字典Dictonary

## 字典的特征
# 1. 字典中数据必须是以键值对的形式出现的
# 2. 逻辑上讲，键是不能重复的，而值可以重复
# 3. 字典中的键（key）是不可改变的，也就是无法修改的；而值（value），是可改变的，可修改的，可以是任何对象

# 注意：字典不能够进行切片
NASDAQ_CODE = {
    'BIDU': 'Baidu',
    'SINA':'Sina',
    'YOKU': 'Youku'
}

print(NASDAQ_CODE)
a = {'key' : 123, 'key' : 123}
print(a)

NASDAQ_CODE.update({'FB': 'FaceBook', 'TSLA': 'Tesla'})
print(NASDAQ_CODE)

del NASDAQ_CODE['FB']
print(NASDAQ_CODE)

## 元组
letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(letters[0])

# 集合
a_set = {1,2,3,4}
a_set.add(5)
a_set.discard(5)
print(a_set)