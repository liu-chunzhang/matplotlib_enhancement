import matplotlib.pyplot as plt
import numpy as np

from matplotlib.cbook import get_sample_data
from matplotlib.colors import LightSource

fig, ax = plt.subplots(1, 2)

fontstyle = dict(fontsize=20, weight="bold", family="serif")

filePath = get_sample_data("jacksboro_fault_dem.npz", asfileobj=False)	# 将图片文件以Python文件路径形式存储在变量imageFile中
with np.load(filePath) as jfdem:
	elev = jfdem["elevation"]

ls = LightSource(azdeg=315, altdeg=45)									# 从西北方向架起探照灯，方向角315度，海拔45度

ai1 = ax[0].imshow(elev, cmap=plt.cm.gist_earth)						# 进行颜色映射
fig.colorbar(ai1, ax=ax[0], orientation="horizontal")

rgba = ls.shade(elev, cmap=plt.cm.gist_earth, vert_exag=0.05, blend_mode="soft")	# 将地理信息数据elev和照射光源的类型结合起来，再使用相同颜色映射表

ai2 = ax[1].imshow(rgba)
fig.colorbar(ai1, ax=ax[1], orientation="horizontal")					# 此处确实应该是ai1

fig.suptitle("shaded relief plot blending with 'soft'", y=0.92, **fontstyle)

plt.show()