#!/usr/local/bin/python
# -*- coding:utf-8 -*-
## 书籍《编程小白的第一本Python书籍》第4章 函数
def fahrenheit_converter(C):
    fahrenheit = C * 9/5 + 32
    return str(fahrenheit) + '˚F'

lyric_length = len('I Cry Out For Magic!')
print(lyric_length)

C2F = fahrenheit_converter(35)
print(C2F)
C2F2 = fahrenheit_converter(13)
print(C2F2)
C2F3 = fahrenheit_converter(0)
print(C2F3)
C2F4 = fahrenheit_converter(-3)
print(C2F4)

def trapezoid_area(base_up, base_down, height=3):
    return 1.0/2 * (base_up + base_down) * height;

print trapezoid_area(1,2,3)

base_up = 1
base_down = 2
height = 3
print trapezoid_area(base_up, base_down, height)
print trapezoid_area(base_up, base_down)
print trapezoid_area(base_up, base_down, 15)

def text_create(name, msg):
    desktop_path = '/Users/miraclewong/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print("Done")

text_create('Hello', "Hello World!")



## 