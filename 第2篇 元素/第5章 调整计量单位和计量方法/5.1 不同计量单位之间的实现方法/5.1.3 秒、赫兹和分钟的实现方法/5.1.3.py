import matplotlib.pyplot as plt
import numpy as np

from basic_units import secs, minutes, hertz
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(3, 1, sharex=True)

t = [2, 4, 3, 5, 8, 6, 7, 9]
secs_t = [time*secs for time in t]

# subplot(311)
ax[0].scatter(secs_t, secs_t, s=5*np.max(t), facecolor="steelblue", marker="o", edgecolor='r')

ax[0].set_xlim(1.0, 10.0)
ax[0].set_xlabel("")
ax[0].xaxis.set_major_locator(MultipleLocator(1))
ax[0].set_ylim(1.0, 10.0)
ax[0].set_ylabel("")
ax[0].yaxis.set_major_locator(MultipleLocator(1))

# subbplot(312)
ax[1].scatter(secs_t, secs_t, s=5*np.max(t), facecolor="gold", marker="D", yunits=hertz, edgecolor='b')

ax[1].axis([1, 10, 0, 1])
ax[1].set_xlabel("")
ax[1].set_ylabel("")
ax[1].yaxis.set_major_locator(MultipleLocator(0.2))

# subbplot(313)
ax[2].scatter(secs_t, secs_t, s=5*np.max(t), facecolor="brown", marker="^", yunits=hertz, edgecolor='c')

ax[2].axis([1, 10, 0, 1])
#ax[2].yaxis.set_units(minutes)		# 这个函数似乎完全没用？在作图时应直接使用待用单位，不再经历转换！
ax[2].set_xlabel("")
ax[2].set_ylim(0.0, 1.0)
ax[2].set_ylabel("")
ax[2].yaxis.set_major_locator(MultipleLocator(0.2))

fig.subplots_adjust(hspace=0.2)

plt.show()