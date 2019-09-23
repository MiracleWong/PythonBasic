#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# OOP 之 获取对象信息
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017499532944768


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))