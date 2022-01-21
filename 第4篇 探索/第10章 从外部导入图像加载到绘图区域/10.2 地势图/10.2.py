import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import get_sample_data
from matplotlib.colors import LightSource

fontstyle = dict(fontsize=25, weight="bold", family="serif")

filePath = get_sample_data("jacksboro_fault_dem.npz", asfileobj=False)

with np.load(filePath) as jfdem:
	elev = jfdem["elevation"]

fig, ax = plt.subplots(1, 2)

ls = LightSource(azdeg=315, altdeg=45)

ai1 = ax[0].imshow(elev, cmap=plt.cm.gist_earth)
fig.colorbar(ai1, ax=ax[0], orientation="horizontal")

rgba = ls.shade(elev, cmap=plt.cm.gist_earth, vert_exag=0.05, blend_mode="soft")

ai2 = ax[1].imshow(rgba)
fig.colorbar(ai1, ax=ax[1], orientation="horizontal")

fig.suptitle("shaded relief plot blending with 'soft'", y=0.92, **fontstyle)

plt.show()