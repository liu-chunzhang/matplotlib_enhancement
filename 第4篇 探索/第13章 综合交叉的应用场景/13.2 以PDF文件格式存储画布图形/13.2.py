import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MultipleLocator

with PdfPages("PdfPages.pdf") as pdf:						# 为生成PDF文件，创建文件名称和存储路径

	# page one
	fig, ax = plt.subplots(figsize=(4, 4))
	x = np.random.rand(20)*100
	y = np.random.rand(20)*100 + 30
	s = np.random.rand(20)*100
	c = np.random.rand(20)
	data = {"a":x, "b":y, "color":c, "size":s}
	plt.scatter("a", "b", c="color", s="size", edgecolor='k', data=data)

	ax.set_xlim(-20, 120)
	ax.xaxis.set_major_locator(MultipleLocator(20))
	plt.xticks(fontsize=12)
	ax.set_ylim(20, 140)
	ax.yaxis.set_major_locator(MultipleLocator(20))
	plt.yticks(fontsize=12)

	ax.set_title("Page1", fontsize=15)
	
	pdf.savefig()		# save the current figure
	#plt.close()		# close the current figure, which seemly makes no sense
	
	# page two
	fig = plt.figure(figsize=(8, 6))

	x = np.linspace(0, 2*np.pi, 100)
	y1 = 0.5*np.cos(x)									# 用折线法绘制圆形
	y2 = 0.5*np.sin(x)

	plt.plot(y1, y2, color="navy", lw=3)

	plt.axis("equal")

	plt.title("Page2", fontsize=15)
	pdf.savefig(fig)

	# page three
	fig, ax = plt.subplots(1, 2)

	x = np.linspace(0, 2*np.pi, 100)
	y = np.sin(x)*np.exp(-x)

	ax[0].scatter(x, y, c="cornflowerblue", s=10)

	ax[0].xaxis.set_major_locator(MultipleLocator(1))
	ax[0].yaxis.set_major_locator(MultipleLocator(0.05))

	ax[1].plot(x, y, "k-o", lw=2)
	ax[1].set(xlim=(-1, 7))
	ax[1].xaxis.set_major_locator(MultipleLocator(1.0))
	ax[1].yaxis.set_major_locator(MultipleLocator(1.0))

	fig.suptitle("Page3", fontsize=15)
	pdf.savefig(fig)
	
	plt.close(fig)