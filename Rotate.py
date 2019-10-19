import numpy as np
import cv2
name= input('input name of image:')
rot=input('input the desired rotation angle (90, 180, or 270) or mirror:')

img=cv2.imread(name)
C=(int(len(img[0])))
R=(int(len(img)))

if rot=='90' or rot=='180' or rot=='270' or rot=='mirror':
    if rot=='90':
        editimg=np.zeros((C,R,3),dtype=int)
        for i in range(R):
            for j in range(C):
                editimg[j][i] = img[i][j]
    if rot=='180':
        editimg=np.zeros((R,C,3), dtype=int)
        for i in range(R):
            for j in range(C):
                editimg[i, C-1-j] = img[R-1-i, j]
    if rot=='270':
        editimg1=np.zeros((C,R,3),dtype=int)
        for i in range(R):
            for j in range(C):
                editimg1[j][i] = img[i][j]
        editimg=np.zeros((C,R,3), dtype=int)
        for i in range(R):
            for j in range(C):
                editimg[C-1-j, i] = editimg1[j,R-1-i]
    if rot=='mirror':
        editimg=np.zeros((R,C,3), dtype=int)
        for i in range(R):
            editimg[C-1-j, i] = editimg[j,R-1-i]
else: print('error: invalid input. Enter a 90,180,270, or mirror')

editimg=editimg.astype(np.uint8)    
cv2.imshow('image', editimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

