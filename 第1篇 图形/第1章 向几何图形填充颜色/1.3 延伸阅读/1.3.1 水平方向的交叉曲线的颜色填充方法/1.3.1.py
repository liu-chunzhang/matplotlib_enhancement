import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 500)
y1 = np.sin(2*np.pi*x)
y2 = 1.1 * np.sin(3*np.pi*x)

fig = plt.figure()

ax = fig.add_subplot(111)

# plot y1 and plot y2
ax.plot(x, y1, color="c", lw=1, ls="-", label=r"$y_1=\sin(2\pi x)$")
ax.plot(x, y2, color="y", lw=1, ls="-", label=r"$y_2=1.1\sin(3\pi x)$")

# "where y1 <= y2"
ax.fill_between(x, y1, y2, where=y2>=y1, interpolate=True, facecolor="cornflowerblue", alpha=0.7)

# "where y1 >= y2"
ax.fill_between(x, y1, y2, where=y2<=y1, interpolate=True, facecolor="darkred", alpha=0.7)

ax.set_xlim(0, 2)
ax.set_ylim(-1.2, 1.2)

ax.grid(ls=":", lw=1, color="gray", alpha=0.5)

ax.legend(loc="lower left")
ax.locator_params(axis="x", tight=True,nbins=5)

plt.show()