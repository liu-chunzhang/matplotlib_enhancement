import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

font = dict(family="monospace", weight="bold")


# get the array of RGB channels
outfile = plt.imread(r"./tree_image.jpg")
print(f"the array 'outfile' shape: {outfile.shape}")

# get the arrays of the red, green and blue channels
rCh = outfile[:, :, 0]
print(f"the array 'rCh' shape: {rCh.shape}")

gCh = outfile[:, :, 1]
print(f"the array 'gCh' shape: {gCh.shape}")

bCh = outfile[:, :, 2]
print(f"the array 'bCh' shape: {bCh.shape}")

# show source image
ax[0, 0].imshow(outfile)
ax[0, 0].set_title("source_image", **font)
ax[0, 0].set_axis_off()

# show the images of the red, green and blue channels
ax[0, 1].imshow(rCh)
ax[0, 1].set_title("rCh_image", **font)
ax[0, 1].set_axis_off()

ax[1, 0].imshow(gCh)
ax[1, 0].set_title("gCh_image", **font)
ax[1, 0].set_axis_off()

ax[1, 1].imshow(bCh)
ax[1, 1].set_title("bCh_image", **font)
ax[1, 1].set_axis_off()

plt.show()