import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 1000)
y = 0.9*np.sin(np.pi*x)

fig, ax = plt.subplots(2, 3)

# subplot(231)
ax[0, 0].plot(x, y, lw=3, color="steelblue")

ax[0, 0].spines["right"].set_visible(False)
ax[0, 0].spines["top"].set_visible(False)

# set left and bottom spines position
ax[0, 0].spines["left"].set_position(("data", 0.5))
ax[0, 0].spines["bottom"].set_position(("data", 1.0))

# set tickline position of bottom and left spines
ax[0, 0].xaxis.set_ticks_position("bottom")
ax[0, 0].yaxis.set_ticks_position("left")

ax[0, 0].set_xlim(0.0, 2.0)
ax[0, 0].locator_params(axis='x', nbins=5)
ax[0, 0].set_ylim(-1, 1)
ax[0, 0].locator_params(axis='y', nbins=5)
ax[0, 0].set_facecolor("lemonchiffon")

# subplot(234)
ax[1, 0].plot(x, y, lw=3, color="steelblue")

ax[1, 0].spines["right"].set_color("none")
ax[1, 0].spines["top"].set_visible("none")

# set left and bottom spines position
ax[1, 0].spines["left"].set_position("zero")
ax[1, 0].spines["bottom"].set_position("zero")

# set tickline position of bottom and left spines
ax[1, 0].xaxis.tick_bottom()
ax[1, 0].yaxis.tick_left()

ax[1, 0].set_xlim(0.0, 2.0)
ax[1, 0].locator_params(axis='x', nbins=5)
ax[1, 0].set_ylim(-1, 1)
ax[1, 0].locator_params(axis='y', nbins=5)
ax[1, 0].set_facecolor("lemonchiffon")

# subplot(232)
ax[0, 1].plot(x, y, lw=3, color="steelblue")

ax[0, 1].spines["right"].set_visible(False)
ax[0, 1].spines["top"].set_visible(False)

# set left and bottom spines position
ax[0, 1].spines["left"].set_position(("axes", 0.25))
ax[0, 1].spines["bottom"].set_position(("axes", 1.0))

# set tickline position of bottom and left spines
ax[0, 1].xaxis.set_ticks_position("bottom")
ax[0, 1].yaxis.set_ticks_position("left")

ax[0, 1].set_xlim(0.0, 2.0)
ax[0, 1].locator_params(axis='x', nbins=5)
ax[0, 1].set_ylim(-1, 1)
ax[0, 1].locator_params(axis='y', nbins=5)
ax[0, 1].set_facecolor("lemonchiffon")

# subplot(235)
ax[1, 1].plot(x, y, lw=3, color="steelblue")

ax[1, 1].spines["right"].set_color("none")
ax[1, 1].spines["top"].set_color("none")

# set left and bottom spines position
ax[1, 1].spines["left"].set_position("center")
ax[1, 1].spines["bottom"].set_position("center")

# set tickline position of bottom and left spines
ax[1, 1].xaxis.tick_bottom()
ax[1, 1].yaxis.tick_left()

ax[1, 1].set_xlim(0.0, 2.0)
ax[1, 1].locator_params(axis='x', nbins=5)
ax[1, 1].set_ylim(-1, 1)
ax[1, 1].locator_params(axis='y', nbins=5)
ax[1, 1].set_facecolor("lemonchiffon")

# subplot(233)
ax[0, 2].plot(x, y, lw=3, color="steelblue")

ax[0, 2].spines["right"].set_visible(False)
ax[0, 2].spines["top"].set_visible(False)

# set left and bottom spines position
ax[0, 2].spines["left"].set_position(("outward", 3.0))
ax[0, 2].spines["bottom"].set_position(("outward", 2.0))

# set tickline position of bottom and left spines
ax[0, 2].xaxis.set_ticks_position("bottom")
ax[0, 2].yaxis.set_ticks_position("left")

ax[0, 2].set_xlim(0.0, 2.0)
ax[0, 2].locator_params(axis='x', nbins=5)
ax[0, 2].set_ylim(-1, 1)
ax[0, 2].locator_params(axis='y', nbins=5)
ax[0, 2].set_facecolor("lemonchiffon")

# subplot(236)
ax[1, 2].plot(x, y, lw=3, color="steelblue")

ax[1, 2].spines["right"].set_color("none")
ax[1, 2].spines["top"].set_color("none")

# set left and bottom spines position
ax[1, 2].spines["left"].set_position(("outward", -3.0))
ax[1, 2].spines["bottom"].set_position(("outward", -2.0))

# set tickline position of bottom and left spines
ax[1, 2].xaxis.tick_bottom()
ax[1, 2].yaxis.tick_left()

ax[1, 2].set_xlim(0.0, 2.0)
ax[1, 2].locator_params(axis='x', nbins=5)
ax[1, 2].set_ylim(-1, 1)
ax[1, 2].locator_params(axis='y', nbins=5)
ax[1, 2].set_facecolor("lemonchiffon")

fig.subplots_adjust(wspace=0.35, hspace=0.2)

plt.show()