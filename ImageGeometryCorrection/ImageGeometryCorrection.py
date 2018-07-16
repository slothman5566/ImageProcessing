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

    def scale_transform(self, image,sacle):    
        new_image=np.zeros(image.shape)
        for x in range(image.shape[0]):
            sx=int(x*sacle)
            if(sx>=image.shape[0]):
                    continue
            for y in range(image.shape[1]):
                sy=int(y*sacle)
                if(sy >=image.shape[1] ):
                    continue
                new_image[x,y]=image[sx,sy]
        return new_image.astype(np.uint8)


if __name__ == '__main__':
    max_count=5
    image = mpimg.imread('./image/lena.bmp')
    transformer=Transformation()
    
    fig = plt.figure()
    fig.set_size_inches(4,max_count*4)

    temp=fig.add_subplot(max_count,1,1)
    temp.set_title('lena')
    plt.imshow(image)

    # temp=fig.add_subplot(max_count,1,2)
    # temp.set_title('offset')
    # plt.imshow(transformer.offset_transform(image,-100,10))

    # temp=fig.add_subplot(max_count,1,3)
    # temp.set_title('transport')
    # plt.imshow(transformer.transport_transform(image))

    # temp=fig.add_subplot(max_count,1,4)
    # temp.set_title('mirror')
    # plt.imshow(transformer.mirror_transform(image))

    temp=fig.add_subplot(max_count,1,5)
    temp.set_title('mirror')
    plt.imshow(transformer.scale_transform(image,2))

    plt.show()