import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(1, 1)

x = np.linspace(0, 2*np.pi, 5000)
y = np.exp(-x) * np.cos(2*np.pi*x)
line, = ax.plot(x, y, color="cornflowerblue", lw=3)
ax.set_xlim(0.0, 7.0)
ax.set_ylim(-1.0, 1.0)

# to clear current frame
def init():
	line.set_ydata([np.nan]*len(x))
	return line,

# to update the data
def animate(data):
	line.set_ydata(np.exp(-x)*np.cos(2*np.pi*x+float(data)/100))
	return line,

# to call class FuncAnimation which connects animate and init
ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=2, blit=True)

# to save the animation
ani.save("mymovie.mp4", fps=20, writer="ffmpeg")

plt.show()