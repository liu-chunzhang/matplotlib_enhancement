import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 1000)
y1 = [2**j for j in x]
y2 = [0.09*j for j in x]

fig, ax = plt.subplots(2, 2)

# linear
ax[0, 0].plot(x, y1)
ax[0, 0].set_xlim(1.0, 10.0)
ax[0, 0].locator_params(axis='x', nbins=9)
ax[0, 0].set_ylim(0.0, 1200.0)
ax[0, 0].locator_params(axis='y', nbins=6)
ax[0, 0].set_yscale("linear")
ax[0, 0].set_title("linear")
ax[0, 0].grid(True, ls="-", lw=1, color='grey')

# log
ax[0, 1].plot(x, y1)
ax[0, 1].set_xlim(1.0, 10.0)
ax[0, 1].locator_params(axis='x', nbins=9)
ax[0, 1].set_ylim(1e0, 1e4)
ax[0, 1].locator_params(axis='y', nbins=5)
ax[0, 1].set_yscale("log")
ax[0, 1].set_title("log")
ax[0, 1].grid(True, ls="-", lw=1, color='gray')

# logit
ax[1, 0].plot(x, y2)
ax[1, 0].set_xlim(1.0, 10.0)
ax[1, 0].locator_params(axis='x', nbins=9)
ax[1, 0].set_ylim(0.10, 0.90)
ax[1, 0].locator_params(axis='y', nbins=25)
ax[1, 0].set_yscale("logit")
ax[1, 0].set_title("logit")
ax[1, 0].grid(True, ls="-", lw=1, color='gray')

# symlog
ax[1, 1].plot(x, y2-np.average(y2))
ax[1, 1].set_xlim(1.0, 10.0)
ax[1, 1].locator_params(axis='x', nbins=9)
ax[1, 1].set_ylim(-1e0, 1e0)
ax[1, 1].locator_params(axis='y', nbins=7)
ax[1, 1].set_yscale("symlog", linthresh=0.02)
ax[1, 1].set_title("symlog")
ax[1, 1].grid(True, ls="-", lw=1, color='gray')

fig.subplots_adjust(hspace=0.3, wspace=0.3)

plt.show()