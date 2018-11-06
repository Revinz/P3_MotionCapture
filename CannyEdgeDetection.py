#THEORY: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

import cv2

#Create and show original image
img = cv2.imread('Human.png')
cv2.imshow('Img',img)

#Convert image to grayscale to make edgedetection easier
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscaled',imgGray)

#Apply Canny edge detection filter, second & third argument represents min & Max intensity values.
edges = cv2.Canny(imgGray,0,255,True)
cv2.imshow('Edges',edges)

cv2.waitKey(0)