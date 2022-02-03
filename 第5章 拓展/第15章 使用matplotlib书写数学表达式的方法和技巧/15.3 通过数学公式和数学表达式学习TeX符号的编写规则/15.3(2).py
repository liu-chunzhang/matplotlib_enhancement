import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MultipleLocator

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

fig, ax = plt.subplots()

# set sample data
x = np.linspace(0, 10, 10000)
y = np.sin(x)*np.cos(x)

plt.plot(x, y, ls="-", lw=2, color="c", alpha=0.3)

plt.xlim(0, 10)
ax.xaxis.set_major_locator(MultipleLocator(2))
plt.ylim(-0.6, 0.6)
ax.yaxis.set_major_locator(MultipleLocator(0.2))

plt.text(1, 0.02, r"$\mathrm{ \bar{x}=\frac{\sum_{i=1}^{n} x_i}{n}}}$", fontsize=20)
plt.axhline(y=0, ls=":", lw=2, color="r", dashes=[1, 1])

plt.show()