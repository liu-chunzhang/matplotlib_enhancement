import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

fig, ax = plt.subplots()

# tick every 5th easter
rule = mdates.rrulewrapper(mdates.YEARLY, byeaster=0, interval=2)
loc = mdates.RRuleLocator(rule)	# a Locator distance

dateFmt = mdates.DateFormatter("%m/%d/%y")	# a Formatter instance

# format the ticks
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(dateFmt)

# set appearance parameters for ticks, ticklabels and gridlines
ax.tick_params(axis='both', direction='out', labelsize=10)
ax.locator_params(axis='y', nbins=9)

date1 = datetime.date(2004, 5, 17)
date2 = datetime.date(2016, 6, 4)
delta = datetime.timedelta(days=5)
dates = mdates.drange(date1, date2, delta)

y = np.random.normal(120, 12, len(dates))

ax.plot_date(dates, y, "b-", alpha=0.7)

fig.autofmt_xdate()

plt.show()