# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
import numpy as np

X = np.linspace(-2*np.pi, 2*np.pi, 10)
y = np.sin(X)

plt.bar(X, y)
plt.show()
