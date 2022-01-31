# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Polygon												# 用于绘制不规则多边形
from matplotlib.ticker import MultipleLocator

mpl.rcParams["font.serif"] = "Fangsong"
mpl.rcParams["axes.unicode_minus"] = False

x = np.random.normal(60, 2.0, 1500)		# 直接用非标准正态分布函数，略去mu和sigma，下同
bins = 50

fig, ax = plt.subplots()

n, bins, patches = ax.hist(x, bins, density=True, histtype="bar", facecolor="cornflowerblue", edgecolor="w", alpha=0.75)

y = 1/(np.power(2*np.pi, 0.5)*2.0) * np.exp(-0.5*np.power((bins-60)/2.0, 2))

ax.plot(bins, y, color="orange", ls="--", lw=2)

ax.set_xlim(52, 66)
plt.xticks(family="serif", fontsize=11)
ax.xaxis.set_major_locator(MultipleLocator(2.0))
ax.set_ylim(0.00, 0.25)
plt.yticks(family="serif", fontsize=11)
ax.yaxis.set_major_locator(MultipleLocator(0.05))

ax.text(53, 0.18, r"$y=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$", {"color":"r", "fontsize":20, "math_fontfamily":"cm"})
ax.set_xlabel("体重", family='Fangsong',fontsize=12)
ax.set_ylabel("概率密度", family='Fangsong', fontsize=12)
ax.set_title(r"体重的直方图： $\mu=60.0$, $\sigma=2.0$", fontsize=16, family='Fangsong', math_fontfamily="cm")

integ_x = np.linspace(60-2*2, 60+2*2, 1000)													# 开始绘制不规则多边形
integ_y = 1/(np.power(2*np.pi, 0.5)*2) * np.exp(-0.5*np.power((integ_x-60)/2.0, 2))
area = [(60-2*2, 0), *zip(integ_x, integ_y), (60+2*2, 0)]

poly = Polygon(area, facecolor="gray", edgecolor='k', alpha=0.6, closed=False)
ax.add_patch(poly)

plt.text(58.2, 0.05, r"$\int_{\mu-2\sigma}^{\mu+2\sigma} y \mathrm{d}x$", fontsize=20, math_fontfamily="cm")

ax.grid(ls=":", lw=1, color="gray", alpha=0.2)

plt.show()