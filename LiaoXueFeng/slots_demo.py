#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# 面向对象高级编程 之 使用__slots__
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017501655757856

from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Miracle'
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

s2 = Student()
# s2.set_age(25)


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(20)
print(s.score)
s2.set_score(100)
print(s2.score)


class Student1(object):
    __slots__ = ('name', 'age')


s1 = Student1()
s1.name = 'Michael'
s1.age = 20

# s1.score = 30


# Notes: 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student1):
    pass


g = GraduateStudent()
g.score = 9999
print(g.score)