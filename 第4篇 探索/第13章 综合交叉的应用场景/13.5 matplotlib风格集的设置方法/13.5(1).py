import matplotlib.pyplot as plt
import numpy as np

from matplotlib.style.core import use

use("fivethirtyeight")

# ColorBrewer Diverging: RdYlBu
hexHtml = ["#d73027", "#f46d43", "#fdae61", "#fee090", "#ffffbf", "#e0f3f8", "#abd9e9", "#74add1", "#4575b4"]
sample = 1000
fig, ax = plt.subplots(figsize=(12, 6))

for i in range(len(hexHtml)):
	x = np.arange(sample)
	y = np.random.normal(0, 0.1, size=sample).cumsum()
	ax.scatter(x, y, label=str(i), linewidths=0.1, edgecolors="grey", facecolor=hexHtml[i])

ax.set_xlim(-200, 1200)
ax.locator_params(axis='x', nbins=8)
ax.set_ylim(-8, 10)
ax.locator_params(axis='y', nbins=10)

ax.legend(loc=1)

plt.show()