import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(3, 5, figsize=(12, 7.5), sharex=True, sharey=True)

x1, y1, x2, y2 = 0.3, 0.2, 0.8, 0.6

bbox = dict(boxstyle="square", facecolor="w", edgecolor="k")

# subplot(3, 5, 1)
ax[0, 0].plot([x1, x2], [y1, y2], ".")

ax[0, 0].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="angle, angleA=0, angleB=90, rad=5"))
                                                            # angle的连接风格时可以设置rad

ax[0, 0].text(0.05, 0.95, "angle,\nangleA=0,\nangleB=90,\nrad=5", ha="left", va="top", bbox=bbox)

ax[0, 0].set_xlim(0, 1)
ax[0, 0].set_xticklabels([])
ax[0, 0].set_ylim(0, 1)
ax[0, 0].set_yticklabels([])

# subplot(3, 5, 6)
ax[1, 0].plot([x1, x2], [y1, y2], ".")

ax[1, 0].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="angle, angleA=20, angleB=50, rad=10"))

ax[1, 0].text(0.05, 0.95, "angle,\nangleA=20,\nangleB=50,\nrad=10", ha="left", va="top", bbox=bbox)

ax[1, 0].set_xlim(0, 1)
ax[1, 0].set_xticklabels([])
ax[1, 0].set_ylim(0, 1)
ax[1, 0].set_yticklabels([])

# subplot(3, 5, 11)
ax[2, 0].plot([x1, x2],[y1, y2], ".")

ax[2, 0].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="angle, angleA=-90, angleB=0, rad=0.0"))

ax[2, 0].text(0.05, 0.95, "angle,\nangleA=-90,\nangleB=0,\nrad=0.0", ha="left", va="top", bbox=bbox)

ax[2, 0].set_xlim(0, 1)
ax[2, 0].set_xticklabels([])
ax[2, 0].set_ylim(0, 1)
ax[2, 0].set_yticklabels([])

# subplot(3, 5, 2)
ax[0, 1].plot([x1, x2], [y1, y2], ".")

ax[0, 1].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="angle3, angleA=90, angleB=0"))
                                                        # angle3的连接风格时不能设置rad
ax[0, 1].text(0.05, 0.95, "angle3,\nangleA=90,\nangleB=0", ha="left", va="top", bbox=bbox)

ax[0, 1].set_xlim(0, 1)
ax[0, 1].set_xticklabels([])
ax[0, 1].set_ylim(0, 1)
ax[0, 1].set_yticklabels([])

# subplot(3, 5, 7)
ax[1, 1].plot([x1, x2], [y1, y2], ".")

ax[1, 1].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="angle3, angleA=0, angleB=90"))

ax[1, 1].text(0.05, 0.95, "angle3,\nangleA=0,\nangleB=90", ha="left", va="top", bbox=bbox)

ax[1, 1].set_xlim(0, 1)
ax[1, 1].set_xticklabels([])
ax[1, 1].set_ylim(0, 1)
ax[1, 1].set_yticklabels([])

# subplot(3, 5, 12)
ax[2, 1].plot([x1, x2], [y1, y2], ".")

ax[2, 1].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="angle3, angleA=20, angleB=60"))

ax[2, 1].text(0.05, 0.95, "angle3,\nangleA=20,\nangleB=60", ha="left", va="top", bbox=bbox)

ax[2, 1].set_xlim(0, 1)
ax[2, 1].set_xticklabels([])
ax[2, 1].set_ylim(0, 1)
ax[2, 1].set_yticklabels([])

# subplot(3, 5, 3)
ax[0, 2].plot([x1, x2], [y1, y2], ".")

ax[0, 2].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="arc, angleA=-90, armA=40, angleB=0, armB=50, rad=0.0"))
                                                        # arc的连接风格时可以设置rad
ax[0, 2].text(0.05, 0.95, "arc,\nangleA=-90,\narmA=40,\nangleB=0,\narmB=50,\nrad=0.0", ha="left", va="top", bbox=bbox)

ax[0, 2].set_xlim(0, 1)
ax[0, 2].set_xticklabels([])
ax[0, 2].set_ylim(0, 1)
ax[0, 2].set_yticklabels([])

# subplot(3, 5, 8)
ax[1, 2].plot([x1, x2], [y1, y2], ".")

ax[1, 2].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="arc, angleA=-90, armA=40, angleB=0, armB=50, rad=3"))

