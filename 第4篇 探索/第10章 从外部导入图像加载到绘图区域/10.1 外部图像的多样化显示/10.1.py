import matplotlib.pyplot as plt

from matplotlib.cbook import get_sample_data
from matplotlib.patches import Circle

with get_sample_data("sunflower.png", asfileobj=True) as imageFile:	# 将图片文件以Python文件对象形式存储在变量imageFile中
	imageArray = plt.imread(imageFile)				# 将imageFile转化为数组array，进而将变量存储，实现将外部图片转化为numpy.ndarray
													# 需要先将所用图片储存在anaconda3/lib/python3.7/site-packages/matplotlib/mpl-data/sample_data
fig, ax = plt.subplots()
ai = ax.imshow(imageArray)							# 将以数组形式存储的图像imageArray加载到坐标轴上
patch = Circle((605, 360), radius=350, transform=ax.transData)			# ax.transData表示使用数值坐标系统
ai.set_clip_path(patch)								# 设置切割路径

ax.set_axis_off()

plt.show()