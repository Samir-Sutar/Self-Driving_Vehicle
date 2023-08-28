import cv2
import numpy as np

def threshoulding(img):

  imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  lowerWhite =np.array([102,0,118])
  upperWhite =np.array([112,255,255])
  maskWhite = cv2.inRange(imgHSV,lowerWhite,upperWhite)
  return maskWhite
