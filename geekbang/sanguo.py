# -*- coding:utf-8 -*-

# 读取人物名称
f = open('/Users/miraclewong/github/PythonBasic/geekbang/txt/name.txt',encoding='utf-8')
data = f.read()
data0 = data.split('|')
print(data0)
#
# 读取兵器名称
f2 = open('/Users/miraclewong/github/PythonBasic/geekbang/txt/weapon.txt',encoding='utf-8')
# data2 = f2.read()
i = 1
for line in f2.readlines():
    if i % 2 == 1:
        print(line.strip('\n'))
    i += 1
#
f3 = open('/Users/miraclewong/github/PythonBasic/geekbang/txt/sanguo.txt',encoding='GB18030')
print(f3.read().replace('\n',''))