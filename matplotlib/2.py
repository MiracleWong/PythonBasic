from matplotlib import pyplot as plt
import numpy as np

X = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(X)

plt.plot(X, y)
plt.show()
