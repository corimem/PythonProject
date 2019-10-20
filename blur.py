import cv2
import numpy as np
name=input('input name of image:')
img=cv2.imread(name)
editimg=img.copy()
C=(int(len(img[0])))
R=(int(len(img)))
for a in range(1,R-2):
    for b in range(1,C-2):
        for d in range(0,2):
            editimg[a][b][d]=(1/8)*(np.sum(np.array([[((img[a-1][b-1][d])),((img[a-1][b][d])),((img[a-1][b+1][d]))],[((img[a][b-1][d])),(-8*(img[a][b][d])),((img[a][b+1][d]))],[((img[a+1][b-1][d])),((img[a+1][b][d])),((img[a+1][b+1][d]))]])))
            editimg[a][b][d]=img[a][b][d]+editimg[a][b][d]
editimg=editimg.astype(np.uint8)   
cv2.imshow('image', editimg)

cv2.waitKey(0)

cv2.destroyAllWindows()   
