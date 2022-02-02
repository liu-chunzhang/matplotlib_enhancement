import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Cursor		# 导入类Cursor的导入工作

lineprops = dict(color="red", lw=1)

fig, ax = plt.subplots(subplot_kw=dict(facecolor="lemonchiffon"))

x = np.random.random(100)
y = np.random.random(100)
ax.scatter(x, y, marker="o")
ax.margins(0.02)

cursor = Cursor(ax, useblit=True, **lineprops)

plt.show()