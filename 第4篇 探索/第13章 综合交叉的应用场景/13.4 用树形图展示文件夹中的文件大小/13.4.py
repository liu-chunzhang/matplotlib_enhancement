import matplotlib.pyplot as plt
import squarify		# pip install squarify

from glob import glob
from matplotlib.image import thumbnail
from os import mkdir
from os.path import basename, dirname, getsize, isdir, join
from sys import argv

script, indir, outdir = argv

sizeList = []
nameList = []

if len(argv) != 3:
	print("On command line, information is not full.")

if not isdir(indir):
	print(f"Input directory {indir} is not found.")

if not isdir(outdir):
	print(f"Outdir directory {outdir} is created.")
	mkdir(outdir)
else:
	print(f"Outdir directory {outdir} has been created.")

# the image file must be PNG or illow-readable
for fname in glob(join(indir, "*.png")):
	indir = dirname(fname)
	filename = basename(fname)
	outfile = join(outdir, filename)
	fig = thumbnail(fname, outfile, scale=0.5)
	print(f"Copy '{filename}' of '{indir}' to '{outdir}'")
	outfilesize = getsize(outfile)
	sizeList.append(outfilesize)
	fn = filename.split(".")
	nameList.append(fn[0])

# treemap
squarify.plot(sizeList, label=nameList, alpha=0.7, edgecolor='k')
plt.hsv()	# set color
plt.axis("off")
plt.show()
