import cv2 as cv
import numpy as np

# Just run this file to test the effects on the camera -- no OpenPose

class Preprocessing:

    ### Change what you need to change. These are just setups to get you all started

    def Contrast(self, value, image): # Easily used for both high and low contrast
        #Just a test, remove when implementing proper method
        new_image = image * 1.5
        return new_image

    def Edge_detection(self, value, image):
        #Just a test, remove when implementing proper method
        new_image = image * 1.5
        return new_image

    def BG_Subtraction(self, value, image):
        #Just a test, remove when implementing proper method
        new_image = image * 1.5
        return new_image

    def Sharpness(self, value, image):
        #Just a test, remove when implementing proper method
        new_image = image * 1.5
        return new_image

    def Histogram_EQ(self, value, image): # Histogram Equalization
        #Just a test, remove when implementing proper method
        new_image = image
        return new_image



# --- Don't put anything related to the class below this --- #

# Testing the processing
cam = cv.VideoCapture(0)
pre = Preprocessing()
while (True):
    ret, image = cam.read();

    # Change the pre.XXXXXX to your desired pre-processing to test it (e.g pre.Contrast(xxxxx) --> pre.Edge_detection(xxxxx))
    output = pre.Contrast(1.5, image) 
    # Show the original and the processed image 
    cv.imshow('Original', image)
    cv.imshow('Processed', output)

    # Hit 'Q' to stop -- doesn't close the windows tho
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.waitKey(0)
cv.destroyAllWindows()