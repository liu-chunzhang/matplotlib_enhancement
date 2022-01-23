import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt
import math

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

# set sample data
x = np.linspace(0, 10, 10000)
y = x*np.power(math.e, (-x**2))

plt.plot(x, y, ls="-", lw=2, color="c", alpha=0.3)

plt.xlim(0, 10)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(0.00, 0.45)
plt.yticks(np.arange(0.0, 0.46, 0.05))
plt.text(1, 0.39, r"$\mathrm{\max_{0\leq{x}\leq{10}}} xe^{-{x}^2}}$", fontsize=20)
plt.axhline(y=np.max(y), ls=":", lw=2, color="r")

plt.show()