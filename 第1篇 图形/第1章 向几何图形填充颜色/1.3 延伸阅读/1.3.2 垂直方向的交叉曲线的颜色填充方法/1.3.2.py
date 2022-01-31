import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(0, 2, 500)
x1 = np.sin(2*np.pi*y)
x2 = 1.1*np.sin(3*np.pi*y)

fig, ax = plt.subplots()

# plot x1 and plot x2
ax.plot(x1, y, color="c", lw=1, ls="-", label=r"$\sin(2\pi y)$") 
ax.plot(x2, y, color="m", lw=1, ls="-", label=r"$1.1\sin(3\pi y)$")

# "where x1 <= x2"
ax.fill_betweenx(y, x1, x2, where=x2>=x1, facecolor="cornflowerblue", alpha=0.7)	# 实现垂直方向的交叉曲线的颜色填充的目标

# "where x1 >= x2"
ax.fill_betweenx(y, x1 ,x2, where=x2<=x1, facecolor="darkred", alpha=0.7)

ax.set_xlim(-1.2, 1.2)
ax.locator_params(axis="x", nbins=5)
ax.set_ylim(0, 2)
ax.locator_params(axis="y", nbins=5)

plt.legend(loc=3)

plt.show()