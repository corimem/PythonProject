#prompts user for image path and opens image in a seperate window. Closes 
import cv2
name=input('input name of image: ')
img=cv2.imread(name)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()        

degree=input('Enter how many degrees you want to rotate. Enter 90, 180, 270 or mirror: ')


while degree.lower()!='mirror' and degree!='90' and degree!='180' and degree!='270':
        degree=input('Enter how many degrees you want to rotate. Enter 90, 180, 270 or mirror: ')



