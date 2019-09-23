#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# OOP 之 继承和多态
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017497232674368


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print("Dog is running...")

    def eat(self):
        print("Eating meat...")


class Cat(Animal):
    def run(self):
        print("Cat is running...")


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


# 多态: 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()
dog = Dog()
print(dog.run())

cat = Cat()
print(cat.run())

# 测试数据类型
a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(isinstance(b, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


print(run_twice(Animal()))
print(run_twice(Dog()))
print(run_twice(Cat()))
print(run_twice(Tortoise()))

# 鸭子类型: 它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。