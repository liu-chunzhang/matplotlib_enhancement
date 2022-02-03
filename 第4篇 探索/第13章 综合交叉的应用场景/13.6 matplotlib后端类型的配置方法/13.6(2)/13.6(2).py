import matplotlib as mpl
mpl.use("qt5agg")

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots()

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.exp(-x) * np.sin(2*np.pi*x)

plt.plot(x, y, color='g', linewidth=3.0)

ax.set_xlim(-8, 8)
ax.xaxis.set_major_locator(MultipleLocator(2.0))
ax.set_ylim(-600, 400)
ax.yaxis.set_major_locator(MultipleLocator(200))

plt.show()