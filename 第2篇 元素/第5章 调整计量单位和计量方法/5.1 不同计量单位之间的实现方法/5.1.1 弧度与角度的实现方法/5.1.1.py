import matplotlib.pyplot as plt
import numpy as np

from basic_units import radians, degrees, cos

x = np.linspace(0, 9.5, 500)
rad_x = [ i*radians for i in x ]

fig, ax = plt.subplots(2, 1)

ax[0].plot(rad_x, cos(rad_x), ls="-", lw=3, color='k', xunits=radians)
ax[0].set_xlabel("")
ax[0].margins(0.0, 0.0)
ax[0].locator_params(axis="y", nbins=5)
ax[1].locator_params(axis='x', nbins=25)

ax[1].plot(rad_x, cos(rad_x), ls="--", color="cornflowerblue", xunits=degrees)
ax[1].set_xlabel("")
ax[1].margins(0, 0)
ax[1].locator_params(axis='x', nbins=8)
ax[1].locator_params(axis="y", nbins=5)

fig.subplots_adjust(hspace=0.3)

plt.show()