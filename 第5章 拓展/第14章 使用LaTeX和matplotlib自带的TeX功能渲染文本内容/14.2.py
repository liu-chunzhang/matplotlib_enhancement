import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib import font_manager
from matplotlib import rc, rcParams
#import matplotlib.dviread as dvi 

print(mpl.get_cachedir())

#rcParams["text.latex.preamble"] = [r"\usepackage{amsmath}"]
rc('text', usetex=True)
#dvi.find_tex_file("/home/lcz/anaconda3/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/tfm/cmss10.tfm", 'tfm')

# sample data
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4*np.pi*t)/2

# plot figure
plt.plot(t, s, ls="-", lw=0.5, c="b")

# No.5 text
plt.text(0.2, 1.2, r"$\forall\ i, \exists\ \alpha_i\geq\beta_i, \sqrt{\alpha_i-\beta_i}\geq{0}$", fontsize=24)

plt.ylim(-0.5, 1.5)

plt.show()