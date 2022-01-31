import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

mu, sigma, bins = 75.0, 15.0, 20

x = np.linspace(1, 100, 199)
y = np.random.normal(mu, sigma, 199)

fig, ax = plt.subplots()

# the main axes
ax.plot(x, y, ls="-", lw=2, color="steelblue")

ax.set_xlim(0, 100)
ax.xaxis.set_major_locator(MultipleLocator(20))
ax.set_ylim(10, 170)
ax.yaxis.set_major_locator(MultipleLocator(20))

# this is an inset axes over the main axes
plt.axes([0.2, 0.6, 0.2, 0.2], facecolor='k')

count, bins, patches = plt.hist(y, bins, color="cornflowerblue")					# bins为统计条数为20的list

plt.xticks([])
plt.ylim(0, 28)
plt.yticks([])

# this is an inset axes over the inset axes
plt.axes([0.205, 0.745, 0.05, 0.05])												# 这里稍微调整了一下窗口，下同

y1 = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp( -(bins-mu)**2 / (2 * sigma**2) )

plt.plot(bins, y1, ls="-", color="r")

plt.margins(x=0, y=0)
plt.xticks([])
plt.yticks([])

# this is another inset axes over the main axes
plt.axes([0.65, 0.6, 0.2, 0.2], facecolor='k')

count, bins, patches = plt.hist(y, bins, color="cornflowerblue", density=True, cumulative=True, histtype="step")

plt.xticks([])
plt.ylim(0.0, 1.0)
plt.yticks([])

# this is another inset axes over another inset axes
plt.axes([0.655, 0.745, 0.05, 0.05])

y2 = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp( -(bins-mu)**2 / (2 * sigma**2) )
y2 = y2.cumsum()
y2 = y2/y2[-1]

plt.plot(bins, y2, ls="-", color='r')

plt.xticks([])
plt.yticks([])
plt.margins(0, 0)

plt.show()