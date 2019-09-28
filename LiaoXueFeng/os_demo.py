#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# IO编程 之 操作文件和目录
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017502939956896

import os
print(os.name)
print(os.cpu_count())
print(os.uname())
print(os.environ)
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
os.path.join('/Users/miraclewong', 'testdir')
os.mkdir('/Users/miraclewong/testdir')
os.rmdir('/Users/miraclewong/testdir')
print(os.path.split('/Users/miraclewong/testdir/file.txt'))
print(os.path.splitext('/path/to/file.txt'))
print([
    x for x in os.listdir('.')
    if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'
])
print([x for x in os.listdir('.') if os.path.isdir(x)])