import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots()

# new sample
sample = 10*np.random.rand(50, 2)	# 生成50个2维随机有序数组
var1 = sample[ : , 0]				# 取上述有序数组的第0维
var2 = sample[ : , 1]				# 取上述有序数组的第1维

# threshold value
td = 12

# discriminant function
df = 2*var1 + var2

cates11 = np.ma.masked_where(df>=td, var1)
cates21 = np.ma.masked_where(df<=td, var1)

ax.scatter(var1, var2, s=cates11*50, marker="s", c=cates11, edgecolor="k", cmap=mpl.cm.jet)
ax.scatter(var1, var2, s=cates21*50, marker="o", c=cates21, edgecolor="k", cmap=mpl.cm.jet)

ax.plot(var1, -2*var1 + 12, lw=1, color='b', alpha=0.65)
ax.axis([-1, 11, -1, 11])
ax.xaxis.set_major_locator(MultipleLocator(2.0))
ax.yaxis.set_major_locator(MultipleLocator(2.0))

plt.show()