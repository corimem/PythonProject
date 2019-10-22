#opens modules used, cv2 for image viewing and saving, numpy for matrix manipulations
import cv2
import numpy as np

#prompts user to input the name of the image file and the what they want to do to the image
name=input('input name of image: ')
do=input('What do you want to do to the image? Input R for rotate, G for grayscale or S for smooth:')
#reads image
img=cv2.imread(name)
#saves a copy of the image for manipulation
editimg=img.copy()
#gets number of columns in image
C=(int(len(img[0])))
#gets number of rows in image
R=(int(len(img)))


def smooth(R,C,img,editimg):
    for a in range(1,R-2):
        for b in range(1,C-2):
            for d in range(0,2):
                editimg[a][b][d]=(np.sum((1/9)*(np.array(                    
                [[((img[a-1][b-1][d])),((img[a-1][b][d])),((img[a-1][b+1][d]))],
                [((img[a][b-1][d])),((img[a][b][d])),((img[a][b+1][d]))],
                [((img[a+1][b-1][d])),((img[a+1][b][d])),((img[a+1][b+1][d]))]]))))
                #puts edited image data in correct type for viewing            
                editimg=editimg.astype(np.uint8)   
                return editimg

def rotate(R,C,img,editimg):
    
    rot=input('Enter how many degrees you want to rotate. Enter 90, 180, 270 or mirror: ')
    while rot.lower()!='mirror' and degree!='90' and degree!='180' and degree!='270':
        rot=input('Enter how many degrees you want to rotate. Enter 90, 180, 270 or mirror: ')
    if rot=='90':
        editimg=np.zeros((C,R,3), dtype=int)
        for j in range(R):
            for i in range(C-1,-1,-1):  
                    editimg[i][j]=img[j][-i] 
    if rot=='180':
        editimg=np.zeros((R,C,3), dtype=int)
        for i in range(R):
            for j in range(C):
                editimg[i, C-1-j] = img[R-1-i, j]
    if rot=='270':
        editimg=np.zeros((R,C,3), dtype=int)
        for i in range(R):
            for j in range(C):
                editimg[i, C-1-j] = img[R-1-i, j]
        for j in range(R):
            for i in range(C-1,-1,-1):  
                    editimg[i][j]=img[j][-i] 
    if rot=='mirror':
        editimg=np.zeros((R,C,3), dtype=int)
        for i in range(R):
            for j in range(C):
                editimg[i][j]=img[i][-j]
    return editimg

#define a function "gray()" that manipulates each R,B, and G value and adds them together into one value
#This creates a two dimensional gray scale matrix
def gray(R,C,img,editimg):
    for R in range(0,len(img)):
        for C in range(0,len(img[i])):            
            editimg[i][j]=img[i][j][0]*(299/1000)+img[i][j][1]*(587/1000)+img[i][j][2]*(114/1000)
    
    return editimg

if do == 'R':
    editimg=rotate(R,C,img,editimg)
if do == 'G':
    editimg=gray(R,C,img,editimg)
if do == 'S':
    editimg=smooth(R,C,img,editimg)

cv2.imshow('image',editimg)
cv2.waitKey(0)
cv2.destroyAllWindows() 
