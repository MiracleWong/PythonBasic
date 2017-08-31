# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
from mpl_tookits.mplot3d import Axes3D
import numpy as np

x= np.linspace(-6 * np.pi, 6 * np.pi, 1000)
y= np.sin(x)
z= np.cos(y)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z)

plt.show()