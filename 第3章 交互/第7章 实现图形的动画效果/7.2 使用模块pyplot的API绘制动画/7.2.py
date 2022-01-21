import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle
from warnings import filterwarnings

# ignore warning
filterwarnings("ignore", ".*GUI is implemented.*")

# set serveral variables
word = "kaleidoscope"
num = col = row = int(len(word)/4)

data = np.random.random((row, col, num))
colorMap = ["spring", "summer", "autumn", "winter"]

subplot_col = subplot_row = int(len(word)/6)

font = dict(family="monospace", weight="bold", style="italic", fontsize=10)
subplot_kw = dict(aspect="equal", frame_on=False, xticks=[], yticks=[])

# create subplots
fig, ax = plt.subplots(subplot_row, subplot_col, subplot_kw=subplot_kw)

# generate a subplot
def rowcolgenerator(r, c, season):
	index = colorMap.index(season)
	t = index*num
	for j in range(len(data)):
		ax[r, c].cla()
		collection = ax[r, c].pcolor(data[j, :], cmap=colorMap[index])
		patch = Circle((1.5, 1.5), radius=1.5, transform=ax[r, c].transData)
		collection.set_clip_path(patch)
		element = colorMap[index].capitalize()
		ax[r, c].set_title(f"No.{j+1} '{word[t:t+3]}' Theme of the {element}", **font)
		ax[r, c].set_axis_off()
		plt.pause(0.15)

# create animation
def animation():
	i = 0
	for r in range(subplot_row):
		for c in range(subplot_col):
			rowcolgenerator(r, c, colorMap[i])
			i += 1

	title = "Life kaleidoscope Consists of Four Seasons"
	plt.suptitle(title, family="serif", weight="black", fontsize=20)

	plt.subplots_adjust(wspace=0.05, hspace=0.2)

if __name__ == "__main__" :
	animation()