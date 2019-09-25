#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# AOOP 之 定制类
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904#0

# __str__ && __repr__


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


s = Student('Michael')
print(s)


# __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a


for n in Fib():
    print(n)


# __getitem__
class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = Fib2()
print(f[0])
print(f[1])
print(f[2])

print(list(range(100))[5:10])
print(f[:10])


# __getattr__
class Student2(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' %
                             attr)


s = Student2()

print(s.name)
print(s.age())
print(s.score)


# __call__
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student3('Michael')
print(s())

print(callable(Student3('Michael')))
print(callable(max))

# Notes：通过callable()函数，我们就可以判断一个对象是否是“可调用”对象，能被调用的对象就是一个Callable对象