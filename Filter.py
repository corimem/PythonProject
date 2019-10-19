
#prompts user for image path and opens image in a seperate window. Closes 

import cv2

name=input('input name of image:')

img=cv2.imread(name)



editimg=img
#copies the first list
import numpy as np
img=img.tolist()
editimg=editimg.tolist()
print (img)

for i in range(len(img)):
    x=img[i]
    for a in range(0,len(x)):
        


        for n in range (0,len(x[1])):
            h_of_nR=((1/3)*x[n+2][0])+((1/3)*x[n+1][0])+((1/3)*x[n][0])+((1/3)*x[n-1][0])+((1/3)*x[n-2][0])
            h_of_nG=((1/3)*x[n+2][1])+((1/3)*x[n+1][1])+((1/3)*x[n][1])+((1/3)*x[n-1][1])+((1/3)*x[n-2][1])
            h_of_nB=((1/3)*x[n+2][2])+((1/3)*x[n+1][2])+((1/3)*x[n][2])+((1/3)*x[n-1][2])+((1/3)*x[n-2][2])
        #accesses each R,G,and B value
            editimg[i][a][0]=h_of_nR
            editimg[i][a][1]=h_of_nG
            editimg[i][a][2]=h_of_nB

editimg=np.asarray(editimg)     
editimg=editimg.astype(np.uint8)   
cv2.imshow('image', editimg)

cv2.waitKey(0)

cv2.destroyAllWindows()   
