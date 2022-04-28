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
# org, im3=ip.processImage(im,'heat',20,.2)
# ax[0,0].set_title("original")
# ax[0,1].set_title("original")
# ax[0,2].set_title("original")
# ax[1,0].set_title("t=5")
# ax[1,1].set_title("t=10")
# ax[1,2].set_title("t=20")
# ax[0,0].imshow(org,cmap='Greys_r')
# ax[0,1].imshow(org,cmap='Greys_r')
# ax[0,2].imshow(org,cmap='Greys_r')
# ax[1,0].imshow(im1,cmap='Greys_r')
# ax[1,1].imshow(im2,cmap='Greys_r')
# ax[1,2].imshow(im3,cmap='Greys_r')
# fig.suptitle("Heat Equation Daisy")
# plt.show()

# fig,ax=plt.subplots(2,3)
# im = imread("images/tile.jpg")
# im=im/255
# org, im1=ip.processImage(im,'heat',5,.2)
# org, im2=ip.processImage(im,'heat',10,.2)
# org, im3=ip.processImage(im,'heat',20,.2)
# ax[0,0].set_title("original")
# ax[0,1].set_title("original")
# ax[0,2].set_title("original")
# ax[1,0].set_title("t=5")
# ax[1,1].set_title("t=10")
# ax[1,2].set_title("t=20")
# ax[0,0].imshow(org,cmap='Greys_r')
# ax[0,1].imshow(org,cmap='Greys_r')
# ax[0,2].imshow(org,cmap='Greys_r')
# ax[1,0].imshow(im1,cmap='Greys_r')
# ax[1,1].imshow(im2,cmap='Greys_r')
# ax[1,2].imshow(im3,cmap='Greys_r')
# fig.suptitle("Heat Equation Tile")
# plt.show()

#QUESTION 2

# fig,ax=plt.subplots(1,6)
# im=imread("images/peanut.jpg")
# im=im/225
# org, im1=ip.processImage(im,'level-set',25,.5,epsilon=.000001)
# org, im2=ip.processImage(im,'level-set',50,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',150,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',250,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',500,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=25")
# ax[2].set_title("t=50")
# ax[3].set_title("t=150")
# ax[4].set_title("t=250")
# ax[5].set_title("t=500")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# ax[2].imshow(im2,cmap='Greys_r')
# ax[3].imshow(im3,cmap='Greys_r')
# ax[4].imshow(im4,cmap='Greys_r')
# ax[5].imshow(im5,cmap='Greys_r')
# fig.suptitle("Level Set Peanut")
# plt.show()




# fig,ax=plt.subplots(1,6)
# im=imread("images/shapes.jpg")
# im=im/225
# org, im1=ip.processImage(im,'level-set',25,.5,epsilon=.000001)
# org, im2=ip.processImage(im,'level-set',50,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',150,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',250,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',500,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=25")
# ax[2].set_title("t=50")
# ax[3].set_title("t=150")
# ax[4].set_title("t=250")
# ax[5].set_title("t=500")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# ax[2].imshow(im2,cmap='Greys_r')
# ax[3].imshow(im3,cmap='Greys_r')
# ax[4].imshow(im4,cmap='Greys_r')
# ax[5].imshow(im5,cmap='Greys_r')
# fig.suptitle("Level Set Shapes")
# plt.show()




# fig,ax=plt.subplots(1,6)
# im=imread("images/boundaries.jpg")
# im=im/225
# org, im1=ip.processImage(im,'level-set',25,.5,epsilon=.000001)
# org, im2=ip.processImage(im,'level-set',50,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',150,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',250,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',500,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=25")
# ax[2].set_title("t=50")
# ax[3].set_title("t=150")
# ax[4].set_title("t=250")
# ax[5].set_title("t=500")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# ax[2].imshow(im2,cmap='Greys_r')
# ax[3].imshow(im3,cmap='Greys_r')
# ax[4].imshow(im4,cmap='Greys_r')
# ax[5].imshow(im5,cmap='Greys_r')
# fig.suptitle("Level Set Boundaries")
# plt.show()




