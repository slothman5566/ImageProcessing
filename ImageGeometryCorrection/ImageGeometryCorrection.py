#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class Transformation:
    def offset_transform(self, image,offset_x,offset_y):
        new_image=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                if(x+offset_x>=image.shape[0] or x+offset_x<0):
                    continue
                if(y+offset_y>=image.shape[1] or y+offset_y<0):
                    continue
                new_image[x+offset_x,y+offset_y]=image[x,y]
        return new_image.astype(np.uint8)

    def transport_transform(self, image):
        new_image=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                
                new_image[x,y]=image[y,x]
        return new_image.astype(np.uint8)

    def mirror_transform(self, image):
        new_image=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                
                new_image[x,y]=image[x,image.shape[1]-y-1]
        return new_image.astype(np.uint8)

    def nearestInterpolation_transform(self, image,sacle):    
        new_image=np.zeros(image.shape)
        resize_width=int(image.shape[0]*sacle)
        resize_height=int(image.shape[1]*sacle)
        new_image=np.zeros((resize_width,resize_height,3))
        for x in range(resize_width):
            sx=int(x/sacle)
            if(sx>=image.shape[0]):
                    continue
            for y in range(resize_height):
                sy=int(y/sacle)
                if(sy >=image.shape[1] ):
                    continue
                new_image[x,y]=image[sx,sy]

        return new_image.astype(np.uint8)

    def bilinearInterpolation_transform(self,image,sacle):
        resize_width=int(image.shape[0]*sacle)
        resize_height=int(image.shape[1]*sacle)
        new_image=np.zeros((resize_width,resize_height,3))
        value=[0,0,0]
        for i in range(resize_width):
            for j in range(resize_height):
                x = i/sacle
                y = j/sacle
                p=int((i+0.0)/sacle-x)
                q=int((j+0.0)/sacle-y)
                x=int(x)-1
                y=int(y)-1
                for k in range(3):
                    if x+1<image.shape[0] and y+1<image.shape[1]:
                        value[k]=int(image[x,y][k]*(1-p)*(1-q)+image[x,y+1][k]*q*(1-p)+image[x+1,y][k]*(1-q)*p+image[x+1,y+1][k]*p*q)
                new_image[i, j] = (value[0], value[1], value[2])
        return new_image.astype(np.uint8)

if __name__ == '__main__':
    max_count=7
    image = mpimg.imread('./image/lena.bmp')
    transformer=Transformation()
    
    fig = plt.figure()
    fig.set_size_inches(4,max_count*4)

    temp=fig.add_subplot(max_count,1,1)
    temp.set_title('lena')
    plt.imshow(image)

    temp=fig.add_subplot(max_count,1,2)
    temp.set_title('offset')
    plt.imshow(transformer.offset_transform(image,-100,10))

    temp=fig.add_subplot(max_count,1,3)
    temp.set_title('transport')
    plt.imshow(transformer.transport_transform(image))

    temp=fig.add_subplot(max_count,1,4)
    temp.set_title('mirror')
    plt.imshow(transformer.mirror_transform(image))

    temp=fig.add_subplot(max_count,1,5)
    temp.set_title('nearestInterpolation_transform')
    plt.imshow(transformer.nearestInterpolation_transform(image,2))

    temp=fig.add_subplot(max_count,1,6)
    temp.set_title('Bilinear_interpolation')
    plt.imshow(transformer.bilinearInterpolation_transform(image,0.8))

    
    plt.show()