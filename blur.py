import cv2
import numpy as np
#asks user for the image file 
name=input('input name of image:')
#reads image file 
img=cv2.imread(name)
#creates a copy of the image file and saves it as editimg, which will be the edited image 
editimg=img.copy()
#gets number of colums
C=(int(len(img[0])))
#gets number of rows
R=(int(len(img)))
#averages the 9 red, green, or blue values in a square surrounding each pixel and assigns the averaged value as the new red, green, or blue value in edited image
for a in range(1,R-2):
    for b in range(1,C-2):
        for d in range(0,2):
            editimg[a][b][d]=(np.sum((1/9)*(np.array(                    
            [[((img[a-1][b-1][d])),((img[a-1][b][d])),((img[a-1][b+1][d]))],
            [((img[a][b-1][d])),((img[a][b][d])),((img[a][b+1][d]))],
            [((img[a+1][b-1][d])),((img[a+1][b][d])),((img[a+1][b+1][d]))]]))))
#puts edited image data in correct type for viewing            
editimg=editimg.astype(np.uint8)   

#shows edited image
cv2.imshow('image', editimg)

cv2.waitKey(0)

cv2.destroyAllWindows()   
