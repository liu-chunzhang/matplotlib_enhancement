import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator, NullFormatter, FixedLocator

fig, ax = plt.subplots(3, 1, figsize=(8, 6))

# subplot(311)
majorLocator = MultipleLocator(1.5)
majorFormatter = FormatStrFormatter("%1.1f")
minorLocator = MultipleLocator(0.5)
minorFormatter = NullFormatter()

x = np.linspace(0, 2*np.pi, 500)
y = np.cos(2*np.pi*x) * np.exp(-x)

ax[0].plot(x, y, lw=3, color="cornflowerblue")

ax[0].xaxis.set_major_locator(majorLocator)
ax[0].xaxis.set_major_formatter(majorFormatter)
ax[0].set_xlim(0.0, 7.0)
ax[0].set_ylim(-0.8, 1.0)
ax[0].locator_params(axis='y', nbins=11)

# subplot(312)
minorLocator = AutoMinorLocator()

ax[1].plot(x, y, lw=3, color="cornflowerblue")

ax[1].xaxis.set_minor_locator(minorLocator)
ax[1].set_xlim(0.0, 7.0)
ax[1].tick_params(axis='x', which='major', length=6, width=1.5)
ax[1].tick_params(axis='x', which='minor', length=4, width=1, color='r')
ax[1].set_ylim(-0.8, 1.0)
ax[1].locator_params(axis='y', nbins=11)

# subplot(313)
majorLocator = FixedLocator([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
minorLocator = AutoMinorLocator(2)

ax[2].plot(x, y, lw=3, color="cornflowerblue")

ax[2].xaxis.set_major_locator(majorLocator)
ax[2].xaxis.set_minor_locator(minorLocator)
ax[2].set_xlim(0.0, 7.0)
ax[2].tick_params(axis='x', which='major', length=6, width=1.5)
ax[2].tick_params(axis='x', which='minor', length=4, width=1, color='r')
ax[2].set_xticklabels(["0", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
ax[2].set_ylim(-0.8, 1.0)
ax[2].locator_params(axis='y', nbins=11)

plt.show()