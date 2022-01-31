import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(subplot_kw={"aspect":"equal"})

x1 = np.arange(1, 2.6, 0.1)			# y1,y2是屋顶的斜线方程
y1 = x1 + 2

x2 = np.arange(2.5, 4.1, 0.1)
y2 = -x2 + 7

# set background color
rectangle = ax.patch 				# 充当坐标轴背景
rectangle.set_facecolor("lightskyblue")

# house
rectangle1 = Rectangle((1, 0), 3, 3, facecolor='w', edgecolor="rosybrown")		# 以下矩形作为组合图形的一部分，类Rectangle的参数分别为左下角坐标，长，宽...

# door
rectangle2 = Rectangle((1.5, 0), 1, 1.5, facecolor='w', edgecolor='rosybrown', hatch="|||")

# window
rectangle3 = Rectangle((2.9, 1.7), 0.6, 0.6, facecolor='w', edgecolor='rosybrown')

rectangle_list = [rectangle1, rectangle2, rectangle3]
for rect in rectangle_list:
	ax.add_patch(rect)

# roof line
ax.plot([1, 2.5, 4], [3, 4.5, 3], color="rosybrown")

# window line
ax.plot([3.2, 3.2], [1.7, 2.3], color='rosybrown')
ax.plot([2.9, 3.5], [2.0, 2.0], color='rosybrown')
ax.plot([1, 4], [0, 0], color='k')												# 这是个人添加的代表屋底的黑线

# roof filled color 															# 屋顶若依照教材填充，则多出来一条中间的竖线，并不是最优解
# ax.fill_between(x1, 3, y1, color='r', alpha=0.5, interpolate=True, zorder=0)
# ax.fill_between(x2, 3, y2, color='r', alpha=0.5, interpolate=True, zorder=0)

plt.fill([1, 2.5, 4], [3, 4.5, 3], color='r', alpha=0.5)						# 这是个人的填充法，没有中间竖线并且语法更简单

plt.fill([2.9, 2.9, 3.2, 3.2], [1.7, 2.0, 2.0, 1.7], color='b', alpha=0.6)		# 这一段教材没有，是为给窗添加色彩而个人添加的
plt.fill([2.9, 2.9, 3.2, 3.2], [2.0, 2.3, 2.3, 2.0], color='b', alpha=0.6)
plt.fill([3.2, 3.2, 3.5, 3.5], [1.7, 2.0, 2.0, 1.7], color='b', alpha=0.6)
plt.fill([3.2, 3.2, 3.5, 3.5], [2.0, 2.3, 2.3, 2.0], color='b', alpha=0.6)
plt.fill([1, 1, 4, 4, 2.5, 2.5, 1.5, 1.5], [0, 3, 3, 0, 0, 1.5, 1.5, 0], color='y', alpha=0.5)	# 这一段是为给墙添加色彩而个人添加的
plt.fill([1.5, 1.5, 2.5, 2.5], [0, 1.5, 1.5, 0], color="brown", alpha=0.8)						# 这一段是为给木门添加色彩而个人添加的

ax.axis([0, 5, 0, 6])

ax.spines["top"].set_color("none")												# 这一段教材没有，是为消除x轴个人添加的
ax.spines["bottom"].set_color("none")
ax.xaxis.set_ticks_position("none")
ax.set_xticks([])

ax.spines["right"].set_color("none")											# 这一段教材没有，是为消除y轴个人添加的
ax.spines["left"].set_color("none")
ax.yaxis.set_ticks_position("none")
ax.set_yticks([])

plt.show()