#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import demjson

# demjson.encode用于将Python对象编码成JSON字符串
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

jdata = demjson.encode(data)

print jdata

# demjson.decode用于解码json数据

jsonData = '{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}';

text = demjson.decode(jsonData)
print text