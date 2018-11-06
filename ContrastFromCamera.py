import numpy as np
import cv2

from matplotlib import pyplot as plt

#Read from camera
cap = cv2.VideoCapture(0)

while 1:
    # Take each frame
    _, frame = cap.read()

    imghsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imghsv[:, :, 2] = [[max(pixel - 75, 0) if pixel < 190 else min(pixel + 75, 255) for pixel in row] for row in imghsv[:, :, 2]]

    cv2.imshow('contrast', cv2.cvtColor(imghsv, cv2.COLOR_HSV2BGR))

#    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()