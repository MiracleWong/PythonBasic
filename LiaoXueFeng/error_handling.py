#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# 错误、调试和测试 之 错误处理
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017598873256736
import logging

try:
    print("try...")
    r = 10 / 1
    print("result:", r)
except ValueError as e:
    print("ValueError:", e)
except ZeroDivisionError as e:
    print("except:", e)
else:
    print('no error!')
finally:
    print("finally...")
print("End")

# Notes: Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy


# Notes: 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
        # print('Error:', e)
    finally:
        print('finally...')


if __name__ == "__main__":
    main()


# 抛出错误
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('0')


# 另一种处理方式，向上级抛出
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


bar()