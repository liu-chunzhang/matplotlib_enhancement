import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm

fig, ax = plt.subplots(figsize=(7.5, 5.4))

golfer_stats = ["GIR", "Scrambling", "Bounce Back", "Ball Striking", "Sand Saves", "Birdie Conversion"]
golfer_names = [f"Golfer {i}" for i in range(1, 7)]

# we use the normalized percentages.
golfer_percentages = np.random.randn(6, 6)
shape = golfer_percentages.shape

# im = ax.imshow(golfer_percentages, cmap="bwr")					# 这也是红蓝对立，但是色彩饱和度更高
im = ax.imshow(golfer_percentages, cmap=cm.coolwarm)				# 既然是热力图，那么用红蓝对比最佳，选这个颜色映射主要是处于其色饱和度更低，不刺眼
colorbar = fig.colorbar(im, ax=ax, ticks=np.arange(-4.0, 4.1, 0.5))
colorbar.set_label("Golfer normalized percentages", rotation=-90, va='bottom')

ax.set_xticks(np.arange(0, shape[1]))		# 此处必须设置xticks，因为FixedFormatter应该只能与FixedLocator共用，下同
ax.set_xticklabels(golfer_names)
ax.set_yticks(np.arange(0, shape[0]))
ax.set_yticklabels(golfer_stats)

# add text to each area of heatmap
for i in range(len(golfer_stats)):
	for j in range(len(golfer_names)):
		text = ax.text(i, j, round(golfer_percentages[j, i], 2), ha="center", size=12, va="center", color='k')

# turn tick line off and set tick label position
ax.tick_params(direction="out", bottom=False, right=False, labeltop=True, labelbottom=False)
														# 若某位置直接取false，为不要刻度线；若某label[位置]取false，为不要标签。且四周坐标轴默认值并不相同

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