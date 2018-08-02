
# -*- coding:utf-8 -*-

from pandas import Series, DataFrame
import pandas as pd

obj = Series([4,5,6,7])
print(obj)
print(obj.index)
print(obj.values)


obj2 = Series([4, 7, -3, 6], index=['d', 'b', 'c', 'a'])

print(obj2)

# data = DataFrame([[1., 6.5, 3], [1., NA, NA]])

import numpy as np
data3 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])

print(data3.unstack())
# print(data3['b':'c'])