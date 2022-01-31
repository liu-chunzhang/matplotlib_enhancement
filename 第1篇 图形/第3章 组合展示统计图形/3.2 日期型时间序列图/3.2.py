import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots()

months = mdates.MonthLocator()				# a Locator instance
dateFmt = mdates.DateFormatter("%m/%d/%y")	# a Formatter instance

# format the ticks
ax.xaxis.set_major_formatter(dateFmt)
ax.xaxis.set_minor_locator(months)

# set appearance parameters for ticks, ticklabels, and gridlines
ax.tick_params(axis="both", direction="out", labelsize=10)

date1 = datetime.date(2008, 4, 17)
date2 = datetime.date(2017, 5, 4)
delta = datetime.timedelta(days=5)
dates = mdates.drange(date1, date2, delta)	# 返回日期间隔数组
y = np.random.normal(100, 15, len(dates))

ax.plot_date(dates, y, 'b-', alpha=0.7)

ax.set_xmargin(0)
ax.set_ylim(40, 160)
ax.yaxis.set_major_locator(MultipleLocator(20))

fig.autofmt_xdate()							# 调整底部子区x轴刻度标签的旋转角度和子区边缘距离画布低端的距离等

plt.show()