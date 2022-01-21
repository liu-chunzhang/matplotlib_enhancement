import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 2)

# subplot(121) data
x = np.linspace(0, 2, 500)
y1 = np.sin(2*np.pi*x)
y2 = 1.2 * np.sin(3*np.pi*x)

y2 = np.ma.masked_greater(y2, 1.0)

# plot y1 and plot y2
ax[0].plot(x, y1, color="r", lw=1, ls="-", label="y1")
ax[0].plot(x, y2, color="b", lw=1, ls="-", label="y2")

# "where y1 >= y2"
ax[0].fill_between(x, y1, y2, where=y2>=y1, facecolor="cornflowerblue", alpha=0.7)

# "where y1 <= y2"
ax[0].fill_between(x, y1, y2, where=y2<=y1, facecolor="darkred", alpha=0.7)

ax[0].set_xlim(0, 2)
ax[0].set_ylim(-1.2, 1.2)

ax[0].grid(ls=":", lw=1, color="gray", alpha=0.5)
ax[0].legend(loc="upper left", ncol=2, mode="expand")
ax[0].locator_params(axis="x", tight=True, nbins=5)

# subplot(122) data
y = np.linspace(0, 2, 500)
x1 = np.sin(2*np.pi*y)
x2 = 1.2 * np.sin(3*np.pi*y)

# plot x1 and plot x2
ax[1].plot(x1, y, color="r", lw=1, ls="-", label="x1")
ax[1].plot(x2, y, color="b", lw=1, ls="-", label="x2")

# "where x1 <= x2"
ax[1].fill_betweenx(y, x1, x2, where=x2>=x1, facecolor="cornflowerblue", alpha=0.7)

# "where x1 >= x2"
ax[1].fill_betweenx(y, x1, x2, where=x2<=x1, facecolor="darkred", alpha=0.7)

ax[1].set_ylim(0, 2)
ax[1].set_xlim(-1.2, 1.2)

ax[1].grid(ls=":", lw=1, color="gray", alpha=0.5)
ax[1].legend(loc="lower left")
ax[1].locator_params(axis="y", tight=True, nbins=5)

plt.show()