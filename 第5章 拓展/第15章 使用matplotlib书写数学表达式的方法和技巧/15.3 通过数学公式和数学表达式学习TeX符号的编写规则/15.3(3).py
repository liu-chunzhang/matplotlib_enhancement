import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt
import math

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

# set sample data
x = np.linspace(1, 10, 10000)
y = np.power(1+1/x, x)

plt.plot(x, y, ls="-", lw=2, color="c", alpha=0.3)

plt.xlim(1, 10)
plt.xticks(np.arange(1.0, 10.1, 1.0))
plt.ylim(1.9, 2.8)
plt.yticks(np.arange(2.0, 2.9, 0.2))
plt.text(1, 2.64, r"$\mathrm{\lim_{n\to\infty}(1+\frac{1}{n})^{n}}$", fontsize=20)
plt.axhline(y=math.e, ls=":", lw=2, color="r")

plt.show()