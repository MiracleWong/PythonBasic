#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'MiracleWong'

# 超实用的 30 段 Python 案例
# 地址：https://mp.weixin.qq.com/s/_q1eJPXZYL7r6VAyjt7Jag

import sys
import time
import random
from collections import Counter
from iteration_utilities import deepflatten


# 1.检查重复元素
def all_unique(lst):
    return len(lst) == len(set(lst))


x = [1, 1, 2, 2, 3, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]
print(all_unique(x))  # False
print(all_unique(y))  # True


# 2. 变位词
def anagram(first, second):
    return Counter(first) == Counter(second)


print(anagram("abcd3", "3acdb"))  # True

# 3. 内存使用情况
variable = 30
print(sys.getsizeof(variable))  # 24
