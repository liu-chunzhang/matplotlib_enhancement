import matplotlib.pyplot as plt
import numpy as np

from basic_units import cm, inch
from matplotlib.ticker import MultipleLocator

x = np.linspace(0, 10, 6)
cm_x = [i*cm for i in x]

fig, ax = plt.subplots(2, 2)

# subplot(221)
ax[0, 0].plot(cm_x, cm_x, ls="-", lw=3, color="k", xunits=cm, yunits=cm)

ax[0, 0].set_xlim(0, 10)
ax[0, 0].set_xlabel("")
ax[0, 0].xaxis.set_major_locator(MultipleLocator(2.0))
ax[0, 0].set_ylim(0, 10)
ax[0, 0].set_ylabel("")
ax[0, 0].yaxis.set_major_locator(MultipleLocator(2.0))

# subplot(222)
ax[0, 1].plot(cm_x, cm_x, ls="--", lw=3, color="cornflowerblue", xunits=cm, yunits=inch, dashes=[2, 1.5])

ax[0, 1].set_xlabel("")
ax[0, 1].set_xlim(2.0, 8.0)
ax[0, 1].xaxis.set_major_locator(MultipleLocator(1.0))
ax[0, 1].set_ylabel("")
ax[0, 1].set_ylim(0.0, 4.0)
ax[0, 1].yaxis.set_major_locator(MultipleLocator(0.5))

# subplot(223)
ax[1, 0].plot(cm_x, cm_x, ls="-.", lw=3, color="gold", xunits=inch, yunits=cm, dashes=[1, 1, 0.5, 1])

ax[1, 0].set_xlim(0.8, 3.2)
ax[1, 0].set_xlabel("")
ax[1, 0].xaxis.set_major_locator(MultipleLocator(0.5))
ax[1, 0].set_ylabel("")
ax[1, 0].set_ylim(0.0, 10.0)
ax[1, 0].yaxis.set_major_locator(MultipleLocator(2))

# subplot(224)
ax[1, 1].plot(cm_x, cm_x, ls=":", lw=3, color="purple", xunits=inch, yunits=inch, dashes=[0.5, 0.5])

ax[1, 1].set_xlim(0.0, 4.0)
ax[1, 1].set_xlabel("")
ax[1, 1].xaxis.set_major_locator(MultipleLocator(0.5))
ax[1, 1].set_ylim(0.0, 4.0)
ax[1, 1].set_ylabel("")
ax[1, 1].yaxis.set_major_locator(MultipleLocator(0.5))

plt.show()