# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt #载入 pyplot 绘图模块
import numpy as np # 载入数值计算模块

# X,y 的坐标均有 numpy 在 0 到 1 中随机生成 1000 个值
X = np.random.normal(0,1,1000)
y = np.random.normal(0,1,1000)

# 向方法中 `*args` 输入 X，y 坐标
plt.scatter(X, y)
plt.show()