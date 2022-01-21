import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt

from matplotlib import rc, rcParams

rcParams["text.usetex"] = True

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Times New Roman"

# set sample data
x = np.linspace(0, 10, 10000)
y = np.sin(x) * np.cos(x)

plt.plot(x, y, ls="-", lw=2, color="c", alpha=0.3)

plt.text(1.5, 0.02, r"\bar{x} = \frac{1}{n}{\sum_{i=1}^n x_i}", fontsize=20)
plt.axhline(y=0, ls=":", lw=2, color="r")

plt.show()