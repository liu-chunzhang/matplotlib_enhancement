import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

fig, ax = plt.subplots(1, 2, subplot_kw={"aspect":"equal"})

# subplot(121)
angles = np.linspace(0, 135, 4)
ellipse = [Ellipse((2, 2), 4, 2, a) for a in angles]

for elle in ellipse:
	ax[0].add_patch(elle)
	elle.set_alpha(0.4)
	elle.set_color("cornflowerblue")

ax[0].axis([-1, 5, -1, 5])

# subplot(122)
num = np.arange(0, 100, 1)
ellipse = [Ellipse(xy=np.random.rand(2)*10, width=np.random.rand(1), height=np.random.rand(1), angle=np.random.rand(1)*360) for i in num]

for elle in ellipse:
	ax[1].add_patch(elle)
	elle.set_alpha(float(np.random.rand(1)))
	elle.set_color(np.random.rand(3))

ax[1].axis([-1, 11, -1, 11])

plt.tight_layout()

plt.show()