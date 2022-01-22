import matplotlib.pyplot as plt
import scipy.misc as msc

fig, ax = plt.subplots(1, 2)

font = dict(family="serif", weight="bold")

ascent = msc.ascent()
invented_ascent = 255-ascent

# show source image
ax[0].imshow(ascent)
ax[0].set_title("source_image", **font)
ax[0].set_axis_off()

# show inverted image
ax[1].imshow(invented_ascent)
ax[1].set_title("inverted_image", **font)
ax[1].set_axis_off()

plt.show()