import cv2 as cv
import numpy as np

# Just run this file to test the effects on the camera -- no OpenPose
fgbg = cv.createBackgroundSubtractorMOG2() #Creating a subtractor 
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

    def BG_Subtraction(self, image):
        #Just a test, remove when implementing proper method
        fgmask = fgbg.apply(image) #Applying subtraction to the video
        return fgmask

    def Sharpness(self, original_image_weight, blurred_image_weight, image):
        #Just a test, remove when implementing proper method
        blurred_image = cv.GaussianBlur(image, (11,11), 0) #Blur the image 
        sharpened = cv.addWeighted(image, original_image_weight, blurred_image, -blurred_image_weight, 0, blurred_image)  #Subtract the blurred image from the original image to sharpen it
        # -- More about this approach here: https://en.wikipedia.org/wiki/Unsharp_masking#Digital_unsharp_masking (Called Unsharp_masking)

        return sharpened

    def Histogram_EQ(self, image): # Histogram Equalization
        #Just a test, remove when implementing proper method
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) #Change the input to a grayscaled image
        equ = cv.equalizeHist(gray_image) #Equalize the histogram
        return equ



# --- Don't put anything related to the class below this --- #

# Testing the processing
cam = cv.VideoCapture(0)
pre = Preprocessing()
while (True):
    ret, image = cam.read();

    # Change the pre.XXXXXX to your desired pre-processing to test it (e.g pre.Contrast(xxxxx) --> pre.Edge_detection(xxxxx))
    output = pre.Sharpness(2.5, 1.3, image)
    # Show the original and the processed image 
    cv.imshow('Original', image)
    cv.imshow('Processed', output)

    # Hit 'Q' to stop -- doesn't close the windows tho
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.waitKey(0)
cv.destroyAllWindows()