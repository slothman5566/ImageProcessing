#%%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math

class Transformation:
    #Gray= R * 0.299 + G * 0.578 + B * 0.114
    def gray_transform(self,image):
        new_image=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                gray=(int)(image[x,y][0]* 0.299+image[x,y][1]* 0.578+image[x,y][2]* 0.114)
                new_image[x,y]=[gray,gray,gray]
        return new_image.astype(np.uint8)


    def grayhistogram_transform(self,image):
        hist=np.zeros(256)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                
                hist[image[x,y,0]]+=1
        return hist
        
    def binarization_transform(self, image):
        new_image=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                gray=(image[x,y][0]* 0.299+image[x,y][1]* 0.578+image[x,y][2]* 0.114)
                new_image[x,y]=[255,255,255] if gray>128 else [0,0,0]
        return new_image.astype(np.uint8)

    def binarization_transform_with_threshold(self, image):
        new_image=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                gray=image[x,y,0]
                if(gray>200):
                    new_image[x,y]=[255,255,255]
                elif(gray>150):
                    new_image[x,y]=[0,0,0]
                elif(gray>100):
                    new_image[x,y]=[255,255,255]
                elif(gray>50):
                    new_image[x,y]=[0,0,0]
                
        return new_image
   
    def linear_transform(self, image):
        hist=np.zeros(256)
        intercept=100
        gradient=0.7
        new_image=np.zeros(image.shape)
        for i in range(hist.size):
            temp=gradient*i+intercept
            hist[i]=int(round(255 if temp>255 else temp))
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                new_image[x,y]=[hist[image[x,y,0]],hist[image[x,y,0]],hist[image[x,y,0]]]

        return new_image.astype(np.uint8)

    def negative_transform(self, image):
        new_image=np.zeros(image.shape)
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                gray=0 if 255-image[x,y,0]<0 else 255-image[x,y,0]
                new_image[x,y]=[gray,gray,gray]
        return new_image.astype(np.uint8)

    # y= a+log(1+x)/b
    def log_transform(self, image):
        new_image=np.zeros(image.shape)
        a=25 
        b=0.025 
        hist=np.zeros(256)
        new_image=np.zeros(image.shape)
        for i in range(hist.size):
            temp=a+ math.log(1+i)/b

            hist[i]=int(round(255 if temp>255 else temp))
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                new_image[x,y]=[hist[image[x,y,0]],hist[image[x,y,0]],hist[image[x,y,0]]]
        return new_image.astype(np.uint8)

        # y=b^c(x-a)-1
    def exp_transform(self, image):
        new_image=np.zeros(image.shape)
        a=0.05 
        b=1.5 
        c=0.065
        hist=np.zeros(256)
        new_image=np.zeros(image.shape)
        for i in range(hist.size):
            temp=math.pow(b,c*(i-a))-1
            hist[i]=int(round(255 if temp>255 else temp))
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                new_image[x,y]=[hist[image[x,y,0]],hist[image[x,y,0]],hist[image[x,y,0]]]
        return new_image.astype(np.uint8)
    #y=a*x^b+c
    def power_transform(self, image):
        new_image=np.zeros(image.shape)
        a=1
        b=3.5 
        c=0
        hist=np.zeros(256)
        new_image=np.zeros(image.shape)
        for i in range(hist.size):
            temp=a*math.pow(i,b)+c
            hist[i]=int(round(255 if temp>255 else temp))
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                new_image[x,y]=[hist[image[x,y,0]],hist[image[x,y,0]],hist[image[x,y,0]]]
        return new_image.astype(np.uint8)
    '''
    y=  if x<x1 then  (y1/x1)*x
        if x1<x<x2 then (x-x1)(y2-y1)/(x2-x1)+y1
        if x>x2 then (x-x2)(255-y2)/(255-x2)+y2
    '''
    def level_transform(self, image):
        new_image=np.zeros(image.shape)
        x1=50.0
        x2=150.0
        y1=50.0
        y2=150.0
        hist=np.zeros(256)
        new_image=np.zeros(image.shape)
        for i in range(hist.size):
            temp=0.0
            if(i<x1):
                temp=(y1/x1)*i
            elif (i<x2):
                temp=(i-x1)*(y2-y1)/(x2-x1)+y1
            else:
                temp=(i-x2)*(255-y2)/(255-x2)+y2
            hist[i]=int(round(255 if temp>255 else temp))
        
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                new_image[x,y]=[hist[image[x,y,0]],hist[image[x,y,0]],hist[image[x,y,0]]]
        return new_image.astype(np.uint8)
    
    # v=255/(width*height)*sigma(i)
    def equalize_transform(self, image):
        new_image=np.zeros(image.shape)
        
        gray_hist=self.grayhistogram_transform(image)
        hist=np.zeros(256)
        new_image=np.zeros(image.shape)
        for i in range(hist.size):
            temp=sum(gray_hist[:i+1])
            hist[i]=int(255*temp/(image.size/3))
        for x in range(image.shape[0]):
            for y in range(image.shape[1]):
                new_image[x,y]=[hist[image[x,y,0]],hist[image[x,y,0]],hist[image[x,y,0]]]
        return new_image.astype(np.uint8)


if __name__ == '__main__':
    max_count=12
    image = mpimg.imread('./image/lena.bmp')
    transformer=Transformation()
    
    fig = plt.figure()
    fig.set_size_inches(4,max_count*4)

    temp=fig.add_subplot(max_count,1,1)
    temp.set_title('lena')
    plt.imshow(image)
    
    temp=fig.add_subplot(max_count,1,2)
    temp.set_title('gray lena')
    gray_image=transformer.gray_transform(image)
    plt.imshow(gray_image)

    temp=fig.add_subplot(max_count,1,3)
    temp.set_title('grayhistogram')
    plt.plot(transformer.grayhistogram_transform(gray_image),color = 'r')
    
    temp=fig.add_subplot(max_count,1,4)
    temp.set_title('binarization')
    plt.imshow(transformer.binarization_transform(image))

    temp=fig.add_subplot(max_count,1,5)
    temp.set_title('binarization_with_threshold')
    plt.imshow(transformer.binarization_transform_with_threshold(gray_image))

    temp=fig.add_subplot(max_count,1,6)
    temp.set_title('linear')
    plt.imshow(transformer.linear_transform(gray_image))

    temp=fig.add_subplot(max_count,1,7)
    temp.set_title('negative')
    plt.imshow(transformer.negative_transform(gray_image))

    temp=fig.add_subplot(max_count,1,8)
    temp.set_title('log_transform')
    plt.imshow(transformer.log_transform(gray_image))

    temp=fig.add_subplot(max_count,1,9)
    temp.set_title('exp_transform')
    plt.imshow(transformer.exp_transform(gray_image))

    temp=fig.add_subplot(max_count,1,10)
    temp.set_title('log_transform')
    plt.imshow(transformer.log_transform(gray_image))

    temp=fig.add_subplot(max_count,1,11)
    temp.set_title('level_transform')
    plt.imshow(transformer.level_transform(gray_image))

    temp=fig.add_subplot(max_count,1,12)
    temp.set_title('equalize_transform')
    plt.imshow(transformer.equalize_transform(gray_image))

    fig.tight_layout(pad=2)
    plt.show()
    