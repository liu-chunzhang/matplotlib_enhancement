import matplotlib.pyplot as plt
import numpy as np

from matplotlib.basic_units import radians, degrees, cos		# 此处我是将basic_units下载放置在matplotlib文件夹中

x = np.linspace(0, 9.5, 500)
rad_x = [ i*radians for i in x ]

fig, ax = plt.subplots(2, 1)

ax[0].plot(rad_x, cos(rad_x), ls="-", lw=3, color='k', xunits=radians)

ax[0].set_xlim(0, 7*np.pi/2)
ax[0].set_xlabel("")
ax[0].set_ylim(-1, 1)
ax[0].locator_params(axis="y", nbins=5)

ax[1].plot(rad_x, cos(rad_x), ls="--", color="cornflowerblue", xunits=degrees)

ax[1].set_xlim(0, 600*degrees)
ax[1].set_xlabel("")
ax[1].set_ylim(-1, 1)
ax[1].locator_params(axis="y", nbins=5)

fig.subplots_adjust(hspace=0.3)

plt.xticks(family="stix", math_fontfamily="cm")

plt.show()