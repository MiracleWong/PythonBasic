# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt #载入 pyplot 绘图模块
import numpy as np # 载入数值计算模块

# X,y 的坐标均有 numpy 在 0 到 1 中随机生成 1000 个值
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
size = np.random.normal(20,30,100)

# 向方法中 `*args` 输入 X，y 坐标
plt.scatter(x, y, s=size, c=colors)
plt.show()