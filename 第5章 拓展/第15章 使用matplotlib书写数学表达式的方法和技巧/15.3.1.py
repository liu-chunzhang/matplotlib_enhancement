import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt

# set sample data
x = np.linspace(0, 10, 10000)
y = np.power(np.sin(x), 2) + np.power(np.cos(x), 2)

plt.plot(x, y, ls="-", lw=2, c="c", alpha=0.3)

plt.text(1, 1.01, r"$\sin^2\alpha+\cos^2\alpha=1$", fontsize=20)

plt.show()