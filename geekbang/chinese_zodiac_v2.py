#!/usr/bin/env python
# -*- coding: utf-8 -*-

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = int(input('请用户输入出生年份'))

print(chinese_zodiac[year % 12])