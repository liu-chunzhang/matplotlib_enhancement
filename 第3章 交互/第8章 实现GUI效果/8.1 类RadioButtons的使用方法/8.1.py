import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import RadioButtons			# 从模块widgets中导入类RadioButtons，实现向画布中添加按钮的关键一步

fig, ax = plt.subplots()

x = np.linspace(0.0, 2.0, 1000)
y1 = 1.5 * np.cos(2*np.pi*x)
y2 = 1.0 * np.cos(2*np.pi*x)
y3 = 0.8 * np.cos(2*np.pi*x)

line, = ax.plot(x, y1, color='r', lw=2)

plt.subplots_adjust(left=0.35)

# a set of radiobuttons about amplitude
ax1 = plt.axes([0.1, 0.7, 0.15, 0.15], facecolor="cornflowerblue")
radio1 = RadioButtons(ax1, ("1.5 A", "1.0 A", "0.8 A"))

def amplitudefunc(label):								# 定义调整振幅的函数amplitudefunc，最后调用draw更新画布内容。下同
	hzdict = {"1.5 A":y1, "1.0 A":y2, "0.8 A": y3}
	ydata = hzdict[label]
	line.set_ydata(ydata)
	plt.draw()											# draw用在交互模式下的画布内容的更新操作的过程里

radio1.on_clicked(amplitudefunc)

# a set of radiobuttons about color
ax2 = plt.axes([0.1, 0.4, 0.15, 0.15], facecolor="cornflowerblue")
radio2 = RadioButtons(ax2, ("red", "green", "orange"))

def colorfunc(label):
	line.set_color(label)
	plt.draw()

radio2.on_clicked(colorfunc)

# a set of radiobuttons about linestyle
ax3 = plt.axes([0.1, 0.1, 0.15, 0.15], facecolor="cornflowerblue")
radio3 = RadioButtons(ax3, ("-", "--", "-.", ":"))

def linestylefunc(label):
	line.set_linestyle(label)
	plt.draw()

radio3.on_clicked(linestylefunc)

ax.set_xlim(0.0, 2.0)
ax.locator_params(axis="x", nbins=5)
ax.set_ylim(-1.5, 1.5)
ax.locator_params(axis="y", nbins=7)

plt.show()