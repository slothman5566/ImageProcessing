#%%
import sys
sys.path.insert(0, 'D:\ImageProcessing')
import ImageEnhancement.IntensityTransformation as it
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
class  MorphologicalImageProcessor:
    def erosion(self, image):
        newImage=np.zeros(image.shape)
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                if (any(image[i-1:i+2,j-1:j+2][:,:,0].reshape(9))):
                    newImage[i,j]=[255,255,255]
        return newImage

    def dilation(self,image):
        newImage=np.zeros(image.shape)
        for i in range(1,image.shape[0]-1):
            for j in range(1,image.shape[1]-1):
                if (all(image[i-1:i+2,j-1:j+2][:,:,0].reshape(9))):
                    newImage[i,j]=[255,255,255]
        return newImage


if __name__ == '__main__':
    max_count=5
    image = mpimg.imread('./image/lena.bmp')
    transfer=it.Transformation()
    processor=MorphologicalImageProcessor()
    fig = plt.figure()
    fig.set_size_inches(4,max_count*4)

    temp=fig.add_subplot(max_count,1,1)
    temp.set_title('lena')
    plt.imshow(image)
    g_image=transfer.gray_transform(image)
    b_image=transfer.binarization_transform(g_image)

    temp=fig.add_subplot(max_count,1,2)
    temp.set_title('binary lena')
    plt.imshow(b_image)

    
    temp=fig.add_subplot(max_count,1,3)
    temp.set_title('erosion')
    plt.imshow(processor.erosion(b_image)) 

    temp=fig.add_subplot(max_count,1,4)
    temp.set_title('dilation')
    plt.imshow(processor.dilation(b_image)) 

    plt.show()