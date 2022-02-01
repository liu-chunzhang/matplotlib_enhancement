import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 3, figsize=(12, 4.8), sharex=True, sharey=True)
x1, y1, x2, y2 = 0.2, 0.2, 0.75, 0.75

bbox = dict(boxstyle="square", facecolor='w', edgecolor='k')

# subplot(131)
ax[0].annotate("relpos=(0.0, 0.0)", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", bbox=dict(boxstyle="round4", fc='w', 
				ec='k'), arrowprops=dict(arrowstyle="-|>", color='k', relpos=(0, 0), connectionstyle="arc3, rad=0.3", shrinkA=10), size=10, 
				ha="center", va='center')

ax[0].text(0.05, 0.95, "arc,\nrad=0.3", ha='left', va='top', bbox=bbox, size=12)

ax[0].set_xlim(0.0, 1.0)
ax[0].set_xticklabels([])
ax[0].set_ylim(0.0, 1.0)
ax[0].set_yticklabels([])

# subplot(132)
ax[1].annotate("relpos=(1.0, 0.0)", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", bbox=dict(boxstyle="round4", fc='w', 
				ec='k'), arrowprops=dict(arrowstyle="-|>", color='k', relpos=(1, 0), connectionstyle="arc3, rad=-0.3", shrinkA=10), size=10, 
				ha="center", va='center')

ax[1].text(0.05, 0.95, "arc,\nrad=-0.3", ha='left', va='top', bbox=bbox, size=12)

ax[1].set_xlim(0.0, 1.0)
ax[1].set_xticklabels([])
ax[1].set_ylim(0.0, 1.0)
ax[1].set_yticklabels([])

# subplot(133)
ax[2].annotate("relpos=(0.2, 0.8)", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", bbox=dict(boxstyle="round4", fc='w', 
				ec='k'), arrowprops=dict(arrowstyle="-|>", color='k', relpos=(0.2, 0.8), connectionstyle="arc3, rad=-0.3", shrinkA=10), 
				size=10, ha="center", va='center')

ax[2].text(0.05, 0.95, "arc,\nrad=-0.3", ha='left', va='top', bbox=bbox, size=12)

ax[2].set_xlim(0.0, 1.0)
ax[2].set_xticklabels([])
ax[2].set_ylim(0.0, 1.0)
ax[2].set_yticklabels([])

fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95, wspace=0.02, hspace=0.02)

plt.show()