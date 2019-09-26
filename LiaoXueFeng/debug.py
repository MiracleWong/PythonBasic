#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# 错误、调试和测试 之 调试
# 地址：https://www.liaoxuefeng.com/wiki/1016959663602400/1017602696742912
import logging
# logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     # print('>>> n = %d' % n)
#     return 10 / n

# def main():
#     foo('0')

# if __name__ == "__main__":
#     main()