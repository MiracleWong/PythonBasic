# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(-2*np.pi, 2*np.pi)

y1 = np.sin(x)
y2 = np.cos(x)

# 绘制大图
plt.axes([.1, .1, .8, .8])
plt.plot(x, y1, 'k')

# 绘制小图
plt.axes([.6, .6, .3, .3])
plt.plot(x, y2, 'r')

plt.show()