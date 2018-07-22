#!/usr/bin/env python
# -*- coding: utf-8 -*-


def a_line(a, b):
    def arg_y(x):
        return a * x + b
    return arg_y


line1 = a_line(3, 5)
line2 = a_line(6, 5)
print(line1(10))
print(line1(20))
print(line2(10))
print(line2(20))


