#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('./lena.bmp')
fig = plt.figure()
viewer=fig.add_subplot(2,1,1)
viewer.axes.get_yaxis().set_visible(False)
viewer.axes.get_xaxis().set_visible(False)
viewer.set_title('before')
plt.imshow(image)

# R * 0.299 + G * 0.578 + B * 0.114
newImage=np.zeros(image.shape)
for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        color=image[x,y][0]* 0.299+image[x,y][1]* 0.578+image[x,y][2]* 0.114 
        newImage[x,y]=[225,255,255] if color>120 else [0,0,0]

viewer=fig.add_subplot(2,1,2)
viewer.axes.get_yaxis().set_visible(False)
viewer.axes.get_xaxis().set_visible(False)
viewer.set_title('after')
plt.imshow(newImage)
plt.show()
