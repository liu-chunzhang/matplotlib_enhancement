import matplotlib.pyplot as plt
import numpy as np

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.set_xlim(0.0, 1.0)
ax1.set_ylim(0.0, 1.0)
ax1.set_autoscale_on(False)
ax1.set_title("Click to zoom")

ax2.set_xlim(0.0, 0.4)
ax2.set_ylim(0.0, 0.4)
ax2.set_autoscale_on(False)
ax2.set_title("Zoom window")

x = np.random.rand(100)
y = np.random.rand(100)
s = np.random.rand(100)*100
c = np.random.rand(100)

ax1.scatter(x, y, s, c, edgecolor='k')
ax2.scatter(x, y, s, c, edgecolor='k')

def clicktozoom(event):
	if event.button != 1 :
		return
	x, y = event.xdata, event.ydata
	ax2.set_xlim(x-0.15, x+0.15)
	ax2.set_ylim(y-0.15, y+0.15)
	fig2.canvas.draw()

fig1.canvas.mpl_connect("button_press_event", clicktozoom)

plt.show()