
'''
IMPORTS
'''
from ipaddress import ip_address
from matplotlib.pyplot import imread
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

import PhotoProcessing as pp


im = imread("images/blackhole.jpg") # Load an image

if np.ndim(im) > 2:
    R, G, B = im[:,:,0], im[:,:,1], im[:,:,2]
    im = 0.2989 * R + 0.5870 * G + 0.1140 * B

im = im/255 # Normalize the image (black and white scale with the largest value being 255)
# print(im) # prints the image object (which is stored as a 2d numpy.ndarray) to the console

fig = plt.figure()
view = plt.imshow(im, cmap = 'Greys_r')

total_time = 0.0
# fig, ax = plt.subplots(1, 2, figsize = (8, 6))
# total_time = 10.0
# dt = 0.5
# org, im = pp.processImage(im, 'modified-level-set', total_time, dt, epsilon = 0.00001, alpha = 0.01)
# # org, im = pp.runModifiedLevelSet(im, total_time, dt, 0.0001, 0.5)

# view = ax[1].imshow(im, cmap = 'Greys_r') # plots the image using a greyscale color map with white = 1, black = 0
# ax[0].imshow(org, cmap = "Greys_r")
# fig.suptitle("time = %.2f, dt = %.2f, alpha = %.2f" % (total_time, dt, 0.01))

# fig.colorbar(view, ax=ax) # adds a color bar to show the scale of the plotted values

# plt.show() # makes the plot visible in a separate window

# total_time = 0.0

# for i in range(100):
#     im = heatEquation(im, 0.2, 0.0001)
#     im = im/np.max(im)

original = np.copy(im)

def animate(frames):
    global im, total_time, original

    if (total_time<1):
        dt = 0.5
        im = pp.modifiedLevelSet(im, original, 1, dt, 0.00000001, 0.01)
        # im = pp.levelSet(im, 1, dt, 0.000001)
        # im = pp.heatEquation(im, 1, dt)
        # im = pp.shockFilter(im, 1, dt)
    else:
        dt = 0.5
        im = pp.shockFilter(im, 1, dt)
    # im = pp.modifiedLevelSet(im, original, 1, dt, 0.00001, 0.01)
    # im = pp.levelSet(im, 1, dt, 0.000001)
    # im = pp.heatEquation(im, 1, dt)

    total_time += dt
    plt.title("time = %.2f, dt = %.2f" % (total_time, dt))
    # print(im.shape)
    # print(im)
    view.set_data(im)

def run_animate():
    global fig
    anim = animation.FuncAnimation(fig, animate, frames = 100, interval = 1)
    plt.show()
    return anim

run_animate()