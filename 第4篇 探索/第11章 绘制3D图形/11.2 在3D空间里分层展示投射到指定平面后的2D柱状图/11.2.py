import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MultipleLocator

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

colorList = ["y", "b", "r"]
yLayersList = [0, 1, 2]

for color, layer in zip(colorList, yLayersList):
	x = np.arange(10)
	y = np.random.rand(10)
	ax.bar(x, y, zs=layer, zdir="y", color=color, alpha=0.7, edgecolor='k')	# zdir='y'设置在与z轴平行的平面绘制2D柱状图

ax.set(xlabel="X", ylabel="Y", zlabel="Z", yticks=yLayersList)
ax.set_xlim(0, 10)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.set_ylim(0, 2)
ax.yaxis.set_major_locator(MultipleLocator(1))
ax.set_zlim(0.0, 1.0)
ax.zaxis.set_major_locator(MultipleLocator(0.2))

plt.show()