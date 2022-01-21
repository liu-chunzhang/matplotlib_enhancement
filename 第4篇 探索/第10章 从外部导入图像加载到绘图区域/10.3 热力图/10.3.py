import matplotlib.pyplot as plt
import numpy as np

golfer_stats = ["GIR", "Scrambling", "Bounce Back", "Ball Striking", "Sand Saves", "Birdie Conversion"]

golfer_names = [f"Golfer {i}" for i in range(1, 7)]

# we use the normalized percentages.
golfer_percentages = np.random.randn(6, 6)
shape = golfer_percentages.shape

fig, ax = plt.subplots()

im = ax.imshow(golfer_percentages, cmap="Greens")
colorbar = fig.colorbar(im, ax=ax)
colorbar.set_label("Golfer normalized percentages", rotation=-90, va='bottom')

ax.set_xticks(np.arange(0, shape[1]))
ax.set_yticks(np.arange(0, shape[0]))

ax.set_xticklabels(golfer_names)
ax.set_yticklabels(golfer_stats)

# add text to each area of heatmap
for i in range(len(golfer_stats)):
	for j in range(len(golfer_names)):
		text = ax.text(i, j, round(golfer_percentages[j, i], 1), ha="center", va="center", color='w')

# turn tick line off and set tick label position
ax.tick_params(direction="out", bottom=False, right=False, labeltop=True, labelbottom=False)

# set tick label format
plt.setp(ax.get_xticklabels(), rotation=-30, ha="right", rotation_mode="anchor")

# turn spines off
spinesTupleList = list(ax.spines.items())
for i, each in enumerate(spinesTupleList):
	spine = each[1]
	spine.set_visible(False)

# set minor tick line position and create white grid
ax.set_xticks(np.arange(0.5, shape[1]-1, 1), minor=True)
ax.set_yticks(np.arange(0.5, shape[0]-1, 1), minor=True)
ax.grid(which="minor", color='w', linestyle="-", linewidth=3)

ax.tick_params(which="minor", top=False, bottom=False, left=False, right=False)

fig.tight_layout()
plt.show()