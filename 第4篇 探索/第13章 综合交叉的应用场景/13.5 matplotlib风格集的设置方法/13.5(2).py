import matplotlib.pyplot as plt
import numpy as np

from matplotlib.style.core import use, available

use("ggplot")

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['axes.edgecolor'] = 'k'

x = np.linspace(0, 2*np.pi, 100)
y = 1.85*np.sin(x)
y1 = 1.85*np.sin(x) + np.random.randn(100)

fig, ax = plt.subplots(2, 2, sharex=True, sharey=True)

# subplot(221)
ax[0, 0].scatter(x, y1, s=50, c="dodgerblue")

ax[0, 0].locator_params(axis='x', nbins=9)
ax[0, 0].set_ylim(-5, 5)
ax[0 ,0].locator_params(axis='y', nbins=5)

ax[0, 0].set_facecolor("lemonchiffon")

# subplot(222)
ax[0, 1].plot(x, y, lw=3, c="yellowgreen")

ax[0, 1].set_xlim(-1, 7)
ax[0, 0].locator_params(axis='x', nbins=9)
ax[0, 1].set_ylim(-5, 5)

ax[0, 1].set_facecolor("lemonchiffon")

# subplot(223)
ax[1, 0].plot(x, y, ls="--", lw=3, c="k")
ax[1, 0].scatter(x, y1, s=50, c="r")

ax[1, 0].locator_params(axis='y', nbins=5)
ax[1, 0].set_ylim(-5, 5)

ax[1, 0].set_facecolor("lemonchiffon")

# subplot(224)
# non-existence
fig.suptitle("'ggplot' style of subplots(2, 2)", fontsize=18, weight="bold", family="monospace")	# for figure 13-10 in book
#fig.suptitle("'ggplot' style of subplots(2, 2)", fontsize=18, weight="bold", family="monospace")	# for figure 13-11 in book

plt.show()