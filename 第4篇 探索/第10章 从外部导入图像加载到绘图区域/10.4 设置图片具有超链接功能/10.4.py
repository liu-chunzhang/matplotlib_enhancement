import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage, TextArea

fig = plt.figure()

# set background of picture in the axes
ax0 = plt.axes([0.0, 0.0, 1.0, 1.0], frameon=True, aspect="equal")
backgroundData = plt.imread("map.jpg")
im0 = ax0.imshow(backgroundData)
ax0.set_axis_off()

# set point links with urls
pc = plt.scatter([351, 823], [343, 163], c='r', s=50, alpha=0.8)
pc.set_urls(["https://www.trip.com", "https://www.wunderground.com"])

# add arrow to the background of picture
ax0.annotate("", xy=(351, 343), xytext=(823, 163), xycoords="data", textcoords="data", color='b', arrowprops=dict(shrinkA=10, shrinkB=10, 
				arrowstyle="fancy, head_length=0.6, head_width=0.6, tail_width=0.5", connectionstyle="arc3, rad=0.3") )

# annotate 1st position with a image box
imageData = plt.imread("das-Auto.png")
imagebox = OffsetImage(imageData, zoom=0.035)		# 设置图像内容与缩放比例

ab_image = AnnotationBbox(imagebox, xy=(351, 343), xycoords="data", xybox=(-50, 40), boxcoords="offset points", pad=0.05, frameon=True, 
							arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=5, relpos=(1.0, 0.0)))
ax0.add_artist(ab_image)

# annotate 2nd position with a linked image
ax1 = plt.axes([0.63, 0.82, 0.1, 0.1], frameon=True, aspect="equal")
imageData = plt.imread("pilot.png")
im = ax1.imshow(imageData, url="https://www.lufthansa.com")
#im.set_url("https://www.lufthansa.com")
ax1.set_axis_off()

# annotate 2nd position with a text box
textprops = dict(fontsize=10, weight="bold", color="b")
textbox = TextArea("TRAVEL", textprops=textprops)

ab_text = AnnotationBbox(textbox, xy=(823, 163), xycoords="data", xybox=(-40, 52), boxcoords="offset points", pad=0.2, bboxprops=dict(
							facecolor="gray", alpha=0.5), arrowprops=dict(arrowstyle="-", shrinkA=0, shrinkB=5, relpos=(0.5, 0.0)))
ax0.add_artist(ab_text)

#plt.show()
fig.savefig("hyperlink_image.svg")