import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 500)
y1 = np.sin(2*np.pi*x)
y2 = 1.1 * np.sin(3*np.pi*x)

fig, ax = plt.subplots(figsize=(12, 4.8))

# plot y1 and plot y2
ax.plot(x, y1, color="c", lw=1, ls="-", label=r"$y_1=\sin(2\pi x)$")		# 只是用来绘制填充区域的轮廓曲线，标记出不同填充区域的颜色内容
ax.plot(x, y2, color="y", lw=1, ls="-", label=r"$y_2=1.1\sin(3\pi x)$")

# "where y1 <= y2"
ax.fill_between(x, y1, y2, where=y2>=y1, interpolate=True, facecolor="cornflowerblue", alpha=0.7)

# "where y1 >= y2"
ax.fill_between(x, y1, y2, where=y2<=y1, interpolate=True, facecolor="darkred", alpha=0.7)

ax.set_xlim(0, 2)
ax.locator_params(axis="x", nbins=5)
ax.set_ylim(-1.2, 1.2)
ax.locator_params(axis="y", nbins=5)

ax.grid(ls=":", lw=1, color="gray", alpha=0.5)

ax.legend(loc="lower left")

plt.show()