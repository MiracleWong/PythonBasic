# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(-2*np.pi, 2*np.pi)
y1 = np.sin(x)
y2 = np.cos(x)


plt.plot(x, y1, color='r', linestyle='--', linewidth=2, label='sin')
plt.plot(x, y2, color='b', linestyle='-', linewidth=2, label='cos')

plt.legend(loc='upper left')
plt.show()