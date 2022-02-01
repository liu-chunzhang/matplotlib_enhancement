import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)

bbox = {"boxstyle":"square", "facecolor":"gray", "edgecolor":"w", "pad":0, "alpha":0.5}

# subplot(121)

# ha-va: top
ax[0].text(0.5, 2.5, "text45", ha="left", va="top", rotation=45, rotation_mode="default", bbox=bbox)			
																# rotation_mode使用default或None参数是先旋转边界框，然后（根据水平和垂直方式）进行对齐

ax[0].text(1.5, 2.5, "text45", ha="center", va="top", rotation=45, rotation_mode="default", bbox=bbox)

ax[0].text(2.5, 2.5, "text45", ha="right", va="top", rotation=45, rotation_mode="default", bbox=bbox)

# ha-va: center
ax[0].text(0.5, 1.5, "text45", ha="left", va="center", rotation=45, rotation_mode="default", bbox=bbox)

ax[0].text(1.5, 1.5, "text45", ha="center", va="center", rotation=45, rotation_mode="default", bbox=bbox)

ax[0].text(2.5, 1.5, "text45", ha="right", va="center", rotation=45, rotation_mode="default", bbox=bbox)

# ha-va: bottom
ax[0].text(0.5, 0.5, "text45", ha="left", va="bottom", rotation=45, rotation_mode="default", bbox=bbox)

ax[0].text(1.5, 0.5, "text45", ha="center", va="bottom", rotation=45, rotation_mode="default", bbox=bbox)

ax[0].text(2.5, 0.5, "text45", ha="right", va="bottom", rotation=45, rotation_mode="default", bbox=bbox)

# set text point
ax[0].scatter([0.5, 1.5, 2.5, 0.5, 1.5, 2.5, 0.5, 1.5, 2.5], [2.5, 2.5, 2.5, 1.5, 1.5, 1.5, 0.5, 0.5, 0.5], c='r', s=50, alpha=0.5)

# ticklabel and tickline limit
ax[0].set_xlim(0.0, 3.0)
ax[0].set_xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax[0].set_xticklabels(["", "left", "", "center", "", "right", ""], fontsize=15)
ax[0].set_ylim(0.0, 3.0)
ax[0].set_yticks([3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0])
ax[0].set_yticklabels(["", "top", "", "center", "", "bottom", ""], rotation=90, fontsize=15, va='center')

ax[0].set_title("default", fontsize=18)
ax[0].grid(ls='-', lw=2, color='b', alpha=0.5)


# subplot(122)

# ha-va: top
ax[1].text(0.5, 2.5, "text45", ha="left", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)
																		# rotation_mode使用anchor参数是先（根据水平和垂直方式）进行对齐，然后旋转边界框

ax[1].text(1.5, 2.5, "text45", ha="center", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)

ax[1].text(2.5, 2.5, "text45", ha="right", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)

# ha-va: center
ax[1].text(0.5, 1.5, "text45", ha="left", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)

ax[1].text(1.5, 1.5, "text45", ha="center", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)

ax[1].text(2.5, 1.5, "text45", ha="right", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)

# ha-va: right
ax[1].text(0.5, 0.5, "text45", ha="left", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)

ax[1].text(1.5, 0.5, "text45", ha="center", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)

ax[1].text(2.5, 0.5, "text45", ha="right", va="top", rotation=45, rotation_mode="anchor", bbox=bbox)

# set text point
ax[1].scatter([0.5, 1.5, 2.5, 0.5, 1.5, 2.5, 0.5, 1.5, 2.5], [2.5, 2.5, 2.5, 1.5, 1.5, 1.5, 0.5, 0.5, 0.5], c='r', s=50, alpha=0.5)

# ticklabel and tickline limit
ax[1].set_xlim(0.0, 3.0)
ax[1].set_xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax[1].set_xticklabels(["", "left", "", "center", "", "right", ""], fontsize=15)
ax[1].set_ylim(0.0, 3.0)
ax[1].set_yticks([3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0])
ax[1].set_yticklabels(["", "top", "", "center", "", "bottom", ""], rotation=90, fontsize=15, va='center')

ax[1].set_title("anchor", fontsize=18)

ax[1].grid(ls='-', lw=2, color='b', alpha=0.5)

plt.show()