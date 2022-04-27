
'''
IMPORTS
'''
from matplotlib.pyplot import imread
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

import PhotoProcessing as pp


im = imread("images/shapes.jpg") # Load an image
im = im/255 # Normalize the image (black and white scale with the largest value being 255)
# print(im) # prints the image object (which is stored as a 2d numpy.ndarray) to the console

fig = plt.figure()
view = plt.imshow(im, cmap = 'Greys_r') # plots the image using a greyscale color map with white = 1, black = 0
plt.title("time = 0.0")
plt.colorbar() # adds a color bar to show the scale of the plotted values
# plt.show() # makes the plot visible in a separate window

total_time = 0.0

# for i in range(100):
#     im = heatEquation(im, 0.2, 0.0001)
#     im = im/np.max(im)

def animate(frames):
    global im, total_time
    dt = 0.5

    original = np.copy(im)

    # im = pp.modifiedLevelSet(im, original, 1, dt, 0.5, 0.000001)
    im = pp.levelSet(im, 1, dt, 0.000001)
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