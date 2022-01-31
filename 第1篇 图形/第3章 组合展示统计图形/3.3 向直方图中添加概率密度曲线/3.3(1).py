# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

mpl.rcParams["font.serif"] = ['Fangsong']
mpl.rcParams["axes.unicode_minus"] = False

mu, sigma = 60.0, 2.0
x = mu + sigma*np.random.randn(2000)	# 变相使用均值为500,方差为2.0的正态分布
bins = 50

fig, ax = plt.subplots(figsize=(7.2, 4.8))

n, bins, patches = ax.hist(x, bins, density=True, histtype="bar", facecolor="cornflowerblue", edgecolor="w", alpha=0.75) # 注意此处用的是density

y = 1/(np.power(2*np.pi, 0.5)*sigma) * np.exp(-0.5*np.power((bins-mu)/sigma, 2))

ax.plot(bins, y, color="orange", ls="--", lw=2)

ax.set_xlim(52, 68)
ax.xaxis.set_major_locator(MultipleLocator(2.0))
ax.set_xlabel("体重", family='Fangsong',fontsize=12, y=-0.1)
ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.set_ylabel("概率密度", family='Fangsong', fontsize=12, math_fontfamily="cm")

ax.grid(ls=":", lw=1, color="gray", alpha=0.2)

ax.set_title(r"体重的直方图： $\mu=60.0$, $\sigma=2.0$", fontsize=16, family='Fangsong', math_fontfamily="cm")
ax.text(53, 0.18, r"$y=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$", {"color":"r", "fontsize":18, "math_fontfamily":"cm"})

plt.xticks(family="serif", fontsize=11)
plt.yticks(family="serif", fontsize=11)

plt.show()