import matplotlib.pyplot as plt
import numpy as np

mu = 75.0
sigma = 15.0
bins = 20

x = np.linspace(1, 100, 200)
y = np.random.normal(mu, sigma, 200)

fig, ax = plt.subplots()

# the main axes
ax.plot(x, y, ls="-", lw=2, color="steelblue")

ax.set_xlim(0, 100)
ax.set_xticks(np.arange(0, 100.1, 20.0))
ax.set_ylim(10, 170)

# this is an inset axes over the main axes
plt.axes([0.2, 0.63, 0.2, 0.2], facecolor='k')
count, bins, patches = plt.hist(y, bins, color="cornflowerblue")
plt.ylim(0, 28)
plt.xticks([])
plt.yticks([])

# this is an inset axes over the inset axes
plt.axes([0.205, 0.775, 0.05, 0.05])
y1 = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp( -(bins-mu)**2 / (2 * sigma**2) )
plt.plot(bins, y1, ls="-", color="r")
plt.margins(0, 0)
plt.xticks([])
plt.yticks([])

# this is another inset axes over the main axes
plt.axes([0.65, 0.63, 0.2, 0.2], facecolor='k')
count, bins, patches = plt.hist(y, bins, color="cornflowerblue", density=True, cumulative=True, histtype="step")
plt.ylim(0.0, 1.0)
plt.xticks([])
plt.yticks([])

# this is another inset axes over another inset axes
plt.axes([0.655, 0.775, 0.05, 0.05])
y2 = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp( -(bins-mu)**2 / (2 * sigma**2) )
y2 = y2.cumsum()
y2 = y2/y2[-1]
plt.plot(bins, y2, ls="-", color='r')
plt.xticks([])
plt.yticks([])
plt.margins(0, 0)

plt.show()