#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

try:
    f = open('/Users/miraclewong/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/Users/miraclewong/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

# 读取非UTF-8编码
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# 写文件
with open('/Users/miraclewong/writes.txt', 'w') as f:
    f.write('Hello, world!')