import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import MultipleLocator

plt.rcParams["mathtext.fontset"] = 'cm'
plt.rcParams["font.style"] = "normal"

fig, ax = plt.subplots(figsize=(8, 6.4))

# set sample data
x = np.linspace(0, 10, 10000)
y = np.sin(x)*np.cos(x)

plt.plot(x, y, ls="-", color='c', alpha=0.3)

plt.text(1.0, 0.5, r"\mathrm{Roman}:$\mathrm{Roman}\/(1st)$", fontsize=15)
plt.text(1.0, 0.4, r"\mathit{Italic}:$\mathit{Italic}\/(2nd)$", fontsize=15)
plt.text(1.0, 0.3, r"\mathtt{Typewriter}:$\mathtt{Typewriter}\/(3rd)$", fontsize=15)
plt.text(1.0, 0.2, r"\mathcal{CALLIGRAPHY}:$\mathcal{CALLIGRAPHY}\/(4th)$", fontsize=15)
plt.text(1.0, 0.1, r"\mathbb{blackboard}:$\mathbb{blackboard}\/(5th)$", fontsize=15)
plt.text(1.0, 0.0, r"\mathfrak{Fraktur}:$\mathfrak{Fraktur}\/(6th)$", fontsize=15)
plt.text(1.0, -0.1, r"\mathsf{sansserif}:$\mathsf{sansserif}\/(7th)$", fontsize=15)
#plt.text(1.0, -0.2, r"\mathcircled{circled}:$\mathcircled{circled}\/(8th)$", fontsize=15)		# it cannot work.
																								# 该命令在3.3.0版本已被移除，应使用Unicode代替！
plt.text(1.0, -0.3, r"\mathrm{\mathbb{blackboard}}:$\mathrm{\mathbb{blackboard}}\/(9th)$", fontsize=15)

plt.xlim(0.0, 10.0)
ax.xaxis.set_major_locator(MultipleLocator(2.0))
plt.ylim(-0.6, 0.6)
ax.yaxis.set_major_locator(MultipleLocator(0.2))

plt.show()