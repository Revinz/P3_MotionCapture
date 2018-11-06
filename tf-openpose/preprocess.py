import cv2 as cv
import numpy as np

# Just run this file to test the effects on the camera -- no OpenPose

class Preprocessing:

    ### Change what you need to change. These are just setups to get you all started

    def Contrast(self, value, image): # Easily used for both high and low contrast
        #Just a test, remove when implementing proper method
        new_image = image * 1.5
        return new_image

    def Edge_detection(self, image):

        #Convert image to grayscale to make edgedetection easier
        imgGray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
        #cv.imshow('Grayscaled',imgGray)

        #Apply Canny edge detection filter, second & third argument represents min & Max intensity values.
        edges = cv.Canny(imgGray,0,255,True)
        #cv.imshow('Edges',edges)

        output = cv.cvtColor(edges,cv.COLOR_GRAY2RGB)
        output = output + image
        return output

    def BG_Subtraction(self, value, image):
        #Just a test, remove when implementing proper method
        new_image = image * 1.5
        return new_image

    def Sharpness(self, original_image_weight, blurred_image_weight, image):
        #Just a test, remove when implementing proper method
        blurred_image = cv.GaussianBlur(image, (9,9), 0) #Blur the image 
        sharpened = cv.addWeighted(image, original_image_weight, blurred_image, -blurred_image_weight, 0, blurred_image)  #Subtract the blurred image from the original image to sharpen it
        # -- More about this approach here: https://en.wikipedia.org/wiki/Unsharp_masking#Digital_unsharp_masking (Called Unsharp_masking)

        return sharpened

    def Histogram_EQ(self, value, image): # Histogram Equalization
        #Just a test, remove when implementing proper method
        new_image = image
        return new_image



# --- Don't put anything related to the class below this --- #

# Testing the processing
cam = cv.VideoCapture(0)
pre = Preprocessing()

'''
while (True):
    ret, image = cam.read();

    # Change the pre.XXXXXX to your desired pre-processing to test it (e.g pre.Contrast(xxxxx) --> pre.Edge_detection(xxxxx))
    output = pre.Edge_detection(image)
    # Show the original and the processed image 
    cv.imshow('Original', image)
    cv.imshow('Processed', output)

    # Hit 'Q' to stop -- doesn't close the windows tho
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()  
'''