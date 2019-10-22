#prompts user for image path and opens image in a seperate window. Closes 
import cv2
import numpy as np
from smooth import smooth
from rotate import rotate
from grayscale import gray

name=input('input name of image: ')
do=input('What do you want to do to the image? Input R for rotate, G for grayscale or S for smooth:')

img=cv2.imread(name)
editimg=img.copy()

C=(int(len(img[0])))
R=(int(len(img)))

if do == 'R':
    editimg=rotate(R,C,img,editimg)
if do == 'G':
    editimg=gray(R,C,img,editimg)
if do == 'S':
    editimg=smooth(R,C,img,editimg)

cv2.imshow('image',editimg)
cv2.waitKey(0)
cv2.destroyAllWindows() 
