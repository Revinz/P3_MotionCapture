#THEORY: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html
import cv2
import numpy as np
#Create and show original image
img = cv2.imread('Human.png')

#Apply Canny edge detection filter, second & third argument represents min & Max intensity values.
edges = cv2.Canny(img, 0, 255, True)

NPedges = np.array(edges)
NPimg = np.array(img)
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        if NPedges[x, y] > 1:
            #NPimg[x,y,2] = NPedges[x,y]
            NPimg[x,y] = [0,0,0]
            print(NPimg[x,y])
cv2.imshow('edges',edges)
cv2.imshow('Img', NPimg)
cv2.waitKey(0)