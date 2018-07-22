#!/usr/bin/env python
# -*- coding: utf-8 -*-


def new_tips(argv):
    def tips(func):
        def nei(a, b):
            print("start %s %s" %(argv, func.__name__))
            func(a, b)
            print("stop")

        return nei
    return tips


@new_tips('add_modules')
def add(a, b):
    print(a + b)


@new_tips('sub_modules')
def sub(a, b):
    print(a - b)

print(add(4, 5))
print(add(7, 3))