# fig,ax=plt.subplots(1,6)
# im=imread("images/curvebdry.jpg")
# im=im/225
# org, im1=ip.processImage(im,'level-set',25,.5,epsilon=.000001)
# org, im2=ip.processImage(im,'level-set',50,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',150,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',250,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',500,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=25")
# ax[2].set_title("t=50")
# ax[3].set_title("t=150")
# ax[4].set_title("t=250")
# ax[5].set_title("t=500")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# ax[2].imshow(im2,cmap='Greys_r')
# ax[3].imshow(im3,cmap='Greys_r')
# ax[4].imshow(im4,cmap='Greys_r')
# ax[5].imshow(im5,cmap='Greys_r')
# fig.suptitle("Level Set Curved Boundary")
# plt.show()



# fig,ax=plt.subplots(1,6)
# im=imread("images/ilovemath.jpg")
# im=im/225
# org, im1=ip.processImage(im,'level-set',5,.5,epsilon=.000001)
# org, im2=ip.processImage(im,'level-set',10,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',15,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',25,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',30,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=5")
# ax[2].set_title("t=10")
# ax[3].set_title("t=15")
# ax[4].set_title("t=25")
# ax[5].set_title("t=30")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# ax[2].imshow(im2,cmap='Greys_r')
# ax[3].imshow(im3,cmap='Greys_r')
# ax[4].imshow(im4,cmap='Greys_r')
# ax[5].imshow(im5,cmap='Greys_r')
# fig.suptitle("Level Set I Love Math")
# plt.show()




#QUESTION 3



# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacelight.jpg")
# im=im/255
# org, im1=ip.processImage(im,'level-set',15,.5,epsilon=0.00001)
# ax[0].set_title("original")
# ax[1].set_title("t=15")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Level Set Light Noise")
# plt.show()


# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacenoisemedium.jpg")
# im=im/255
# org, im1=ip.processImage(im,'level-set',10,.5,epsilon=0.00001)
# ax[0].set_title("original")
# ax[1].set_title("t=10")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Level Set Medium Noise")
# plt.show()



# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacenoiseheavy.jpg")
# im=im/255
# org, im1=ip.processImage(im,'level-set',15,.5,epsilon=0.00001)
# ax[0].set_title("original")
# ax[1].set_title("t=15")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Level Set Heavy Noise")
# plt.show()

# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacelight.jpg")
# im=im/255
# org, im1=ip.processImage(im,'modified-level-set',10,.5,epsilon=0.00001,alpha=.01)
# ax[0].set_title("original")
# ax[1].set_title("t=10,a=.01")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Modified Level Set Light Noise")
# plt.show()

# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacenoisemedium.jpg")
# im=im/255
# org, im1=ip.processImage(im,'modified-level-set',10,.5,epsilon=0.00001,alpha=.001)
# ax[0].set_title("original")
# ax[1].set_title("t=10,a=.001")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Modified Level Set Medium Noise")
# plt.show()

# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacenoiseheavy.jpg")
# im=im/255
# org, im1=ip.processImage(im,'modified-level-set',10,.5,epsilon=0.00001,alpha=.01)
# ax[0].set_title("original")
# ax[1].set_title("t=10,a=.01")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Modified Level Set Heavy Noise")
# plt.show()


#QUESTION 4

fig,ax=plt.subplots(1,2)
im=imread("images/stocktonospreyblurnoise.jpg")
im=im/255
org, im1=ip.processImage(im,'level-set',15,.5,epsilon=0.00001)
ax[0].set_title("original")
ax[1].set_title("t=15")
ax[0].imshow(org,cmap='Greys_r')
ax[1].imshow(im1,cmap='Greys_r')
fig.suptitle("Level Set Stockton Osprey")
plt.show()
