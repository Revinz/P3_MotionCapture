#Import modules
import cv2

#Create and show image
img = cv2.imread('Meow.png')
cv2.imshow('Meow',img)

#Convert the picture into HSV colorformat
imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#If pixel values are above 190 intensity, decrease it with 25. if above, increase it with 25 up to a max of 255
#Adjust pixel values(190 and 250 respectively) to change the contrast.
#imghsv[:,:,2] = [[max(pixel - 190, 0) if pixel < 190 else min(pixel + 255,255) for pixel in row] for row in imghsv[:,:,2]]

#Below is low contrast example
imghsv[:, :, 2] = [[max(pixel +50, 0) if pixel < 190 else min(pixel - 50,255) for pixel in row] for row in imghsv[:,:,2]]


cv2.imshow('contrast', cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR))
cv2.waitKey(0)