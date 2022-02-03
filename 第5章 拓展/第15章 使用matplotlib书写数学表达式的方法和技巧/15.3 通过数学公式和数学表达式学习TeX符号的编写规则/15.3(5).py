import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib.ticker import MultipleLocator

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

fig, ax = plt.subplots()

# set sample data
x = np.linspace(0.5, 16, 100)
y = np.array([math.log(value, 2) for value in x])

plt.plot(x, y, ls="-", lw=2, color="r", alpha=0.3)

plt.xlim(0, 16)
ax.xaxis.set_major_locator(MultipleLocator(2))
plt.ylim(-1.0, 4.0)
ax.yaxis.set_major_locator(MultipleLocator(1))

plt.text(4.0, 1.6, r"$\mathrm{\log_{2}{x}}$", fontsize=20)
plt.axhline(y=1, ls=":", lw=2, color='c')
plt.axvline(x=2, ls=":", lw=2, color='c')

plt.show()