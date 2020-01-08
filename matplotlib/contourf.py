# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt  #载入 pyplot 绘图模块
import numpy as np  # 载入数值计算模块

# 生成数据
x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)
X, Y = np.meshgrid(x, y)
Z = (1 - X / 2 + X**3 + Y**4) * np.exp(-X**2 - Y**2)

# 绘图
plt.contourf(X, Y, Z)
plt.show()