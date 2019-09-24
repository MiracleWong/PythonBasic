#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# AOOP 之 多重继承
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017502939956896


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 各种动物:
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Fly):
    pass


class Ostrich(Bird):
    pass


class MyTCPServer(TCPServer, ForkingMixIn):
    pass


class MyUDPServer(UDPServer, ThreadingMixIn):
    pass


class MyTCPServer(TCPServer, CoroutineMixIn):
    pass