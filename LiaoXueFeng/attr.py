#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# class Student(object):
#     def __init__(self, name):
#         self.name = name

# s = Student('Bob')
# s.score = 90
# print(s.score)


class Student(object):
    name = 'Student'


s = Student()
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
print(Student.name)  # 打印类的name属性
s.name = 'Michael'  # 给实例绑定name属性
print(s.name)  # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name)  # 但是类属性并未消失，用Student.name仍然可以访问
print('----------')
del s.name  # 如果删除实例的name属性
print(s.name)  # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了


# Practice
class Student(object):
    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name


# 测试:
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')