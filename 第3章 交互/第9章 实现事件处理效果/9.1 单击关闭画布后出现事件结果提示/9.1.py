from __future__ import print_function
import matplotlib.pyplot as plt

def handle_event(close):
	print("Handling Event: Closed Figure!")

font_style = {"family":"serif", "weight":"black", "size":50}

fig = plt.figure()
fig.canvas.mpl_connect("close_event", handle_event)

plt.text(0.15, 0.5, "close_event", **font_style)

plt.show()