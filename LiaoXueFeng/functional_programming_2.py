#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools
# 2 返回函数


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(1, 3, 5, 7, 9))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)
print(f2())


# 闭包
def count():
    fs = []
    for i in range(1, 4):

        def f():
            return i * i

        fs.append(f)
    return fs


# Notes: 一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
f1, f2, f3 = count()

print(f1(), f2(), f3())


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

# 3 匿名函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

# 可以把匿名函数作为返回值返回


def build(x, y):
    return lambda: x * x + y * y


# Practice
L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)

# 4 装饰器


def now():
    print('2015-3-25')


f = now
print(f())
print(now.__name__)
print(f.__name__)


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


f = now
print(f())
print(now.__name__)
print(f.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


f = now
print(f())
print(now.__name__)
print(f.__name__)

# 5 偏函数
print(int('12345', base=8))
print(int('12345', base=16))

# Notes: functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1111111'))

max2 = functools.partial(max, 10)
print(max2(1, 2, 3, 4, 5, 6, 7, 8))
print(max2(1, 2, 3, 4, 5, 6, 7, 8, 20))
