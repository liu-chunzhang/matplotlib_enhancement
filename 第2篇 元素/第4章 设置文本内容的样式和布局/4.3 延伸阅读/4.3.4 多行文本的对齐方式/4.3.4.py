import matplotlib.pyplot as plt

fig, ax = plt.subplots()

bbox = dict(boxstyle='square', facecolor='w', edgecolor='k', alpha=0.5)

# ha: left--va: baseline--multialignment: left, center and right
ax.text(0.5, 2.5, "text0\nTEXT0\nalignment", ha='left', va='baseline', multialignment='left', bbox=bbox)
ax.text(0.5, 1.5, "text0\nTEXT0\nalignment", ha='left', va='baseline', multialignment='center', bbox=bbox)
ax.text(0.5, 0.5, "text0\nTEXT0\nalignment", ha='left', va='baseline', multialignment='right', bbox=bbox)

# ha: center--va: baseline--multialignment: left, center and right
ax.text(1.5, 2.5, "text0\nTEXT0\nalignment", ha='center', va='baseline', multialignment='left', bbox=bbox)
ax.text(1.5, 1.5, "text0\nTEXT0\nalignment", ha='center', va='baseline', multialignment='center', bbox=bbox)
ax.text(1.5, 0.5, "text0\nTEXT0\nalignment", ha='center', va='baseline', multialignment='right', bbox=bbox)

# ha: right--va: baseline--multialignment: left, center and right
ax.text(2.5, 2.5, "text0\nTEXT0\nalignment", ha='right', va='baseline', multialignment='left', bbox=bbox)
ax.text(2.5, 1.5, "text0\nTEXT0\nalignment", ha='right', va='baseline', multialignment='center', bbox=bbox)
ax.text(2.5, 0.5, "text0\nTEXT0\nalignment", ha='right', va='baseline', multialignment='right', bbox=bbox)

# set text point
ax.scatter([0.5, 1.5, 2.5, 0.5, 1.5, 2.5, 0.5, 1.5, 2.5], [2.5, 2.5, 2.5, 1.5, 1.5, 1.5, 0.5, 0.5, 0.5], c='r', s=50, alpha=0.6)

# ticklabel and tickline limit
ax.set_xlim(0.0, 3.0)
ax.set_xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
ax.set_xticklabels(["", "left", "", "center", "", "right", ""], fontsize=15)
ax.set_ylim(0.0, 3.0)
ax.set_yticks([3.0, 2.5, 2.0, 1.5, 1.0, 0.5, 0.0])
ax.set_yticklabels(["", "baseline", "", "baseline", "", "baseline", ""], rotation=90, fontsize=15, va='center')

ax.grid(ls="-", lw=2, c='b', alpha=0.5)

plt.show()