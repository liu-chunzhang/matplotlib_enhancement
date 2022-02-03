import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc, rcParams

rc("mathtext", **{"fontset":"cm", "it":"italic", "rm":"times"})
rc("font", **{"family": "serif", "serif":["Helvetica"], "size":16})

fig = plt.figure(figsize=(8, 6.4))

# sample data
t = np.linspace(0.0, 1.0, 100)
s = np.cos(4*np.pi*t)+2

# plot figure
plt.plot(t, s, ls="-", lw=0.5, c="b")

# No.1 text
plt.text(0.2, 2.8, r"$some\ ranges:(\alpha), [\beta],\{\gamma\}, |\Gamma|, \Vert\phi\Vert, \langle\Phi\rangle $")

# No.2 text
# these went wrong in pdf in a previous version
plt.text(0.2, 2.5, r"gamma: $\gamma$", {"color":"r", "fontsize":20})
plt.text(0.2, 2.3, r"Omega: $\Omega$", {"color":"r", "fontsize":20})

# No.3 text
plt.text(0.2, 2.0, r"$\lim_{i\to\infty}\cos(2\pi)\times\exp\{-i\}=0$", **{"family": "Times New Roman"})

# No.4 text
plt.text(0.2, 1.5, r"$\mathrm{math\ equation}:\frac{n!}{(n-k)!}=\binom{n}{k}$", {"color":"c", "fontsize":20})

# No.5 text
plt.text(0.2, 1.2, r"$\forall\ i, \exists\ \alpha_i\geq\beta_i, \sqrt{\alpha_i-\beta_i}\geq{0}$")

# We can write labels with LaTeX
plt.xlabel(r"time(s)$")
plt.ylabel(r"Velocity(m/s)")

# and also write title with LaTeX
plt.annotate(r"$\cos(4\times\pi\times{t})+2$", xy=(0.87, 2.0), xytext=(0.65, 2.3), color='r', arrowprops={"arrowstyle":"->", "color":"r"})

plt.xlim(0.0, 1.0)
plt.locator_params(axis='x', nbins=6)
plt.ylim(1.0, 3.0)
plt.locator_params(axis='y', nbins=5)

plt.subplots_adjust(top=0.8)

plt.show()