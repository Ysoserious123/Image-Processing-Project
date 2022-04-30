
'''
IMPORTS
'''
from ipaddress import ip_address
from matplotlib.pyplot import imread
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

import PhotoProcessing as pp


im = imread("images/shapes.jpg") # Load an image

if np.ndim(im) > 2:
    R, G, B = im[:,:,0], im[:,:,1], im[:,:,2]
    im = 0.2989 * R + 0.5870 * G + 0.1140 * B

im = im/255 # Normalize the image (black and white scale with the largest value being 255)
# print(im) # prints the image object (which is stored as a 2d numpy.ndarray) to the console

fig = plt.figure(figsize=(8,8))
# mngr = plt.get_current_fig_manager()
# mngr.window.set_geometry(50,100,640, 545)

view = plt.imshow(im, cmap = 'Greys_r')

# title = fig.text(0, 0, "")

# print(type(title))

total_time = 0.0

original = np.copy(im)

def animate(frames):
    global im, total_time, original, fig

    if (total_time<400):
        dt = 0.5
        # im = pp.modifiedLevelSet(im, original, 1, dt, 0.00000001, 0.02)
        im = pp.levelSet(im, 1, dt, 0.000001)
        # im = pp.heatEquation(im, 1, dt)
        # im = pp.shockFilter(im, 1, dt)
    else:
        dt = 0.5
        im = pp.shockFilter(im, 1, dt)
    # im = pp.modifiedLevelSet(im, original, 1, dt, 0.00001, 0.01)
    # im = pp.levelSet(im, 1, dt, 0.000001)
    # im = pp.heatEquation(im, 1, dt)

    total_time += dt
    # title.set_text("time = %.2f, dt = %.2f" % (total_time, dt))
    plt.title("time = %.2f, dt = %.2f" % (total_time, dt))
    # print(im.shape)
    # print(im)
    view.set_data(im)

    return [view]

def run_animate():
    global fig
    anim = animation.FuncAnimation(fig, animate, frames = 300, interval = 1)
    # writervideo = animation.FFMpegWriter(fps = 60)
    # anim.save("test-figures/heat_then_shock-filter.gif", writer = writervideo)
    plt.show()
    return anim

run_animate()