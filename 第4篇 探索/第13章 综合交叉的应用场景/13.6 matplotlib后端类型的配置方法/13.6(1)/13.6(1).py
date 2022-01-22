import matplotlib as mpl
mpl.rcParams["backend"] = "Qt5Agg"	# Qt4Agg在Matplotlib3.3版本后已被弃用，需要使用Qt5Agg

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.exp(-x) * np.sin(2*np.pi*x)

plt.plot(x, y, linewidth=3.0)
plt.show()