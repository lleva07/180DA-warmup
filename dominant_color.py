"""
file: dominant_color.py
author: Archie Noel C. Lleva
description: initiates object tracking of blue objects using the HSV color model
References: 
video capture
https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html

dominant color bar
https://github.com/aysebilgegunduz/DominantColor/blob/master/dominant_color.py



note: used youtube tutorial to apply contour box around the masked colored object
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar

cap = cv.VideoCapture(0)
while(1):
    _, frame = cap.read()
    height, width, _ = frame.shape
    x = int(width * 0.40)
    y = int(height * 0.40)
    roi_height= int(height * 0.2)
    roi_width = int(roi_height)
    roi = frame[y:y+roi_height, x:x+roi_width]

    frm = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

    frm = frm.reshape((frm.shape[0] * frm.shape[1],3)) #represent as row*column,channel number
    clt = KMeans(n_clusters=2) #cluster number
    clt.fit(frm)

    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)

    
    # Overlay bar on vid frame
    frame[0:50, 0:300] = bar

    cv.rectangle(frame,(x,y),(x+roi_width,y+roi_height),(0,255,0),2)
    cv.imshow('frame', frame)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()