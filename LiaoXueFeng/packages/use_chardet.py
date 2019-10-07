#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

import chardet
print(chardet.detect(b'Hello, world!'))

data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))

data2 = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data2))

data3 = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data3))

## Notes
## chardet的支持列表：https://chardet.readthedocs.io/en/latest/supported-encodings.html