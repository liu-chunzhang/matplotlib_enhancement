import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots()

x = np.random.rand(50)*10
y = np.random.rand(50)*10 + 20
s = np.random.rand(50)*100
c = np.random.rand(50)

data = {"a":x, "b":y, "color":c, "size":s}								# 使用字符串代替变量

# with the "data" keyword argument
ax.scatter("a", "b", c="color", s="size", data=data, edgecolor='k')		# 使用变量data来实现变量用字符串替代

ax.set(xlabel="X", ylabel="Y")
ax.set_xlim(-2, 12)
ax.xaxis.set_major_locator(MultipleLocator(2))
ax.set_ylim(18, 32)
ax.yaxis.set_major_locator(MultipleLocator(2))

plt.show()
