#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

class ImageFilter:
    def make_saltNoise(self, image,noise):
        newImage=np.zeros(image.shape,np.uint8)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                rand=random.random()
                if(rand<noise):
                    if((i+j)%2):
                        newImage[i,j]=[0,0,0]
                    else:
                        newImage[i,j]=[255,255,255]
                else:
                    newImage[i,j]=image[i,j]
        return newImage

    def make_avaverageFilter(self,image):
        newImage=np.zeros(image.shape,np.uint8)
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                rgb_array=np.zeros(3)
                for rx in range(i-1,i+2):
                    for ry in range(j-1,j+2):
                        np.add(rgb_array,image[rx,ry],rgb_array)
                newImage[i,j]=rgb_array/9

        return newImage
    def make_guassianFilter(self,image):
        image=np.array(image,np.int32)
        newImage=np.zeros(image.shape,np.uint8)
        mask=np.array([[1,2,1],[2,4,2],[1,2,1]])
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                rgb_array=np.zeros(3)
                for rx in range(i-1,i+2):
                    for ry in range(j-1,j+2):

                        np.add(rgb_array,image[rx,ry]*mask[rx-i+1,ry-j+1],rgb_array)
                
                newImage[i,j]=rgb_array/16

        return newImage

    def make_medianFilter(self,image):
        image=np.array(image,np.int32)
        newImage=np.zeros(image.shape,np.uint8)
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):    
                newImage[i,j]=[sorted(image[i-1:i+2,j-1:j+2][:,:,0].reshape(9))[4],sorted(image[i-1:i+2,j-1:j+2][:,:,1].reshape(9))[4],sorted(image[i-1:i+2,j-1:j+2][:,:,2].reshape(9))[4]]

        return newImage


    
if __name__ == '__main__':
    max_count=12
    image = mpimg.imread('./image/lena.bmp')
    fliter=ImageFilter()
    
    fig = plt.figure()
    fig.set_size_inches(4,max_count*4)

    temp=fig.add_subplot(max_count,1,1)
    temp.set_title('lena')
    plt.imshow(image)

    temp=fig.add_subplot(max_count,1,2)
    temp.set_title('noise lena')
    noise_image=fliter.make_saltNoise(image,0.05)
    plt.imshow(noise_image)

    temp=fig.add_subplot(max_count,1,3)
    temp.set_title('avaverageFilter')
    plt.imshow(fliter.make_avaverageFilter(noise_image))

    temp=fig.add_subplot(max_count,1,4)
    temp.set_title('guassianFilter')
    plt.imshow(fliter.make_guassianFilter(noise_image))   
    
    temp=fig.add_subplot(max_count,1,5)
    temp.set_title('medianFilter')
    plt.imshow(fliter.make_medianFilter(noise_image))   

    plt.show()
