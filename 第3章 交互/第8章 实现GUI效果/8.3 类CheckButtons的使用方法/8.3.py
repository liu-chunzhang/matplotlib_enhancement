import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import CheckButtons

x = np.linspace(0.0, 2.0, 1000)
y1 = 1.2 * np.cos(2*np.pi*x)
y2 = 1.0 * np.cos(2*np.pi*x)
y3 = 0.8 * np.cos(2*np.pi*x)

fig, ax = plt.subplots()
line1, = ax.plot(x, y1, color="red", lw=2, visible=False, label="1.2 A")
line2, = ax.plot(x, y2, color="green", lw=2, label="1.0 A")
line3, = ax.plot(x, y3, color="orange", lw=2, label="0.8 A")
plt.subplots_adjust(left=0.30)

axesbgcolor = "cornflowerblue"

cax = plt.axes([0.1, 0.4, 0.1, 0.15], facecolor=axesbgcolor)

lines = [line1, line2, line3]

labels = [str(line.get_label()) for line in lines]
visibility = [line.get_visible() for line in lines]
check = CheckButtons(cax, labels, visibility)

def func(label):
	index = labels.index(label)
	lines[index].set_visible(not lines[index].get_visible())
	plt.draw()

check.on_clicked(func)

ax.set_xlim(0.0, 2.0)
ax.locator_params(axis="x", nbins=5)
ax.set_ylim(-1.5, 1.5)
ax.locator_params(axis="y", nbins=7)

plt.show()