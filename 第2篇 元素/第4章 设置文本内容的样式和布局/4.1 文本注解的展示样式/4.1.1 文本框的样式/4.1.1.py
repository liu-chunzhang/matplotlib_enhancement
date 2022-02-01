import matplotlib.patches as patches
import matplotlib.pyplot as plt

fig = plt.figure(1, figsize=(9.6, 7.2), dpi=72)		# dpi为图像每英寸长度内的像素点数
fontsize = 0.25 * fig.dpi							# 根据分辨率调节字体大小

# subplot(111)
ax = fig.add_subplot(frameon=False, xticks=[], yticks=[])

boxStyles = patches.BoxStyle.get_styles()
boxStyleNames = list(boxStyles)
boxStyleNames.sort()

for i, name in enumerate(boxStyleNames):
	ax.text((0.9*i+0.5)/len(boxStyleNames), (len(boxStyleNames)-0.5-0.9*i)/len(boxStyleNames), name, ha='center', size=fontsize, 
		transform=ax.transAxes, bbox=dict(boxstyle=name, fc='w', ec='k'))		# ha控制文字的相对位置

plt.show()