import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib.ticker import MultipleLocator

mpl.rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})

fig, ax = plt.subplots(figsize=(8, 6.4))

# set sample data
x = np.linspace(0.5, 16, 100)
y = [math.log(value, math.e) for value in x]				# due to lack of latex, it doesn't work.

plt.plot(x, y, ls="-", lw=2, color="r", alpha=0.3)
#plt.text(4.0, 2.1, r"$\mathrm{ \begin{pmatrix} \ln{e^{2}} & 2 \\ 1 & \ln{e} \end{pmatrix}}$", fontsize=20)
plt.text(12.0, 2.3, r"$\mathrm{y=\ln{x}}$", fontsize=20)
# (e, 1)
plt.axhline(y=1, ls=":", lw=1, color='c')
plt.axvline(x=math.e, ls=":", lw=1, color='c')

# (e^2, 1)
plt.axhline(y=2, ls=":", lw=1, color='c')
plt.axvline(x=(math.e)**2, ls=":", lw=1, color='c')

plt.xlim(0, 16)
ax.xaxis.set_major_locator(MultipleLocator(2))
plt.ylim(-1.0, 3.0)
ax.yaxis.set_major_locator(MultipleLocator(0.5))

plt.show()