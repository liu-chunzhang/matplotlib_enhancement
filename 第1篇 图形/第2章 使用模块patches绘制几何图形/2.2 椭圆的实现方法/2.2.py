import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(1, 2, subplot_kw={"aspect":"equal"})

# subplot(121)
angles = np.linspace(0, 135, 4)
ellipse = [Ellipse((2, 2), 4, 2, a) for a in angles]	# Ellipse的构造函数的参数分别为中心，长轴长，短轴长，中心逆时针旋转角

for elle in ellipse:
	ax[0].add_patch(elle)
	elle.set_alpha(0.4)
	elle.set_color("cornflowerblue")

ax[0].axis([-1, 5, -1, 5])
ax[0].xaxis.set_major_locator(MultipleLocator(1))
ax[0].yaxis.set_major_locator(MultipleLocator(1))

# subplot(122)
num = np.arange(0, 100, 1)
ellipse = [Ellipse(xy=np.random.rand(2)*10, width=np.random.rand(1), height=np.random.rand(1), angle=np.random.rand(1)*360) for i in num]

for elle in ellipse:
	ax[1].add_patch(elle)
	elle.set_alpha(float(np.random.rand(1)))
	elle.set_color(np.random.rand(3))

ax[1].axis([-1, 11, -1, 11])
ax[1].xaxis.set_major_locator(MultipleLocator(2))
ax[1].yaxis.set_major_locator(MultipleLocator(2))

plt.tight_layout()		# 自动调整子图系统，使之填充整个图像区域

plt.show()