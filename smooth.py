import numpy as np
import cv2

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
