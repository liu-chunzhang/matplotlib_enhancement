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

def clicktozoom(event):										# 设置事件处理效果，完成单击散点图中任意位置后放大展示的可视化效果
	if event.button != 1 :
		return
	x, y = event.xdata, event.ydata
	ax2.set_xlim(x-0.15, x+0.15)
	ax2.set_ylim(y-0.15, y+0.15)
	fig2.canvas.draw()

fig1.canvas.mpl_connect("button_press_event", clicktozoom)	# 将事件处理名称与事件处理效果相关联起来，从而完成特定模式的执行任务

plt.show()