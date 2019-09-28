#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# IO编程 之 序列化
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424

import json
d = dict(name='Bob', age=20, score=88)
j = json.dumps(d)
print(j)

json_str = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {'name': std.name, 'age': std.age, 'score': std.score}


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))