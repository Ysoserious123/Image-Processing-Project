import PhotoProcessing as ip
from matplotlib.pyplot import axes, imread
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

#QUESTION 1

# fig,ax=plt.subplots(2,3)
# im = imread("images/daisy.jpg")
# im=im/255
# org, im1=ip.processImage(im,'heat',5,.2)
# org, im2=ip.processImage(im,'heat',10,.2)
# org, im3=ip.processImage(im,'heat',15,.2)
# ax[0,0].set_title("original")
# ax[0,1].set_title("original")
# ax[0,2].set_title("original")
# ax[1,0].set_title("t=5")
# ax[1,1].set_title("t=10")
# ax[1,2].set_title("t=15")
# ax[0,0].imshow(org,cmap='Greys_r')
# ax[0,1].imshow(org,cmap='Greys_r')
# ax[0,2].imshow(org,cmap='Greys_r')
# ax[1,0].imshow(im1,cmap='Greys_r')
# ax[1,1].imshow(im2,cmap='Greys_r')
# ax[1,2].imshow(im3,cmap='Greys_r')
# fig.suptitle("Heat Equation")
#plt.show()

fig,ax=plt.subplots(1,2)
im=imread("images/happyfacenoiseheavy.jpg")
im=im/255
org, im1=ip.processImage(im,'modified-level-set',10,.5,epsilon=0.00001,alpha=.01)
ax[0].set_title("original")
ax[1].set_title("t=10,a=.2")
ax[0].imshow(org,cmap='Greys_r')
ax[1].imshow(im1,cmap='Greys_r')
plt.show()

