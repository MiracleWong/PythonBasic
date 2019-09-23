#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'


class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart Simpson', 59)
print(bart.print_score())
print(bart._Student__name)

# 以下是错误写法
bart.__name = 'New Name'
print(bart.get_name())
print(bart._Student__name)
print(bart.__name)