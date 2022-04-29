import PhotoProcessing as ip
from matplotlib.pyplot import axes, imread
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

# ## Load image first, and uncomment question you want to run
# im = imread("images/daisy.jpg")
# if np.ndim(im) > 2:
#     R, G, B = im[:,:,0], im[:,:,1], im[:,:,2]
#     im = 0.2989 * R + 0.5870 * G + 0.1140 * B

# # # #QUESTION 1

# fig,ax=plt.subplots(3,3, figsize = (8, 6))
# im = im/255
# org, im1=ip.processImage(im,'heat',5,.2)
# org, im2=ip.processImage(im,'heat',10,.2)
# org, im3=ip.processImage(im,'heat',20,.2)
# _, im4 = ip.processImage(im1, 'shock-filter', 100, 0.5)
# _, im5 = ip.processImage(im2, 'shock-filter', 100, 0.5)
# _, im6 = ip.processImage(im3, 'shock-filter', 100, 0.5)
# ax[0,0].set_title("original")
# ax[0,1].set_title("original")
# ax[0,2].set_title("original")
# ax[1,0].set_title("t=5, dt = 0.2")
# ax[1,1].set_title("t=10, dt = 0.2")
# ax[1,2].set_title("t=20, dt = 0.2")
# ax[2,0].set_title("t=105, dt = 0.5")
# ax[2,1].set_title("t=110, dt = 0.5")
# ax[2,2].set_title("t=120, dt = 0.5")
# ax[0,0].imshow(org,cmap='Greys_r')
# ax[0,1].imshow(org,cmap='Greys_r')
# ax[0,2].imshow(org,cmap='Greys_r')
# ax[1,0].imshow(im1,cmap='Greys_r')
# ax[1,1].imshow(im2,cmap='Greys_r')
# ax[1,2].imshow(im3,cmap='Greys_r')
# ax[2,0].imshow(im4,cmap='Greys_r')
# ax[2,1].imshow(im5,cmap='Greys_r')
# ax[2,2].imshow(im6,cmap='Greys_r')
# fig.suptitle("Heat (row 2) and Shock Filter (row 3) Equation Daisy")
# plt.show()

# fig,ax=plt.subplots(3,3, figsize=(8,6))
# im = imread("images/tile.jpg")
# im=im/255
# org, im1=ip.processImage(im,'heat',5,.2)
# org, im2=ip.processImage(im,'heat',10,.2)
# org, im3=ip.processImage(im,'heat',20,.2)
# _, im4 = ip.processImage(im1, 'shock-filter', 100, 0.5)
# _, im5 = ip.processImage(im2, 'shock-filter', 200, 0.5)
# _, im6 = ip.processImage(im3, 'shock-filter', 300, 0.5)
# ax[0,0].set_title("original")
# ax[0,1].set_title("original")
# ax[0,2].set_title("original")
# ax[1,0].set_title("t=5, dt=.2")
# ax[1,1].set_title("t=10, dt=.2")
# ax[1,2].set_title("t=20, dt=.2")
# ax[2,0].set_title("t=105, dt = 0.5")
# ax[2,1].set_title("t=210, dt = 0.5")
# ax[2,2].set_title("t=320, dt = 0.5")
# ax[0,0].imshow(org,cmap='Greys_r')
# ax[0,1].imshow(org,cmap='Greys_r')
# ax[0,2].imshow(org,cmap='Greys_r')
# ax[1,0].imshow(im1,cmap='Greys_r')
# ax[1,1].imshow(im2,cmap='Greys_r')
# ax[1,2].imshow(im3,cmap='Greys_r')
# ax[2,0].imshow(im4,cmap='Greys_r')
# ax[2,1].imshow(im5,cmap='Greys_r')
# ax[2,2].imshow(im6,cmap='Greys_r')
# fig.suptitle("Heat (row 2) & Shock Filter (row 3) Equation Tile")
# plt.show()

# #QUESTION 2

