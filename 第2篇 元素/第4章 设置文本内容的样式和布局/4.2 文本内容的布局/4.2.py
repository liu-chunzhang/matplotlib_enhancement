import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig = plt.figure(1, figsize=(8, 8), dpi=80, facecolor='w')
fontsize = 0.3*fig.dpi
font_style = {"family":"sans-serif", "fontsize":fontsize, "weight":"bold"}

# add axes in axis coords
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], facecolor='gold')

left, right, top, bottom = 0.2, 0.8, 0.8, 0.2
width, height = right-left, top-bottom

# add a rectangle in axis coords
rect = Rectangle((left, bottom), width, height, transform=ax.transAxes, facecolor='w', edgecolor='k')
ax.add_patch(rect)

# add text in axis coords
# left-bottom
ax.text(0.21, bottom, "left bottom", ha="left", va="bottom", transform=ax.transAxes, **font_style)
																							# ha说的是基线相对于字体的位置，left即基线在文字左边，下同
# left-top
ax.text(0.21, bottom, "left top", ha="left", va="top", transform=ax.transAxes, **font_style)	
																							# va说的是基线相对于字体的位置，top即基线在文字上方，下同
# right-bottom
ax.text(0.79, top, "right bottom", ha="right", va="bottom", transform=ax.transAxes, **font_style)

# right-top
ax.text(0.79, top, "right top", ha="right", va="top", transform=ax.transAxes, **font_style)

# center-top
ax.text(right, bottom, "center top", ha="center", va="top", transform=ax.transAxes, **font_style)

# center-bottom
ax.text(right, bottom, "center bottom", ha="center", va="bottom", transform=ax.transAxes, **font_style)

# left-center
ax.text(left, top, "left center", ha="left", va="center", transform=ax.transAxes, **font_style)

# right-center
ax.text(right, 0.5, "right center", ha="right", va="center", transform=ax.transAxes, rotation=90, **font_style)	# ha和va的效果不随旋转改变

# center-center
ax.text(left, 0.5, "center center", ha="center", va="center", transform=ax.transAxes, rotation=90, **font_style)

# middle
ax.text(0.5, 0.5, "middle", ha="center", va="center", transform=ax.transAxes, color='r', **font_style)

# rotated center-center
# left-center
ax.text(left*0.7, top+0.05, "rotated\ncenter center", ha="center", va="center", transform=ax.transAxes, rotation=45, **font_style)
																						# 这些旋转都是先制定旋转角度再依据指定对齐方式进行位置设定的

plt.show()