import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Wedge

fig, ax = plt.subplots(subplot_kw={"aspect":"equal"})

font_style = {"family":"serif", "size":12, "style":"italic", "weight":"black"}

sample_data = [350, 150, 200, 300]
total = sum(sample_data)
percents = [i/float(total) for i in sample_data]
angles = [360*i for i in percents]

wedge1 = Wedge((2, 2), 1, 45, 45+sum(angles[0:1]), color="orange")	# 使用color会覆盖掉facecolor和edgecolor设置
wedge2 = Wedge((2, 1.9), 1, 45+sum(angles[0:1]), 45+sum(angles[0:2]), facecolor="steelblue", edgecolor='w')
wedge3 = Wedge((2, 1.9), 1, 45+sum(angles[0:2]), 45+sum(angles[0:3]), facecolor="cyan", edgecolor='w')
wedge4 = Wedge((2, 1.9), 1, 45+sum(angles[0:3]), 45+sum(angles[0:4]), facecolor="lightgreen", edgecolor='w')
wedges = [wedge1, wedge2, wedge3, wedge4]

for wedge in wedges:
	ax.add_patch(wedge)

ax.text(1.6, 2.5, "%3.1f%%" % (percents[0]*100), **font_style)
ax.text(1.1, 1.6, "%3.1f%%" % (percents[1]*100), **font_style)
ax.text(1.6, 1.2, "%3.1f%%" % (percents[2]*100), **font_style)
ax.text(2.4, 1.7, "%3.1f%%" % (percents[3]*100), **font_style)

ax.axis([0, 4, 0, 4])
ax.set_xticks([])
ax.spines["left"].set_color("none")
ax.spines["right"].set_color("none")

ax.set_yticks([])
ax.spines["top"].set_color("none")
ax.spines["bottom"].set_color("none")

plt.show()