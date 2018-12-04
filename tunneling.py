import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg
from matplotlib.widgets import Slider

t=1 #tunneling strength
d=2 #quantum dot energy
theta = 0 #theta parameter
w = np.linspace(-4,4,500) #weyl point energy
def a(value):
    '''calculating three roots of the odd parity tunneling matrix, with no spin splitting
    and value as the theta parameter.
    sorting the roots in descending order as a[0], a[1], a[2]
    --------------------
    returns a
    '''
    m = np.empty([3,500])
    for i in range(500):
        m[0,i] = np.sort(np.roots([1,-4,3-(w**2)[i],2-w[i]*np.cos(value)]))[0]
        m[1,i] = np.sort(np.roots([1,-4,3-(w**2)[i],2-w[i]*np.cos(value)]))[1]
        m[2,i] = np.sort(np.roots([1,-4,3-(w**2)[i],2-w[i]*np.cos(value)]))[2]
    return m

fig = plt.figure()
ax = fig.add_subplot(111) #subplot for plot and the slide bar
fig.subplots_adjust(left=0.25, bottom=0.25)

[line1] = ax.plot(w,a(theta)[0])
[line2] = ax.plot(w,a(theta)[1])
[line3] = ax.plot(w,a(theta)[2])
ax.plot(w,np.zeros_like(w),'--',alpha = 0.6)
ax.set_xlim([-4, 4])
#draw 3 roots as a function of weyl energy w

theta_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03]) #draw slider
theta_slider = Slider(theta_slider_ax, r'$\theta$', 0, np.pi, valinit=theta)

def sliders_on_changed(val):
    '''
    activate the controling of the parameter theta
    ------------
    val = theta
    '''
    line1.set_ydata(a(theta_slider.val)[0])
    line2.set_ydata(a(theta_slider.val)[1])
    line3.set_ydata(a(theta_slider.val)[2])
    #updating the parameter theta by sliding val = theta
    fig.canvas.draw_idle()
theta_slider.on_changed(sliders_on_changed)

plt.show()
