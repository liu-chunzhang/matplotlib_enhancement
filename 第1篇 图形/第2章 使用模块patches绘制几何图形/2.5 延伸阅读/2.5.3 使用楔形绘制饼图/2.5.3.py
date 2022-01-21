import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Shadow, Wedge

fig, ax = plt.subplots(subplot_kw={"aspect":"equal"})

font_style = {"family":"serif", "size":12, "style":"italic", "weight":"black"}

sample_data = [350, 150, 200, 300]

total = sum(sample_data)

percents = [i/float(total) for i in sample_data]

angles = [360*i for i in percents]

delta = 45

wedge1 = Wedge((2, 2), 1, delta, delta+sum(angles[0:1]), color="orange")

wedge2 = Wedge((2, 1.9), 1, delta+sum(angles[0:1]), delta+sum(angles[0:2]), facecolor="steelblue", edgecolor='w')

wedge3 = Wedge((2, 1.9), 1, delta+sum(angles[0:2]), delta+sum(angles[0:3]), facecolor="cyan", edgecolor='w')

wedge4 = Wedge((2, 1.9), 1, delta+sum(angles[0:3]), delta+sum(angles[0:4]), facecolor="lightgreen", edgecolor='w')

wedges = [wedge1, wedge2, wedge3, wedge4]

for wedge in wedges:
	ax.add_patch(wedge)

ax.text(1.6, 2.5, "%3.1f%%" % (percents[0]*100), **font_style)
ax.text(1.1, 1.6, "%3.1f%%" % (percents[1]*100), **font_style)
ax.text(1.6, 1.2, "%3.1f%%" % (percents[2]*100), **font_style)
ax.text(2.4, 1.7, "%3.1f%%" % (percents[3]*100), **font_style)

ax.axis([0, 4, 0, 4])

plt.show()