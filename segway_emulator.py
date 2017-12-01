"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()
plt.xlim(-15, 15)
plt.ylim(0, 30)

line, = ax.plot([0, 0], [0, 10], '-o')


x = 0
y = 0
h = 10
fi = 0.1


def animate(i):
    x_1 = x + math.sin(fi) * h
    y_1 = x + math.cos(fi) * h

    line.set_xdata([0, x_1])
    line.set_ydata([0, y_1])
    return line,


def init():
    return line,


ani = animation.FuncAnimation(
    fig, animate,
    np.arange(1, 200),
    init_func=init,
    interval=25, blit=True)

plt.show()
