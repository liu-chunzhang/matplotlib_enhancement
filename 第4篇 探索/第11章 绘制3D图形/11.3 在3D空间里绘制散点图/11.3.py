import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator

fig = plt.figure()
ax = fig.add_subplot(projection="3d")	# 教材原文中会给出警告gca函数已被弃用，如此改写不会报错

xs = np.random.rand(50)*10
ys = np.random.rand(50)*10 + 20
zs1 = np.random.rand(50)*10
zs2 = np.sqrt(xs**2 + ys**2)

ax.scatter(xs, ys, zs=zs1, zdir="z", c="cornflowerblue", marker="o", s=40, edgecolor='k')	# zs是与xs和ys数组长度相同的数组
ax.scatter(xs, ys, zs=zs2, zdir="z", c="purple", marker="^", s=40, edgecolor='k')

ax.set(xlabel="X", ylabel="Y", zlabel="Z")
ax.set_xlim(-2, 12)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.set_ylim(18, 32)
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.set_zlim(-5, 35)
ax.zaxis.set_major_locator(MultipleLocator(5))

plt.show()