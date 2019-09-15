#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import sys

# 官方内置函数合集
# https: // docs.python.org/3/library/functions.html

# 函数定义


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return - x


print(my_abs(99))


# 返回多个值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    # return nx, ny
    return (nx, ny)


# 在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
x, y = move(100, 100, 60, math.pi / 6)
# 默认参数必须指向不变对象！


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))
print(calc(1, 2, 3))
print(calc(0))

nums = [1, 2, 3]
tp1 = (1, 2, 3, 4, 5, 6)
print(calc(*nums))
print(calc(*list(tp1)))


# 关键字参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 命名关键字参数
def person1(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person1('Jack', 24, city='Nanjing', job='Engineer')
person1('Jack', 24, job='Engineer')


# 递归形式
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(5))

# 尾递归的形式
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(10))


# Practice
n1 = 255
n2 = 1000
print('n1转换十六进制后为：%s' % hex(n1), '\n''n2转换十六进制后为：%s' % hex(n2))

print(x, y)
