import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection="3d")

colorList = ["r", "b", "y"]
yLayersList = [2, 1, 0]

for color, layer in zip(colorList, yLayersList):
	x = np.arange(10)
	y = np.random.rand(10)
	ax.bar(x, y, zs=layer, zdir="y", color=color, alpha=0.7, edgecolor='k')

ax.set(xlabel="X", ylabel="Y", zlabel="Z", yticks=yLayersList)

plt.show()