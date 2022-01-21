import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(subplot_kw={"aspect":"equal"})

x1 = np.arange(1, 2.6, 0.1)
y1 = x1+2

x2 = np.arange(2.5, 4.1, 0.1)
y2 = -x2 + 7

# set background color
rectangle = ax.patch
rectangle.set_facecolor("lightskyblue")

# house
rectangle1 = Rectangle((1, 0), 3, 3, facecolor='w', edgecolor="rosybrown")

# door
rectangle2 = Rectangle((1.5, 0), 1, 1.5, facecolor='w', edgecolor='rosybrown', hatch="|||")

# window
rectangle3 = Rectangle((2.9, 1.7), 0.6, 0.6, facecolor='w', edgecolor='rosybrown')

# roof line
ax.plot([1, 2.5, 4], [3, 4.5, 3], color="rosybrown")

# window line
ax.plot([3.2, 3.2], [1.7, 2.3], color='rosybrown')
ax.plot([2.9, 3.5], [2.0, 2.0], color='rosybrown')

# roof filled color
# ax.fill_between(x1, 3, y1, color='r', alpha=0.5, interpolate=True, zorder=0)
# ax.fill_between(x2, 3, y2, color='r', alpha=0.5, interpolate=True, zorder=0)
x = [1, 2.5, 4.0]
y = [3, 4.5, 3]
plt.fill(x, y, color='r', alpha=0.5)

rectangle_list = [rectangle1, rectangle2, rectangle3]
for rect in rectangle_list:
	ax.add_patch(rect)

ax.axis([0, 5, 0, 6])

plt.show()