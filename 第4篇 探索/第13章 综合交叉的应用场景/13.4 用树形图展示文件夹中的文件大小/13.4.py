import matplotlib.pyplot as plt
import squarify													# pip install squarify

from glob import glob
from matplotlib.image import thumbnail
from os import mkdir
from os.path import basename, dirname, getsize, isdir, join
from sys import argv

script, indir, outdir = argv									# 在命令行执行此脚本的命令python3 13.4.py . thumbnail/

sizeList = []
nameList = []

if len(argv) != 3:
	print("On command line, information is not full.")
	raise SystemExit

if not isdir(indir):
	print(f"Input directory {indir} is not found.")
	raise SystemExit

if not isdir(outdir):
	print(f"Outdir directory {outdir} is created.")
	mkdir(outdir)
else:
	print(f"Outdir directory {outdir} has been created.")

# the image file must be PNG or illow-readable
for fname in glob(join(indir, "*.png")):						# 使用函数glob()建立包含PNG格式的图像生成器
	indir = dirname(fname)
	filename = basename(fname)
	outfile = join(outdir, filename)
	fig = thumbnail(fname, outfile, scale=0.5)					# scale参数指长和宽各自变为原来各自长度的比率
	print(f"Copy '{filename}' of '{indir}' to '{outdir}'")
	outfilesize = getsize(outfile)
	sizeList.append(outfilesize)
	fn = filename.split(".")
	nameList.append(fn[0])

# treemap
squarify.plot(sizeList, label=nameList, alpha=0.7, edgecolor='k')
plt.hsv()														# 设置配色方案

plt.axis("off")

plt.show()