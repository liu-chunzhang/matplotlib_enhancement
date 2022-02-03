import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib.ticker import MultipleLocator

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

fig, ax = plt.subplots()

# set sample data
x = np.linspace(1, 10, 10000)
y = np.power(1+1/x, x)

plt.plot(x, y, ls="-", lw=2, color="c", alpha=0.3)

plt.xlim(1, 10)
ax.xaxis.set_major_locator(MultipleLocator(1))
plt.ylim(1.9, 2.8)
ax.yaxis.set_major_locator(MultipleLocator(0.2))

plt.text(1, 2.64, r"$\mathrm{\lim_{n\to\infty}(1+\frac{1}{n})^{n}}$", fontsize=20)
plt.axhline(y=math.e, ls=":", lw=2, color="r")

plt.show()