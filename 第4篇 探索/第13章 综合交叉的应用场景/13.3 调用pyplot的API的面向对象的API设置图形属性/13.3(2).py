import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 3]
line, = plt.plot(x, y)
line.set_linewidth(2)

plt.margins(0.0)
plt.show()