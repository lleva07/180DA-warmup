"""
file: video_capture.py
author: Archie Noel C. Lleva
description: initiates object tracking of blue objects using the HSV color model
"""

import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
 
    #find contours of mask
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    min_area_thresh = 1000
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > min_area_thresh:
            x,y,w,h = cv.boundingRect(cnt)
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()


#HSV vs RGB: HSV values are generally better, since they take into account the change in light conditions around an object

#lights on or off: able to retain tracking capabilities despite low light conditions

#does turning off light hurt color detection: to some extent yes: at low brightness, model was able to fully detect block, however at high brightness model was
#unable to detect color as evidenced by the masking