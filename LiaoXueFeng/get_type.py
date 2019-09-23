#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# OOP 之 获取对象信息
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017499532944768

import types
from animals import Animal, Dog

print(type(123))
print(type('123'))
print(type(None))
print(type(abs))
a = Animal()
print(type(a))


def fn():
    pass


print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


# 使用isinstance()
class Husky(Dog):
    def run():
        print("Husky is running...")


d = Dog()
h = Husky()
print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

print(dir('ABC'))
print(len('ABC'))
print('ABC'.__len__())