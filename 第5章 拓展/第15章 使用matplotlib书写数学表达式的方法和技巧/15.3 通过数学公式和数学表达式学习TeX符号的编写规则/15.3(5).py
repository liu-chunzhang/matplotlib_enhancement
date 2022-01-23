import matplotlib as mpl
import numpy as np

import matplotlib.pyplot as plt
import math

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

# set sample data
x = np.linspace(0.5, 16, 100)
y = np.array([math.log(value, 2) for value in x])

plt.plot(x, y, ls="-", lw=2, color="r", alpha=0.3)
plt.text(4.0, 1.6, r"$\mathrm{\log_{2}{x}}$", fontsize=20)
plt.axhline(y=1, ls=":", lw=2, color='c')
plt.axvline(x=2, ls=":", lw=2, color='c')

plt.xlim(0, 16)
plt.xticks(np.arange(0.0, 16.1, 2.0))
plt.ylim(-1.0, 4.0)
plt.yticks(np.arange(-1.0, 4.1))

plt.show()