
# -*- coding:utf-8 -*-

import numpy as np

arr1 = np.array([2, 3, 4])
print(arr1)
print(arr1.dtype)

arr2 = np.array([1.2, 1.3, 1.4])
print(arr2)
print(arr2.dtype)

print(arr1 + arr2)
print(arr2 * 10)

print(np.zeros(10))
print(np.zeros([3, 5]))
print(np.ones((4, 6)))
print(np.empty((2,3,2)))

arr4 = np.arange(10)
arr4[5:8] = 10
print(arr4)

