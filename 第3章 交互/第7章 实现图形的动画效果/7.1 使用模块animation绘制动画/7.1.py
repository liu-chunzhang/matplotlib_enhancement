import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation			# 调用绘制动画的模块FuncAnimation
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 5000)
y = np.exp(-x) * np.cos(2*np.pi*x)
line, = ax.plot(x, y, color="cornflowerblue", lw=3)

ax.set_xlim(0.0, 7.0)
ax.xaxis.set_major_locator(MultipleLocator(1))
ax.set_ylim(-1.0, 1.0)
ax.yaxis.set_major_locator(MultipleLocator(0.5))

# to clear current frame
def init():												# 在绘制下一帧动画画面之前清空画布窗口中的当前动画画面
	line.set_ydata([np.nan]*len(x))
	return line,

# to update the data
def animate(data):										# 绘制每帧动画
	line.set_ydata(np.exp(-x)*np.cos(2*np.pi*x+float(data)/100))
	return line,

# to call class FuncAnimation which connects animate and init
ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=2, blit=True)

# to save the animation
ani.save("mymovie.mp4", fps=20, writer="ffmpeg")

plt.show()