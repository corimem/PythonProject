


#opens modules used, cv2 for image viewing and saving, numpy for matrix manipulations
import cv2

import numpy as np



#imports os.path so we can use the function to check if it is a file in the directory

import os.path



name=input('Input name of image: ')

variable=str(os.path.isfile(name))



#a loop that runs while the file inputed is not saved in the directory 

while variable=='False':
    
    print('Invalid input')

    #askes for an input for the image 

    name=input('Input name of image: ')
    
    variable=str(os.path.isfile(name))
    

#defines the variable do  that allows the user to input what they want to do 

do=input('What do you want to do to the image? Input R for rotate, G for grayscale, or S for smooth: ') 


#reads image
img=cv2.imread(name)



#saves a copy of the image for manipulation
editimg=img.copy()



#gets number of columns in image
C=(int(len(img[0])))


#gets number of rows in image
R=(int(len(img)))



#Defines a function to blur the image with the arguments of the number of rows, the number of colums, the data of the image, and the copy of the image 
def smooth(R,C,img,editimg):

#    loops through the rows of the data of the image 
    for a in range(1,R-2):

#        loops through all the colums of the image 
        for b in range(1,C-2):

        
#           loops through the elements of each row and colum for R G B values for each pixel
            for d in range(0,2):                

                # 
                editimg[a][b][d]=(np.sum((1/9)*(np.array(                    

                [[((img[a-1][b-1][d])),((img[a-1][b][d])),((img[a-1][b+1][d]))],

                [((img[a][b-1][d])),((img[a][b][d])),((img[a][b+1][d]))],

                [((img[a+1][b-1][d])),((img[a+1][b][d])),((img[a+1][b+1][d]))]]))))


                #
    return editimg

# defines the function to rotate the image taking the number of rowsm the number of columns, the data of the image, and the copy of the image to edit as arguments 
def rotate(R,C,img,editimg):    

    #lets the user imput how many degrees they would like to rotate the image 
    rot=input('Enter how many degrees you want to rotate. Enter 90, 180, 270 or mirror: ')

    
    #validates the degrees to rotate - if it is not one of the 4 choices it wil prompt the user to enter a value again 
    while rot.lower()!='mirror' and rot!='90' and rot!='180' and rot!='270':

        #tells the user they have an invalid input
        print('Invalid Input')

        #and promptas them to enter a new value 
        rot=input('Enter how many degrees you want to rotate. Enter 90, 180, 270 or mirror: ')



    # if the user enters 90 degreees then it will run the code to rotate it 
    if rot=='90':


        #
        editimg=np.zeros((C,R,3), dtype=int)


        #itterates through the range of the number of rows 
        for j in range(R):

            #
            for i in range(C-1,-1,-1):  

                    #
                    editimg[i][j]=img[j][-i] 


    #if the user enters 180 degrees to rotate then it runs the code to rotate it 180 degrees
    if rot=='180':


        #
        editimg=np.zeros((R,C,3), dtype=int)

        
        #runs a loop in the range of the number of the rows 
        for i in range(R):

            
            #runs a loop for the range of the number of columns 
            for j in range(C):

                
                #
                editimg[i, C-1-j] = img[R-1-i, j]

# if the user enters 270 degres then it runs the code to rotate it 270 degrees 
    if rot=='270':


         #
        editimg1=np.zeros((R,C,3), dtype=int)

    # runs the loop for the number of rows 
        for i in range(R):


            #runs the loops for the number of columns
            for j in range(C):



                #
                editimg1[i, C-1-j] = img[R-1-i, j]


        editimg=np.zeros((C,R,3), dtype=int)


        for j in range(R):
            
            #
            for i in range(C-1,-1,-1):  

                    #
                    editimg[i][j]=editimg1[j][-i] 

    #if the user inputs mirror then it will run code to mirror the immage 
    if rot=='mirror':

        #
        editimg=np.zeros((R,C,3), dtype=int)

    #runs the loop for the number of rows 
        for i in range(R):

            #runs the loop for the number of columns
            for j in range(C):

                #
                editimg[i][j]=img[i][-j]

    #returns the edited image 
    return editimg


#define a function "gray()" that manipulates each R,B, and G value and adds them together into one value

def gray(R,C,img,editimg):


    #runs the loop fir the number of rows 
    for i in range(0,R):


        #runs the loop for the number of columns 
        for j in range(0,C):            

                #This creates a two dimensional gray scale matrix
            editimg[i][j]=img[i][j][0]*(299/1000)+img[i][j][1]*(587/1000)+img[i][j][2]*(114/1000)


    #returns the edited image 
    return editimg


# if the user enters R (or r) for roatate then 
if do == 'R' or do == 'r':


    #it will call the function to rotate the image with the number of rows, number of colums, the data of the image, and the copy of the image as arguments 
    editimg=rotate(R,C,img,editimg)


#if the user enters G (or g on accident) then
if do == 'G' or do == 'g':

    #it will call the function to grayscale the image with the number of rows, number of colums, the data of the image, and the copy of the image as arguments 
    editimg=gray(R,C,img,editimg)

#if the user enters S for smoothing it will call the finction to smooth with the number of rows, number of colums, the data of the image, and the copy of the image as arguments 
if do == 'S'or do == 's':

    editimg=smooth(R,C,img,editimg)

#puts edited image data in correct type for viewing            
editimg=editimg.astype(np.uint8)   
               
cv2.imshow('image',editimg)

#
cv2.waitKey(0)

#
cv2.destroyAllWindows() 

#
cv2.imwrite('editedimage.jpg',editimg)
