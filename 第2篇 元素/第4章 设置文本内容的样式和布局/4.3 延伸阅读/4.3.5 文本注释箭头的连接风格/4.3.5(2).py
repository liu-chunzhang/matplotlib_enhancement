import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 3, figsize=(12, 6), sharex=True, sharey=True)

x1, y1 = 0.3, 0.3
x2, y2 = 0.7, 0.7

bbox = dict(boxstyle="square", facecolor="w", edgecolor='k')

# subplot(131)
ax[0].annotate("simple", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", bbox=dict(boxstyle='round', fc='w', ec='k'), 
				arrowprops=dict(arrowstyle="simple, head_length=0.7, head_width=0.6, tail_width=0.3", color='gray', shrinkA=5, shrinkB=5,
				patchB=None, connectionstyle="angle3, angleA=0, angleB=90"), size=15, ha='center', va='center')

ax[0].text(0.05, 0.95, "angle3,\nangleA=0,\nangleB=90", ha='left', va='top', bbox=bbox, size=15)
ax[0].set_xlim(0, 1)
ax[0].set_ylim(0, 1)
ax[0].set_xticklabels([])
ax[0].set_yticklabels([])

# subplot(132)
ax[1].annotate("fancy", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", bbox=dict(boxstyle='round', fc='w', ec='k'), 
				arrowprops=dict(arrowstyle="fancy, head_length=0.4, head_width=0.4, tail_width=0.6", color='gray', shrinkA=5, shrinkB=5,
				patchB=None, connectionstyle="arc3, rad=0.5"), size=15, ha='center', va='center')

ax[1].text(0.05, 0.95, "arc3,\nrad=0.5", ha='left', va='top', bbox=bbox, size=15)
ax[1].set_xlim(0, 1)
ax[1].set_ylim(0, 1)
ax[1].set_xticklabels([])
ax[1].set_yticklabels([])

# subplot(133)
ax[2].annotate("wedge", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", bbox=dict(boxstyle='round', fc='w', ec='k'), 
				arrowprops=dict(arrowstyle="wedge, tail_width=0.5", color='gray', shrinkA=5, shrinkB=5, patchB=None, 
					connectionstyle="arc3, rad=-0.3"), size=15, ha='center', va='center')

ax[2].text(0.05, 0.95, "arc3,\nrad=-0.3", ha='left', va='top', bbox=bbox, size=15)
ax[2].set_xlim(0, 1)
ax[2].set_ylim(0, 1)
ax[2].set_xticklabels([])
ax[2].set_yticklabels([])

fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95, wspace=0.02, hspace=0.02)

plt.show()