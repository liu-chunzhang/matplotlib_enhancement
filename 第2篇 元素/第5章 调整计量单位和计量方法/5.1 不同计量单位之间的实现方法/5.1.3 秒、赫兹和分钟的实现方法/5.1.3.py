import matplotlib.pyplot as plt
import numpy as np

from basic_units import secs, minutes, hertz

t = [2, 4, 3, 5, 8, 6, 7, 9]
secs_t = [time*secs for time in t]

fig, ax = plt.subplots(3, 1, sharex=True)

ax[0].scatter(secs_t, secs_t, s=10*np.max(t), c="steelblue", marker="o", edgecolor='r')
ax[0].set_xlim(0.0, 10.0)
ax[0].set_xlabel("")
ax[0].set_ylim(0.0, 10.0)
ax[0].set_ylabel("")
ax[0].locator_params(axis='y', nbins=11)

ax[1].scatter(secs_t, secs_t, s=10*np.max(t), c="gold", marker="D", yunits=hertz, edgecolor='b')
ax[1].set_xlabel("")
ax[1].set_ylabel("")
ax[1].locator_params(axis='y', nbins=6)
ax[1].axis([1, 10, 0, 1])

ax[2].scatter(secs_t, secs_t, s=10*np.max(t), c="brown", marker="^", yunits=hertz, edgecolor='c')
#ax[2].yaxis.set_units(minutes)		# 这个函数似乎完全没用。
ax[2].set_xlabel("")
ax[2].set_ylim(0.0, 1.0)
ax[2].set_ylabel("")
ax[2].locator_params(axis='y', nbins=6)

fig.subplots_adjust(hspace=0.2)

plt.show()