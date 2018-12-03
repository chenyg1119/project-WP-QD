import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
from matplotlib.widgets import Slider, Button

t=1 #tunneling strength
d=2 #quantum dot energy
theta = 0.2 #theta parameter
w = np.linspace(-3,3,1000) weyl point energy
def a(value):
    ***
    calculating three roots of the odd parity tunneling matrix, with no spin splitting
    and value as the theta parameter.
    sorting the roots in descending order as a[0], a[1], a[2]
    --------------------
    returns a
    ***
    m = np.empty([3,1000])
    for i in range(1000):
        m[0,i] = np.sort(np.roots([1,-4,3-(w**2)[i],2-w[i]*np.cos(value)]))[0]
        m[1,i] = np.sort(np.roots([1,-4,3-(w**2)[i],2-w[i]*np.cos(value)]))[1]
        m[2,i] = np.sort(np.roots([1,-4,3-(w**2)[i],2-w[i]*np.cos(value)]))[2]
    return m

fig = plt.figure()
ax = fig.add_subplot(111) #subplot for plot and the slide bar
fig.subplots_adjust(left=0.25, bottom=0.25)

theta_0 = np.pi #control boundary for theta
[line1] = ax.plot(w,a(theta)[0])
[line2] = ax.plot(w,a(theta)[1])
[line3] = ax.plot(w,a(theta)[2])
#draw 3 roots as a function of weyl energy w

theta_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03]) #draw slider
theta_slider = Slider(theta_slider_ax, r'$\theta$', 0.1, 10.0, valinit=theta_0)

def sliders_on_changed(val):
    ***
    activate the controling of the parameter theta
    ------------
    val = theta
    ***
    line1.set_ydata(a(theta_slider.val))
    line2.set_ydata(a(theta_slider.val))
    line3.set_ydata(a(theta_slider.val))
    #updating the parameter theta by sliding val = theta
    fig.canvas.draw_idle()
theta_slider.on_changed(sliders_on_changed)

plt.show()