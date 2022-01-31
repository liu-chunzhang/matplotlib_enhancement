import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 500)
y1 = np.sin(2*np.pi*x)
y2 = 1.1*np.sin(3*np.pi*x)

fig, ax = plt.subplots(3, 1, sharex="all")

# "between y2 and 0"
ax[0].fill_between(x, 0, y2, color="b", alpha=0.5)		# 使用交叉曲线的填充方法

ax[0].set_ylim(-1.2, 1.2)
ax[0].locator_params(axis="y", nbins=5)

# "between y2 and 1.1"
ax[1].fill_between(x, 1.1, y2, color="b", alpha=0.5)

ax[1].set_ylim(-1.2, 1.2)
ax[1].locator_params(axis="y", nbins=5)

# "between y1 and y2"
ax[2].fill_between(x, y1, y2, color="b", alpha=0.5)

ax[2].set_xlim(0.0, 2.0)
ax[2].locator_params(axis="x", nbins=5)
ax[2].set_ylim(-1.2, 1.2)
ax[2].locator_params(axis="y", nbins=5)

plt.show()