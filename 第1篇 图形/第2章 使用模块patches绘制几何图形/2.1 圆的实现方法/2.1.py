import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(2, 2)

# subplot(211)
circle = Circle((2, 2), radius=2, facecolor="w", edgecolor="cornflowerblue")
ax[0, 0].add_patch(circle)

ax[0, 0].set_xlim(-1, 5)
ax[0, 0].locator_params(axis='x', nbins=7)
ax[0, 0].set_ylim(-1, 5)
ax[0, 0].locator_params(axis='y', nbins=7)

# sublot(222)
rectangle = ax[0, 1].patch
rectangle.set_facecolor("gold")

circle = Circle((2, 2), radius=2, facecolor="w", edgecolor="cornflowerblue")
ax[0, 1].add_patch(circle)						# 将圆片的patch加到ax[0, 1]中

ax[0, 1].set_xlim(-1, 5)
ax[0, 1].locator_params(axis='x', nbins=7)
ax[0, 1].set_ylim(-1, 5)
ax[0, 1].locator_params(axis='y', nbins=7)

ax[0, 1].set_aspect("equal", "box")				# 控制y轴与x轴的长度比（但不是显示刻度长比）

# subplot(223)
rectangle = ax[1, 0].patch
rectangle.set_facecolor("palegreen")

circle = Circle((2, 2), radius=2, facecolor="w", edgecolor="cornflowerblue")
ax[1, 0].add_patch(circle)

ax[1, 0].axis("equal")
ax[1 ,0].xaxis.set_major_locator(MultipleLocator(1.0))
ax[1, 0].set_ylim(0.0, 4.0)
ax[1, 0].locator_params(axis="y", nbins=9)

# subplot(224)
rectangle = ax[1, 1].patch
rectangle.set_facecolor("lightskyblue")

circle = Circle((2, 2), radius=2, facecolor="w", edgecolor="cornflowerblue")
ax[1, 1].add_patch(circle)

#ax[1, 1].axis([-1, 5, -1, 5])		# 这个语句实际上不该起作用
ax[1, 1].axis("equal")

ax[1, 1].xaxis.set_major_locator(MultipleLocator(1.0))
ax[1, 1].set_ylim(0, 4)
ax[1, 1].yaxis.set_major_locator(MultipleLocator(1.0))

plt.subplots_adjust(left=0.1)

plt.show()