# fig,ax=plt.subplots(1,6)
# im=imread("images/peanut.jpg")
# im=im/225
# org, im1=ip.processImage(im,'level-set',50,.5,epsilon=.000001)
# org, im2=ip.processImage(im,'level-set',150,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',300,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',500,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',700,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=50, dt=.5")
# ax[2].set_title("t=150, dt=.5")
# ax[3].set_title("t=300, dt=.5")
# ax[4].set_title("t=500, dt=.5")
# ax[5].set_title("t=700, dt=.5")
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
# org, im5=ip.processImage(im,'level-set',350,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=25, dt=.5")
# ax[2].set_title("t=50, dt=.5")
# ax[3].set_title("t=150, dt=.5")
# ax[4].set_title("t=250, dt=.5")
# ax[5].set_title("t=350, dt=.5")
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
# org, im2=ip.processImage(im,'level-set',150,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',300,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',450,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',900,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=25, dt=.5")
# ax[2].set_title("t=150, dt=.5")
# ax[3].set_title("t=300, dt=.5")
# ax[4].set_title("t=450, dt=.5")
# ax[5].set_title("t=900, dt=.5")
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
# org, im1=ip.processImage(im,'level-set',100,.5,epsilon=.000001)
# org, im2=ip.processImage(im,'level-set',600,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',1000,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',6500,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',8000,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=100, dt=.5")
# ax[2].set_title("t=600, dt=.5")
# ax[3].set_title("t=1000, dt=.5")
# ax[4].set_title("t=6500, dt=.5")
# ax[5].set_title("t=8000, dt=.5")
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
# org, im1=ip.processImage(im,'level-set',10,.5,epsilon=.000001)
# org, im2=ip.processImage(im,'level-set',25,.5,epsilon=.000001)
# org, im3=ip.processImage(im,'level-set',35,.5,epsilon=.000001)
# org, im4=ip.processImage(im,'level-set',50,.5,epsilon=.000001)
# org, im5=ip.processImage(im,'level-set',80,.5,epsilon=.000001)
# ax[0].set_title("original")
# ax[1].set_title("t=10, dt=.5")
# ax[2].set_title("t=25, dt=.5")
# ax[3].set_title("t=35, dt=.5")
# ax[4].set_title("t=50, dt=.5")
# ax[5].set_title("t=80, dt=.5")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# ax[2].imshow(im2,cmap='Greys_r')
# ax[3].imshow(im3,cmap='Greys_r')
# ax[4].imshow(im4,cmap='Greys_r')
# ax[5].imshow(im5,cmap='Greys_r')
# fig.suptitle("Level Set I Love Math")
# plt.show()




# #QUESTION 3



# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacelight.jpg")
# im=im/255
# org, im1=ip.processImage(im,'level-set',15,.5,epsilon=0.0001)
# ax[0].set_title("original")
# ax[1].set_title("t=15, dt=.5")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Level Set Light Noise")
# plt.show()


# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacenoisemedium.jpg")
# im=im/255
# org, im1=ip.processImage(im,'level-set',10,.5,epsilon=0.00001)
# ax[0].set_title("original")
# ax[1].set_title("t=10, dt=.5")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Level Set Medium Noise")
# plt.show()



# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacenoiseheavy.jpg")
# im=im/255
# org, im1=ip.processImage(im,'level-set',15,.5,epsilon=0.00001)
# ax[0].set_title("original")
# ax[1].set_title("t=15, dt=.5")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Level Set Heavy Noise")
# plt.show()

# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacelight.jpg")
# im=im/255
# org, im1=ip.processImage(im,'modified-level-set',15,.5,epsilon=0.00001,alpha=.01)
# ax[0].set_title("original")
# ax[1].set_title("t=15,a=.01, dt=.5")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Modified Level Set Light Noise")
# plt.show()

# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacenoisemedium.jpg")
# im=im/255
# org, im1=ip.processImage(im,'modified-level-set',10,.5,epsilon=0.00001,alpha=.001)
# ax[0].set_title("original")
# ax[1].set_title("t=10,a=.001, dt=.5")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Modified Level Set Medium Noise")
# plt.show()

# fig,ax=plt.subplots(1,2)
# im=imread("images/happyfacenoiseheavy.jpg")
# im=im/255
# org, im1=ip.processImage(im,'modified-level-set',15,.5,epsilon=0.00001,alpha=.01)
# ax[0].set_title("original")
# ax[1].set_title("t=15,a=.01, dt=.5")
# ax[0].imshow(org,cmap='Greys_r')
# ax[1].imshow(im1,cmap='Greys_r')
# fig.suptitle("Modified Level Set Heavy Noise")
# plt.show()


#QUESTION 4

fig,ax=plt.subplots(1,3)
im=imread("images/stocktonospreyblurnoise.jpg")
im=im/255
org, im1=ip.processImage(im,'modified-level-set',500,.5,epsilon=0.00001,alpha=.05)
_, im2 = ip.processImage(im1,'shock-filter', 900, 0.5)
ax[0].set_title("original")
ax[1].set_title("MLS t=500, a=.05, dt=.5")
ax[2].set_title(" Shock Filter t=1400, dt=.5")
ax[0].imshow(org,cmap='Greys_r')
ax[1].imshow(im1,cmap='Greys_r')
ax[2].imshow(im2,cmap='Greys_r')
fig.suptitle("Modified Level Set and Shock Stockton Osprey")
plt.show()


# # # QUESTION 5
# # im = imread("images/jayden.jpg")
# # if np.ndim(im) > 2:
# #     R, G, B = im[:,:,0], im[:,:,1], im[:,:,2]
# #     im = 0.2989 * R + 0.5870 * G + 0.1140 * B


# # fig,ax=plt.subplots(1,2, figsize = (8, 6))
# # im = im/255
# # org, im1=ip.processImage(im,'shock-filter',5000, 0.5)

# # ax[0].set_title("original")
# # ax[1].set_title("original")

# # ax[0].imshow(org,cmap='Greys_r')
# # ax[1].imshow(org,cmap='Greys_r')

# # fig.suptitle("Shock Filter Jayden")
# # plt.show()

