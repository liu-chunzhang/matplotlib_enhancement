import matplotlib as mpl
mpl.use("qt5agg")

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.exp(-x) * np.sin(2*np.pi*x)

plt.plot(x, y, color='g', linewidth=3.0)

plt.show()