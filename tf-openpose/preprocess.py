import cv2 as cv
import numpy as np

# Just run this file to test the effects on the camera -- no OpenPose

class Preprocessing:

    def Contrast(self, value, image): # Used for both high and low contrast
        #Convert to HSV to get the Value channel
        hsv = cv.cvtColor(image, cv.COLOR_RGB2HSV)

        #Multiply the value channel by the value
        hsv[...,2] = cv.multiply(hsv[...,2], value)

        #Convert the image back into RGB
        new_image = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
        return new_image

    def Edge_detection(self, image):
        #Converts image to grayscale for better edge detection (May not have any effect, results vary, needs to be tested properly)
        cv.cvtColor(image,cv.COLOR_BGR2GRAY)

        #Apply Canny edge detection filter, second & third argument represents min & Max intensity values.
        edges = cv.Canny(image, 75, 150, True)

        #For every value from 0 to image width(x) and image height(y), check if the pixel in edges is white, if yes, set the corresponding pixel in image to white
        mask = cv.inRange(edges, 1, 255)

        #Convert the mask to be an RGB image
        mask = cv.cvtColor(mask, cv.COLOR_GRAY2RGB)

        #mask = cv.bitwise_not(mask, mask) #Remove comment to make the outline black -- also change the 'black' to white in the np.where statement!
        white = [255, 255, 255]
        black = [0, 0, 0]
        # Where the mask is not black, make the pixel white else keep the image's original color
        image = np.where(mask != black, mask, image)
        #cv.imshow('edges', edges)
        return image

    def Sharpness(self, original_image_weight, blurred_image_weight, image):
        #Blur the image 
        blurred_image = cv.GaussianBlur(image, (9,9), 0)
        
        #Subtract the blurred image from the original image to sharpen it
        sharpened = cv.addWeighted(image, original_image_weight, blurred_image, -blurred_image_weight, 0, blurred_image)  #Subtract the blurred image from the original image to sharpen it

        return sharpened

    def Histogram_EQ(self, image): # Histogram Equalization
        img_yuv = cv.cvtColor(image, cv.COLOR_RGB2YUV)
        img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
        eqa_img = cv.cvtColor(img_yuv, cv.COLOR_YUV2RGB)
        return eqa_img


# --- Don't put anything related to the class below this --- #
# Testing the processing
cam = cv.VideoCapture(0)
pre = Preprocessing()

'''
ret2, background_image = cam.read();
while (True):
    ret, image = cam.read();

    #background_image = cv.imread('images/image_name'); #Insert the image name instead of image_name
    

    # Change the pre.XXXXXX to your desired pre-processing to test it (e.g pre.Contrast(xxxxx) --> pre.Edge_detection(xxxxx))
    #output = pre.Sharpness(2.2, 1, image)
    output = pre.BG_Subtraction(background_image, image)
    # Show the original and the processed image 
    cv.imshow('Original', image)
    cv.imshow('Processed', output)

    # Hit 'Q' to stop -- doesn't close the windows tho
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
'''
