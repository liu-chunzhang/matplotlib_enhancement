import matplotlib.pyplot as plt
import numpy as np

from basic_units import cm, inch

x = np.linspace(0, 10, 6)
cm_x = [i*cm for i in x]

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(cm_x, cm_x, ls="-", lw=3, color="k", xunits=cm, yunits=cm)
ax[0, 0].set_xlabel("")
ax[0, 0].set_ylabel("")
ax[0, 0].margins(0, 0)
ax[0, 0].locator_params(axis='both', nbins=5)

ax[0, 1].plot(cm_x, cm_x, ls="--", lw=3, color="cornflowerblue", xunits=cm, yunits=inch, dashes=[2, 1])
ax[0, 1].set_xlabel("")
ax[0, 1].set_xlim(2.0, 8.0)
ax[0, 1].set_ylabel("")
ax[0, 1].set_ylim(0.0, 4.0)
ax[0, 1].margins(0, 0)
ax[0, 1].locator_params(axis='both', nbins=8)

ax[1, 0].plot(cm_x, cm_x, ls="-.", lw=3, color="gold", xunits=inch, yunits=cm)

ax[1, 0].set_xlabel("")
ax[1, 0].set_xlim(0.8, 3.2)
ax[1, 0].set_ylabel("")
ax[1, 0].set_ylim(0.0, 10.0)
ax[1, 0].margins(0, 0)
ax[1, 0].locator_params(axis='both', nbins=5)

ax[1, 1].plot(cm_x, cm_x, ls=":", lw=3, color="purple", xunits=inch, yunits=inch)
ax[1, 1].set_xlabel("")
ax[1, 1].set_xlim(0.0, 4.0)
ax[1, 1].set_ylabel("")
ax[1, 1].set_ylim(0.0, 4.0)
ax[1, 1].margins(0, 0)
ax[1, 1].locator_params(axis='both', nbins=8)

plt.show()