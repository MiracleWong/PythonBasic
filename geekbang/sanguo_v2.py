# -*- coding:utf-8 -*-
import re

# 读取人物名称
def find_hero(hero):
    with open('/Users/miraclewong/github/PythonBasic/geekbang/txt/sanguo.txt'
            ,encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        # print("主角 %s 出现了 %d 次" %(hero, len(name_num)))
    return len(name_num)

name_dict = {}
with open('/Users/miraclewong/github/PythonBasic/geekbang/txt/name.txt'
        ,encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            # print(n)
            name_num = find_hero(n)
            name_dict[n] = name_num

name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])