# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
from matplotlib import animation as animation
import numpy as np

x_bar = [10, 20, 30, 40, 50] #柱形图横坐标
fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
line, = plt.plot(x, np.sin(x))

def update(i):
    line.set_ydata(np.sin(x + i/10.0))
    return line,

## 绘制动图
animation = animation.FuncAnimation(fig, update)
plt.show()