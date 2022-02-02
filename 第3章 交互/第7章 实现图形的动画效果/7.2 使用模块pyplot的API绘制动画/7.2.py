import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Circle
from warnings import filterwarnings

# ignore warning
filterwarnings("ignore", ".*GUI is implemented.*")	# 设置对于警告信息而言脚本所采用的运行模式

# set serveral variables
word = "kaleidoscope"
num = col = row = int(len(word)/4)
data = np.random.random((row, col, num))										# 生成半开区间[0.0, 1.0)内的随机浮点数的数组array
colorMap = ["Spring", "Summer", "Autumn", "Winter"]
subplot_col = subplot_row = 2
font = dict(family="monospace", weight="bold", style="italic", fontsize=10)
subplot_kw = dict(aspect="equal", frame_on=False, xticks=[], yticks=[])			# 用字典数据结构设置子区的坐标轴的展示形式

# create subplots
fig, ax = plt.subplots(subplot_row, subplot_col, subplot_kw=subplot_kw)

# generate a subplot
def rowcolgenerator(r, c, season):
	index = colorMap.index(season)
	t = index*num
	for j in range(len(data)):
		ax[r, c].cla()															# 清除当前子区里的坐标轴ax[r, c]上的图形
		collection = ax[r, c].pcolor(data[j, :], cmap=colorMap[index].lower())	# 绘制模拟颜色图
		patch = Circle((1.5, 1.5), radius=1.5, transform=ax[r, c].transData)
		collection.set_clip_path(patch)											# 将圆形补片patch作为剪切模板或裁减路径
		ax[r, c].set_title(f"No.{j+1} '{word[t:t+3]}' Theme of the {colorMap[index]}", **font)
		ax[r, c].set_axis_off()
		plt.pause(0.15)															# 设置在下一句代码之前的延迟时间，用来绘制较简单的动画内容

# create animation
def animation():
	i = 0
	for r in range(subplot_row):
		for c in range(subplot_col):
			rowcolgenerator(r, c, colorMap[i])
			i += 1

title = "Life kaleidoscope Consists of Four Seasons"
plt.suptitle(title, family="serif", weight="black", fontsize=15)

plt.subplots_adjust(wspace=0.05, hspace=0.2)

if __name__ == "__main__" :
	animation()