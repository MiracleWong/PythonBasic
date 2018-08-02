#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

import numpy as np

# x = np.linspace(-np.pi * 2 , np.pi * 2, 100)
# plt.figure(1, dpi=50)
# for i in range(1,5):
#     plt.plot(x, np.sin(x / i))
# plt.show()

# plt.figure(1, dpi=200)
# data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
# plt.hist(data)
# plt.show()

# x = np.arange(1, 10)
# y = x
# fig = plt.figure()
# plt.scatter(y, x, c='r', marker='o')
# plt.show()

import pandas as pd

# iris = pd.read_csv("./iris_training.csv")
# print(iris.head())
#
# iris.plot(kind='scatter', x="120", y="4")
#
# plt.show()


import seaborn as sns

iris = pd.read_csv("./iris_training.csv")

sns.set(style='white', color_codes=True)
sns.jointplot(x="120", y="4", data=iris, size=5)
sns.distplot(iris['120'])
plt.show()