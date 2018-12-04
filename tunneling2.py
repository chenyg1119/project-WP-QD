import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
from matplotlib.widgets import Slider

t=1
d=2
theta = np.pi

w = np.linspace(-4,4,200)
def b(value):
    m = np.empty([3,200])
    for i in range(200):
        m[0,i] = np.sort(np.roots([1,-2,-2-(w**2)[i],2*(w**2)[i]+2*w[i]*np.cos(value)]))[0]
        m[1,i] = np.sort(np.roots([1,-2,-2-(w**2)[i],2*(w**2)[i]+2*w[i]*np.cos(value)]))[1]
        m[2,i] = np.sort(np.roots([1,-2,-2-(w**2)[i],2*(w**2)[i]+2*w[i]*np.cos(value)]))[2]
    return m

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(left=0.25, bottom=0.25)

ax.plot(w,2*np.ones_like(w))
[line1] = ax.plot(w,b(theta)[0])
[line2] = ax.plot(w,b(theta)[1])
[line3] = ax.plot(w,b(theta)[2])
ax.plot(w,np.zeros_like(w),'--',alpha = 0.6)
ax.set_xlim([-4, 4])

theta_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03])
theta_slider = Slider(theta_slider_ax, r'$\theta$', 0, np.pi, valinit=theta)

def sliders_on_changed(val):
    line1.set_ydata(b(theta_slider.val)[0])
    line2.set_ydata(b(theta_slider.val)[1])
    line3.set_ydata(b(theta_slider.val)[2])
    fig.canvas.draw_idle()
theta_slider.on_changed(sliders_on_changed)

plt.show()