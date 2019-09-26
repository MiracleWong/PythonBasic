#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

from io import StringIO

f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())

f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())