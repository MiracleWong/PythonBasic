#!/usr/bin/env python
# -*- coding:utf-8 -*-


def binary_search(list, item):
    # low 和 high 用于跟踪要在其中查找的部分
    low = 0
    high = len(list) - 1

    # 只要范围没有缩小到只有一个元素，就继续循环
    while low <= high:
        # 检查中间的元素
        mid = (low + high) // 2  # 这里注意下，必须是 // 而不是 /，否则会报错
        guess = list[mid]
        # 如果猜的数是对了，返回结果
        if guess == item:
            return mid
        # 如果猜的数大了，上限减1
        if guess > item:
            high = mid - 1
        # 如果猜的数小了，下限加1
        else:
            low = mid + 1

    # 如果没有这个元素，返回None
    return -1


my_list = [1, 2, 2, 4, 5, 5]  ##测试数据
# my_list = [3, 4, 5, 8, 8, 8, 8, 10, 13, 14]  ##测试数据
# my_list = [1, 2, 3, 3, 4, 5, 10]  # 测试数据

print(binary_search(my_list, 3))
