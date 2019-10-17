#prompts user for image path and opens image in a seperate window. Closes 
import cv2
name=input('input name of image:')
img=cv2.imread(name)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()        
