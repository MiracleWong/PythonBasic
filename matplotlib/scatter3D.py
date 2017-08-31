# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
from mpl_tookits.mplot3d import Axes3D
import numpy as np

x= np.random.normal(0, 1, 100)
y= np.random.normal(0, 1, 100)
z= np.random.normal(0, 1, 100)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x,y,z)

plt.show()