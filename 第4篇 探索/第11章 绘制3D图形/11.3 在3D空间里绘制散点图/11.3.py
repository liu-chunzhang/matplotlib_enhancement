import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

xs = np.random.rand(50)*10
ys = np.random.rand(50)*10 + 20
zs1 = np.random.rand(50)*10
zs2 = np.sqrt(xs**2 + ys**2)

ax.scatter(xs, ys, zs=zs1, zdir="z", c="cornflowerblue", marker="o", s=40, edgecolor='k')
ax.scatter(xs, ys, zs=zs2, zdir="z", c="purple", marker="^", s=40, edgecolor='k')

ax.set(xlabel="X", ylabel="Y", zlabel="Z")

plt.show()