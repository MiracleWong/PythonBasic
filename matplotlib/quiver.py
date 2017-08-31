# -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt #载入 pyplot 绘图模块
import numpy as np # 载入数值计算模块

# 生成数据矩阵
X, y = np.mgrid[0:10, 0:10]
# 绘图
plt.quiver(X, y)
plt.show()