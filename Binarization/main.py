#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class Binarization:
    #Gray= R * 0.299 + G * 0.578 + B * 0.114
    def process(self,image):
        
        newImage=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                gray=image[x,y][0]* 0.299+image[x,y][1]* 0.578+image[x,y][2]* 0.114 
                newImage[x,y]=[225,255,255] if gray>120 else [0,0,0]
        return newImage

    def process_with_threshold(self, image):
        newImage=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                gray=image[x,y][0]* 0.299+image[x,y][1]* 0.578+image[x,y][2]* 0.114 
                if(gray>200):
                    newImage[x,y]=[225,255,255]
                elif(gray>150):
                    newImage[x,y]=[0,0,0]
                elif(gray>100):
                    newImage[x,y]=[225,255,255]
                elif(gray>50):
                    newImage[x,y]=[0,0,0]
                
        return newImage

def show_image(image_list):
    fig = plt.figure()
    fig.set_size_inches(10,10)
    for i,v in enumerate(image_list):
        viewer=fig.add_subplot(len(image_list),1,i+1)
        viewer.axes.get_yaxis().set_visible(False)
        viewer.axes.get_xaxis().set_visible(False)
        plt.imshow(v)
    plt.margins(0.05, 0.1)
    plt.show()

if __name__ == '__main__':
    image = mpimg.imread('./image/lena.bmp')
    processor=Binarization()    
    image_list=[]
    image_list.append(image)
    image_list.append(processor.process(image))
    image_list.append(processor.process_with_threshold(image))
    show_image(image_list)
