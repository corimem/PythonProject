#use OpenCV to read in the matrix of an image
import cv2
name=input('input name of image:')
img=cv2.imread(name)
cv2.waitKey(0)
cv2.destroyAllWindows()        

#define a function "gray()" that manipulates each R,B, and G value and adds them together into one value
#This creates a two dimensional gray scale matrix
def gray():
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):            
            img[i][j]=img[i][j][0]*(299/1000)+img[i][j][1]*(587/1000)+img[i][j][2]*(114/1000)
    
    return img

#Use OpenCV to display the image to a file named image.
img = gray()
cv2.imshow('Purdue_arch_600x308',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
