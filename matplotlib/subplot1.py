# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(-2*np.pi, 2*np.pi)

y1 = np.sin(x)
y2 = np.cos(x)

# 绘制图1、2
plt.subplot(2,2,1)
plt.plot(x, y1, 'k')
plt.subplot(2,2,2)
plt.plot(x, y2, 'r')

# 绘制图3、4
plt.subplot(2,2,3)
plt.plot(x, y1, 'y')
plt.subplot(2,2,4)
plt.plot(x, y2, 'g')

plt.show()