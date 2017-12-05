"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time

fig, ax = plt.subplots()
plt.xlim(-15, 15)
plt.ylim(0, 20)

line, = ax.plot([0, 0], [0, 10], '-o')


x = 0
y = 0
h = 10
fi = 0.2
dt = 25 / 1000
g = 9.8
m = 5
I = (1/3) * m * h ** 2
omega = 0
v = 0
a = 0
kp = 40
kd = 10

def animate(i):
    global x,y,h,fi,dt,g,m,I,omega,v,a,kp,kd
    #a = math.cos(time.time() * 20) * 20
    v = a * dt
    x += v
    a = kp * fi + kd * omega
    angular_a = ( m * g * h * math.sin(fi) - m * a * h * math.cos(fi) ) / I
    omega += angular_a * dt
    fi += omega * dt
    x_1 = x + math.sin(fi) * h
    y_1 = x + math.cos(fi) * h

    line.set_xdata([x, x_1])
    line.set_ydata([y, y_1])
    return line,


def init():
    return line,


ani = animation.FuncAnimation(
    fig, animate,
    np.arange(1, 200),
    init_func=init,
    interval=25, blit=True)

plt.show()
