import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)

fig, ax = plt.subplots()

plt.fill(x, y, color="cornflowerblue", alpha=0.4)

plt.plot(x, y, color="cornflowerblue", alpha=0.8)
plt.plot([x[0], x[-1]], [y[0], y[-1]], color="cornflowerblue", alpha=0.8)	# 这条线只起到修饰的作用，对于确定颜色填充区域并无帮助

ax.set_xlim(0, 2*np.pi)
ax.locator_params(axis='x', nbins=7)
ax.set_ylim(-1.1, 1.1)
ax.locator_params(axis='y', nbins=5)

plt.show()