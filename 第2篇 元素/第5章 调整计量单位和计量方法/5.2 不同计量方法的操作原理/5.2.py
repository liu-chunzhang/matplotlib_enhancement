import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

plt.rcParams["font.family"] = "stix"						# 为了消除多余的缺省字体缺失警告而添加的语句

x = np.linspace(1, 10, 1000)
y1 = [2**j for j in x]
y2 = [0.09*j for j in x]

fig, ax = plt.subplots(2, 2, figsize=(10.8, 6.8))

# linear
ax[0, 0].plot(x, y1)
ax[0, 0].set_xlim(1.0, 10.0)
ax[0, 0].xaxis.set_major_locator(MultipleLocator(1))
ax[0, 0].set_ylim(0.0, 1200.0)
ax[0, 0].yaxis.set_major_locator(MultipleLocator(200))
ax[0, 0].set_yscale("linear")

ax[0, 0].set_title("linear")

ax[0, 0].grid(True, ls="-", lw=1, color='grey')

# log
ax[0, 1].plot(x, y1)
ax[0, 1].set_xlim(1.0, 10.0)
ax[0, 1].xaxis.set_major_locator(MultipleLocator(1))
ax[0, 1].set_ylim(1e0, 1e4)
ax[0, 1].locator_params(axis='y', nbins=5)
ax[0, 1].set_yscale("log")

ax[0, 1].set_title("log")

ax[0, 1].grid(True, ls="-", lw=1, color='gray')

# logit
ax[1, 0].plot(x, y2)

ax[1, 0].set_xlim(1.0, 10.0)
ax[1, 0].xaxis.set_major_locator(MultipleLocator(1.0))
ax[1, 0].set_ylim(0.10, 0.90)
ax[1, 0].set_yscale("logit", one_half="0.5", use_overline=True)

ax[1, 0].set_title("logit")

ax[1, 0].xaxis.grid(True, ls="-", lw=1, color='gray')
ax[1, 0].axhline(0.5, linestyle='-', lw=1, color='gray')	# 为了绘制中线，添加一条水平线即可

# symlog
ax[1, 1].plot(x, y2-np.average(y2))
ax[1, 1].set_xlim(1.0, 10.0)
ax[1, 1].xaxis.set_major_locator(MultipleLocator(1))
ax[1, 1].set_ylim(-1e0, 1e0)
ax[1, 1].locator_params(axis='y', nbins=7)
ax[1, 1].set_yscale("symlog", linthresh=0.02)				# 参数linthreshy已被废弃，现应使用linthresh

ax[1, 1].set_title("symlog")

ax[1, 1].grid(True, ls="-", lw=1, color='gray')


fig.subplots_adjust(hspace=0.3, wspace=0.3)

plt.show()