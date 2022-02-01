import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

fig, ax = plt.subplots(1, 2)					# 注意这张图片不能随意拉伸来改变坐标刻度尺！

# subplot(121)
x1 = np.linspace(0, 5, 6)
y1 = np.linspace(0, 5, 6)

ax[0].plot(x1, y1)

ax[0].set_xlim(-2, 6)
ax[0].xaxis.set_major_locator(MultipleLocator(1))
ax[0].set_ylim(0, 5)
ax[0].yaxis.set_major_locator(MultipleLocator(1))

p1 = np.array([0, 0])
p2 = np.array([3, 3])							# 此处设为[1, 1]或者[2, 2]等对于ticklabel Rule的角度更改效果相同，只是后面显示位置改变

# rotation angle
angle = 45
trans_angle = ax[0].transData.transform_angles(np.array([45, ]), p2.reshape([1, 2]))[0]	# reshape将p2变为[3, 3]，trans_angle随着figsize比例而改变

# angle kind text
ax[0].text(p1[0], p1[1], "tickline Rule", fontsize=12, rotation=angle, rotation_mode="anchor")
ax[0].text(p2[0], p2[1], "ticklabel Rule", fontsize=12, rotation=trans_angle, rotation_mode="anchor")

# subplot(122)
x2 = np.arange(-1, 5, 0.5)
y2 = np.arange(-5, 5)

ax[1].plot([0, np.sqrt(3), 2*np.sqrt(3), 3*np.sqrt(3)], [0, 1, 2, 3])

ax[1].set_xlim(-2, 6)
ax[1].xaxis.set_major_locator(MultipleLocator(1))
ax[1].set_ylim(0, 5)
ax[1].yaxis.set_major_locator(MultipleLocator(1))

p3 = np.array([0, 0])
p4 = np.array([2*np.sqrt(3), 2])

# rotation angle
angle = 30
trans_angle = ax[1].transData.transform_angles(np.array([30, ]), p4.reshape([1, 2]))[0]

# angle kind text
ax[1].text(p3[0], p3[1], "tickline Rule", fontsize=12, rotation=angle, rotation_mode="anchor")
ax[1].text(p4[0], p4[1], "ticklabel Rule", fontsize=12, rotation=trans_angle, rotation_mode="anchor")

plt.show()