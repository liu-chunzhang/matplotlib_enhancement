import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Ellipse

fig, ax = plt.subplots(1, 1, subplot_kw={"aspect":"equal"})

circle = Circle((2, 2), radius=1)

angles = np.linspace(0, 135, 4)

ellipse = [Ellipse((2, 2), 2, 2, a) for a in angles]

ellipse.append(circle)

polygon = ellipse

for pln in polygon:
	ax.add_patch(pln)
	pln.set_alpha(float(np.random.rand(1)))
	pln.set_color(np.random.rand(3))

#ax.axis([0, 4, 0 ,4])
ax.set_xticks(np.arange(0, 5, 1))
ax.set_yticks(np.arange(0, 5, 1))

plt.show()