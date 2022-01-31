import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle, Ellipse
from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(subplot_kw={"aspect":"equal"})

angles = np.linspace(0, 135, 4)

circle = Circle((2, 2), radius=1)							# 实际上，这个圆补片被后面的椭圆补片完全覆盖了
ellipse = [Ellipse((2, 2), 2, 2, a) for a in angles]
ellipse.append(circle)

for pln in ellipse:
	pln.set_alpha(float(np.random.rand(1)))					# 此处必须使用float转型，否则将报错！
	pln.set_color(np.random.rand(3))
	ax.add_patch(pln)

ax.axis([0, 4, 0 ,4])
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))

plt.show()