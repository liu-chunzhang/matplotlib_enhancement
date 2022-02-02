from __future__ import print_function
import matplotlib.pyplot as plt

def handle_event(close):										# 引入事件处理机制，对于关闭画布的动作有了有效追踪与记录
	print("Handling Event: Closed Figure!")

font_style = {"family":"serif", "weight":"black", "size":40}

fig = plt.figure()
fig.canvas.mpl_connect("close_event", handle_event)

plt.text(0.15, 0.5, "close_event", **font_style)

plt.show()