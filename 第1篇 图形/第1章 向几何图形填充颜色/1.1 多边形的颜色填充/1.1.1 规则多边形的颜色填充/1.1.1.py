import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots()

x = [0, 0, 5, 10, 15, 15, 10, 5]
y = [5, 10, 15, 15, 10, 5, 0, 0]

plt.fill(x, y, color="cornflowerblue")		# 绘制封闭图形并填充

plt.xlim(-1, 16)
plt.ylim(-1, 16)

ax.xaxis.set_major_locator(MultipleLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(5))

plt.show()