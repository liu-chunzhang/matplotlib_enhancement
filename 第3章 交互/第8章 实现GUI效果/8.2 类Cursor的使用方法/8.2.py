import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Cursor

lineprops = dict(color="red", lw=1)

fig, ax = plt.subplots(1, 1, subplot_kw=dict(facecolor="lemonchiffon"))

x = np.random.random(100)
y = np.random.random(100)
ax.scatter(x, y, marker="o")
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(-0.02, 1.02)

cursor = Cursor(ax, useblit=True, **lineprops)

plt.show()