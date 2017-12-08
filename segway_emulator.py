"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time

fig, ax = plt.subplots()
plt.xlim(-5, 5)
plt.ylim(-5, 5)

line, = ax.plot([0, 0], [0, 10], '-o')


x = 0
y = 0
h = 1
fi = -0.2
dt = (25 / 1000)
g = 9.8
m = 5
I = m * h ** 2
omega = 0
v = 0
a = 0
kp = 20
kd = math.sqrt(2 * h * (kp - g))

kp_v = 1 / (50 * dt)
v_s = 0

x_s = 2
kp_x = 1 / (100 * dt)
i_x_dt = 0
def animate(i):
    global x,y,h,fi,dt,g,m,I,omega,v,a,kp,kd,kp_v,v_s,i_x_dt
    #a = math.cos(time.time() * 20) * 20
    #a = kp * fi + kd * omega
    #v_s = math.cos(time.time() * 2) * 2
    #print(my_fi)
    angular_a  = ( m * g * h * math.sin(fi) - (m * a + 0) * h * math.cos(fi) ) / I
    omega += angular_a * dt
    fi += omega * dt
    i_x_dt += (x_s - x) * dt
    ki = 0.1
    a_s = -kp_v * (v_s - v) - kp_x * (x_s - x) - ki * i_x_dt
    
    a = kp * fi + kd * omega + a_s 
    v += a * dt
    x += v * dt

    x_1 = x + math.sin(fi) * h
    y_1 = y + math.cos(fi) * h
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
