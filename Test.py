import PhotoProcessing as ip
from matplotlib.pyplot import axes, imread
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

im = imread('images/woman.jpg')

if np.ndim(im) > 2:
    R, G, B = im[:,:,0], im[:,:,1], im[:,:,2]
    im = 0.2989 * R + 0.5870 * G + 0.1140 * B

im = im/255

fig, ax = plt.subplots(1, 2)

fig.suptitle("Shock-FIlter for t = 200, dt = 0.1")

org, im1 = ip.processImage(im, 'shock-filter', 200, 0.1)

# _, im2 = ip.processImage(im1, 'shock-filter', 100, 0.5)

ax[0].imshow(org, cmap = "Greys_r")
ax[1].imshow(im1, cmap = "Greys_r")
# ax[2].imshow(im2, cmap = "Greys_r")


# fig.text(0.25,0.1,'Seeing the effect of shock filter after applying level set is very difficult to see \nas this image has high resolution, making edges very thin. If you look closely you can see the effect\nof shock-filer around the chair, my shirtline, my eyes, and maybe a little in my hair.',transform=fig.transFigure)

plt.show()