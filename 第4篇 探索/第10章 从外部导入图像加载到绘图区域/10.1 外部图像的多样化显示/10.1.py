import matplotlib.pyplot as plt
from matplotlib.cbook import get_sample_data
from matplotlib.patches import Circle

with get_sample_data("./sunflower.png", asfileobj=True) as imageFile:
	imageArray = plt.imread(imageFile)

fig, ax = plt.subplots()
ai = ax.imshow(imageArray)
patch = Circle((605, 360), radius=350, transform=ax.transData)
ai.set_clip_path(patch)

ax.set_axis_off()

plt.show()