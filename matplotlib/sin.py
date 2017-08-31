# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
import numpy as np

X = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = np.sin(X)
y2 = np.cos(X)

plt.plot(X, y1, color='r', linestyle=':', linewidth=2, alpha=0.8)
plt.plot(X, y2, color='b', linestyle='-', linewidth=2)
plt.show()
