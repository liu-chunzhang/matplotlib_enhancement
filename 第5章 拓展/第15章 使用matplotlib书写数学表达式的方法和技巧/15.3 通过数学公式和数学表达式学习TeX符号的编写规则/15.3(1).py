import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

# set sample data
x = np.linspace(0, 10, 10000)
y = np.power(np.sin(x), 2) + np.power(np.cos(x), 2)

plt.plot(x, y, ls="-", lw=2, color="c", alpha=0.3)

plt.xlim(0, 10)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(0.94, 1.06)
plt.yticks(np.arange(0.94, 1.07, 0.02))
plt.text(1, 1.01, r"$\sin^2\alpha + \cos^2 \alpha=1$", fontsize=20)

plt.show()