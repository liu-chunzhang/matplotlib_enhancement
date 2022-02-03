import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D								# 绘制3D图形而导入类Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

x = np.arange(-3.0, 3.01, 0.25)
y = np.arange(-3.0, 3.01, 0.25)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(np.power(x, 2)+np.power(y, 2)))

# plot 3d surface
surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)	
																				# 绘制曲面。rstride和cstride设置曲面上单位曲面大小，补片连接线宽度设置为0

# customize the z axis
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set(zlim=(-1, 1))
ax.zaxis.set_major_locator(LinearLocator(7))
ax.zaxis.set_major_formatter(FormatStrFormatter("%3.2f"))

# add a color bar mapping values to colors
fig.colorbar(surf, shrink=0.6, aspect=20, ticks=np.arange(-1.0, 1.1, 0.2))		# shrink设置表尺整体大小，aspect设置表尺框的长宽比

plt.show()