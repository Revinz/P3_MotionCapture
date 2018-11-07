import cv2 as cv
import numpy as np

# Just run this file to test the effects on the camera -- no OpenPose

class Preprocessing:

    ### Change what you need to change. These are just setups to get you all started

    def Contrast(self, value, image): # Easily used for both high and low contrast
        #Just a test, remove when implementing proper method
        hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)
        hsv[...,2] = cv.multiply(hsv[...,2], value)
        new_image = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
        return new_image

    def Edge_detection(self, image):
        #Converts image to grayscale for better edge detection (May not have any effect, results vary, needs to be tested properly)
        cv.cvtColor(image,cv.COLOR_BGR2GRAY)

        #Apply Canny edge detection filter, second & third argument represents min & Max intensity values.
        edges = cv.Canny(image, 100, 150, True)       
        #For every value from 0 to image width(x) and image height(y), check if the pixel in edges is white, if yes, set the corresponding pixel in image to white

        mask = cv.inRange(edges, 10, 255)

        image = cv.bitwise_not(image, image, mask=mask)

        #cv.imshow('edges', edges)
        return image

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

    def Histogram_EQ(self, image): # Histogram Equalization
        img_yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)
        img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
        #cv.imshow('test', img_yuv)
        eqa_img = cv.cvtColor(img_yuv, cv.COLOR_YUV2RGB)
        return eqa_img


# --- Don't put anything related to the class below this --- #
# Testing the processing
cam = cv.VideoCapture(0)
pre = Preprocessing()
'''
while (True):
    ret, image = cam.read();

    # Change the pre.XXXXXX to your desired pre-processing to test it (e.g pre.Contrast(xxxxx) --> pre.Edge_detection(xxxxx))
    #output = pre.Sharpness(2.2, 1, image)
    output = pre.Contrast(1.5, image)
    # Show the original and the processed image 
    cv.imshow('Original', image)
    cv.imshow('Processed', output)

    # Hit 'Q' to stop -- doesn't close the windows tho
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
'''