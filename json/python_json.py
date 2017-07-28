#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json

# json.dumps用于编码json对象
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

jdata = json.dumps(data)

print  jdata

# json.loads用于解码json对象

jsonData = '{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}';

text = json.loads(jsonData)
print text