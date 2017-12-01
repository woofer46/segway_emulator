"""
A simple example of an animated plot
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
plt.xlim(-5,5)
plt.ylim(0,6)

x = [0,1]
y = [0,3]
line, = ax.plot(x,y,"-o")


class mayat():
	h = 3
	x = [0,0]
	y = [0,h]
	def __init__(self):
		pass
	def new_coordinates(self,f):
		x1 = self.x[1] * math.cos(f) - self.y[1] * math.sin(f)                                           (1.2)
		y1 = self.x[1] * math.sin(f) + self.y[1] * math.cos(f)
		x = [0,x1]
		y = [0,y1]
		print(x)
		print(y)
		return x,y

mayat_1 = mayat()
def animate(i):
	x,y=mayat_1.new_coordinates(math.pi/2)
	line.set_ydata(y)
	line.set_xdata(x)
	return line,


# Init only required for blitting to give a clean slate.
def init():
    #line.set_ydata(np.ma.array(x, mask=True))
    #h = ball1.h
    #line.set_ydata(h)
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init,
                              interval=50)
plt.show()