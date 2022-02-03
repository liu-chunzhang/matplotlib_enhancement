import matplotlib.pyplot as plt
import numpy as np

from matplotlib.style.core import use
from matplotlib.ticker import MultipleLocator

use("fivethirtyeight")						# 设置fivethirtyeight

# ColorBrewer Diverging: RdYlBu
hexHtml = ["#d73027", "#f46d43", "#fdae61", "#fee090", "#ffffbf", "#e0f3f8", "#abd9e9", "#74add1", "#4575b4"]
sample = 1000
fig, ax = plt.subplots(figsize=(8, 5.6))

for i in range(len(hexHtml)):
	x = np.arange(sample)
	y = np.random.normal(0, 0.1, size=sample).cumsum()
	ax.scatter(x, y, label=str(i), linewidths=0.1, s=3, edgecolors="grey", facecolor=hexHtml[i])

ax.set_xlim(-200, 1200)
ax.xaxis.set_major_locator(MultipleLocator(200))
ax.yaxis.set_major_locator(MultipleLocator(2))
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

ax.legend(loc=1)

plt.show()