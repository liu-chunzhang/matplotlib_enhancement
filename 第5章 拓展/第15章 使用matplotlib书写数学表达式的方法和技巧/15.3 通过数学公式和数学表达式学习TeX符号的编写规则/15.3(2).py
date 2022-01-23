import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

# set sample data
x = np.linspace(0, 10, 10000)
y = np.sin(x)*np.cos(x)

plt.plot(x, y, ls="-", lw=2, color="c", alpha=0.3)

plt.xlim(0, 10)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(-0.6, 0.6)
plt.yticks(np.arange(-0.6, 0.7, 0.2))
plt.text(1, 0.02, r"$\mathrm{ \bar{x}=\frac{\sum_{i=1}^{n} x_i}{n}}}$", fontsize=20)
plt.axhline(y=0, ls=":", lw=2, color="r")

plt.show()