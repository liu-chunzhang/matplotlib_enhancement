import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig = plt.figure(1, figsize=(8, 8), dpi=80, facecolor='w')

# add axes in axis coords
ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], facecolor='gold')

left = 0.2
bottom = 0.2
right = 0.8
top = 0.8
width = right-left
height = top-bottom

the_Zen_of_Python = "Explicit is better than implicit. Complex is better than complicated."

# add a rectangle in axis coords
rect = Rectangle((left, bottom), width, height, transform=ax.transAxes, facecolor='w', edgecolor='k')
ax.add_patch(rect)

ax.text(0.5, 1.0, the_Zen_of_Python, transform=ax.transAxes, fontsize=16, weight='black', ha='center', va='top', wrap=True)

ax.text(0.3, 0.5, the_Zen_of_Python, transform=ax.transAxes, ha='right', rotation=20, fontsize=10, style='italic', family='monospace', 
			weight='black', wrap=True)

ax.text(left, bottom, the_Zen_of_Python, transform=ax.transAxes, ha='left', rotation=-15, fontsize=15, style='oblique', family='serif', 
			weight='black', wrap=True)

ax.text(0.6, 0.3, the_Zen_of_Python, transform=ax.transAxes, ha='left', rotation=15, fontsize=22, style='normal', family='sans-serif', wrap=True)

plt.show()