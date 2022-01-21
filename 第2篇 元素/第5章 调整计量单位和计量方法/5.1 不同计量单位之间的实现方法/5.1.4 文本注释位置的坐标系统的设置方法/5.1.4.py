import matplotlib.pyplot as plt
from basic_units import cm
from matplotlib.patches import Ellipse

fig, ax = plt.subplots(1, 1)

font_style = {"family":"monospace", "fontsize":15, "weight":"bold"}

ellipse = Ellipse((2*cm, 1*cm), 0.05*cm, 0.05*cm, color="blue")

ax.add_patch(ellipse)

ax.annotate("fancy", xy=(2*cm, 1*cm), xycoords="data", xytext=(0.8*cm, 0.85*cm), textcoords="data", bbox=dict(boxstyle="round", fc='w', 
				ec='k'), arrowprops=dict(arrowstyle="fancy, head_length=0.4, head_width=0.4, tail_width=0.6", fc='gray', 
				connectionstyle='arc3, rad=0.3', shrinkA=5, patchB=ellipse, shrinkB=5), ha='right', va='top', **font_style)

ax.annotate("fancy", xy=(2*cm, 1*cm), xycoords="data", xytext=(0.95, 0.83), textcoords="axes fraction", bbox=dict(boxstyle="round", fc='w', 
				ec='k'), arrowprops=dict(arrowstyle="fancy, head_length=0.4, head_width=0.4, tail_width=0.6", fc='gray',
				connectionstyle='arc3, rad=0.4', shrinkA=5, patchB=ellipse, shrinkB=5), ha='right', va='top', **font_style)

ax.set_xlim(0*cm, 3*cm)
ax.set_ylim(0*cm, 3*cm)

plt.show()