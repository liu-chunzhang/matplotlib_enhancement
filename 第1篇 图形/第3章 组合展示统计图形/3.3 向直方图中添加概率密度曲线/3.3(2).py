# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

mpl.rcParams["font.serif"] = "Times New Roman"
mpl.rcParams["axes.unicode_minus"] = False

mu = 60.0
sigma = 2.0
x = mu + sigma*np.random.randn(500)

bins = 50

fig, ax = plt.subplots(1, 1)

n, bins, patches = ax.hist(x, bins, density=True, histtype="bar", facecolor="cornflowerblue", edgecolor="w", alpha=0.75)

y = 1/(np.power(2*np.pi, 0.5)*sigma) * np.exp(-0.5*np.power((bins-mu)/sigma, 2))

ax.plot(bins, y, color="orange", ls="--", lw=2)

ax.grid(ls=":", lw=1, color="gray", alpha=0.2)

ax.text(54, 0.2, r"$y=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma}}$", {"color":"r", "fontsize":20})
ax.set_xlim(52, 68)
ax.locator_params(axis='x', nbins=9)
ax.locator_params(axis='y', nbins=9)

ax.set_xlabel("体重", family='Fangsong',fontsize=12)
ax.set_ylabel("概率密度", family='Fangsong', fontsize=12)
ax.set_title(r"体重的直方图： $\mu=60.0$, $\sigma=2.0$", fontsize=16, family='Fangsong')

integ_x = np.linspace(mu-2*sigma, mu+2*sigma, 1000)
integ_y = 1/(np.power(2*np.pi, 0.5)*sigma) * np.exp(-0.5*np.power((integ_x-mu)/sigma, 2))
area = [(mu-2*sigma, 0), *zip(integ_x, integ_y), (mu+2*sigma, 0)]

poly = Polygon(area, facecolor="gray", edgecolor='k', alpha=0.6, closed=False)
ax.add_patch(poly)

plt.text(58.2, 0.05, r"$\int_{\mu-2\sigma}^{\mu+2\sigma} y \mathrm{d}x$", fontsize=20)

plt.show()