import cv2
import numpy as np

def initializeTrackbars(intialTracbarVals,wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 720, 360)
    cv2.createTrackbar("Width Top", "Trackbars", intialTracbarVals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", intialTracbarVals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", intialTracbarVals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", intialTracbarVals[3], hT, nothing)

def valTrackbars(wT=480,hT=240):
     widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
     heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
     widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
     heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
     points = np.float32([(widthTop, heightTop),(wT-widthTop, heightTop),(widthBottom , heightBottom ),(wT-widthBottom, heightBottom)])
     return points