ax[1, 2].text(0.05, 0.95, "arc,\nangleA=-90,\narmA=40,\nangleB=0,\narmB=50,\nrad=3", ha="left", va="top", bbox=bbox)

ax[1, 2].set_xlim(0, 1)
ax[1, 2].set_xticklabels([])
ax[1, 2].set_ylim(0, 1)
ax[1, 2].set_yticklabels([])

# subplot(3, 5, 13)
ax[2, 2].plot([x1, x2], [y1, y2], ".")

ax[2, 2].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="arc, angleA=100, armA=0, angleB=20, armB=50, rad=10"))

ax[2, 2].text(0.05, 0.95, "arc,\nangleA=100,\narmA=0,\nangleB=20,\narmB=50,\nrad=10", ha="left", va="top", bbox=bbox)

ax[2, 2].set_xlim(0, 1)
ax[2, 2].set_xticklabels([])
ax[2, 2].set_ylim(0, 1)
ax[2, 2].set_yticklabels([])

# subplot(3, 5, 4)
ax[0, 3].plot([x1, x2], [y1, y2], ".")

ax[0, 3].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray",
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="arc3, rad=0.0"))
                                                                # arc3的连接风格时只能设置rad
ax[0, 3].text(0.05, 0.95, "arc3,\nrad=0.0", ha="left", va="top", bbox=bbox)

ax[0, 3].set_xlim(0, 1)
ax[0, 3].set_xticklabels([])
ax[0, 3].set_ylim(0, 1)
ax[0, 3].set_yticklabels([])

# subplot(3, 5, 9)
ax[1, 3].plot([x1, x2], [y1, y2], ".")

ax[1, 3].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="arc3, rad=0.5"))

ax[1, 3].text(0.05, 0.95, "arc3,\nrad=0.5", ha="left", va="top", bbox=bbox)

ax[1, 3].set_xlim(0, 1)
ax[1, 3].set_xticklabels([])
ax[1, 3].set_ylim(0, 1)
ax[1, 3].set_yticklabels([])

# subplot(3, 5, 14)
ax[2, 3].plot([x1, x2], [y1, y2], ".")

ax[2, 3].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="arc3, rad=-0.5"))

ax[2, 3].text(0.05, 0.95, "arc3,\nrad=-0.5", ha="left", va="top", bbox=bbox)

ax[2, 3].set_xlim(0, 1)
ax[2, 3].set_xticklabels([])
ax[2, 3].set_ylim(0, 1)
ax[2, 3].set_yticklabels([])

# subplot(3, 5, 5)
ax[0, 4].plot([x1, x2], [y1, y2], ".")

ax[0, 4].annotate("", xy=(x1, y1),xycoords="data", xytext=(x2, y2),textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="bar, armA=30, armB=30, fraction=0.0"))
                                                        # bar的连接风格时不能设置rad
ax[0, 4].text(0.05, 0.95, "bar,\narmA=30,\narmB=30,\nfraction=0.0", ha="left", va="top", bbox=bbox)

ax[0, 4].set_xlim(0, 1)
ax[0, 4].set_xticklabels([])
ax[0, 4].set_ylim(0, 1)
ax[0, 4].set_yticklabels([])

# subplot(3, 5, 10)
ax[1, 4].plot([x1, x2], [y1, y2], ".")

ax[1, 4].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2), textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="bar, fraction=-0.3"))

ax[1, 4].text(0.05, 0.95, "bar,\nfraction=-0.3", ha="left", va="top", bbox=bbox)

ax[1, 4].set_xlim(0, 1)
ax[1, 4].set_xticklabels([])
ax[1, 4].set_ylim(0, 1)
ax[1, 4].set_yticklabels([])

# subplot(3, 5, 15)
ax[2, 4].plot([x1, x2], [y1, y2], ".")

ax[2, 4].annotate("", xy=(x1, y1), xycoords="data", xytext=(x2, y2),textcoords="data", arrowprops=dict(arrowstyle="->", color="gray", 
                    shrinkA=5, shrinkB=5, patchA=None, patchB=None, connectionstyle="bar,armB=60,angle=90,fraction=0.4"))

ax[2, 4].text(0.05, 0.95, "bar,\narmB=60,\nangle=90,\nfraction=0.4", ha="left", va="top", bbox=bbox)

ax[2, 4].set_xlim(0, 1)
ax[2, 4].set_xticklabels([])
ax[2, 4].set_ylim(0, 1)
ax[2, 4].set_yticklabels([])

fig.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=0.95, wspace=0.02, hspace=0.02)

plt.show()