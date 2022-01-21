import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import FuncFormatter, MaxNLocator

fig, ax = plt.subplots()

ticklabels_list = ['stage1', 'stage2', 'stage3', 'stage4', 'stage5']

x = np.arange(len(ticklabels_list))
y = np.exp(-x)

ax.plot(x, y, lw=3, color="steelblue", marker="s", mfc='r', mec='c')

def tick_controller(value, position):
	if int(value) in x :
		return ticklabels_list[int(value)]
	else :
		return " "

ax.xaxis.set_major_formatter(FuncFormatter(tick_controller))
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

xticklabel_text = ax.get_xticklabels()
for i, j in enumerate(xticklabel_text):
	j.set_family("monospace")
	j.set_fontsize(12)
	j.set_weight("bold")
	j.set_rotation(30)

ax.margins(0.25)

plt.show()