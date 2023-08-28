import cv2
import numpy as np

def threshoulding(img):

  imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
  lowerWhite =np.array([102,0,118])
  upperWhite =np.array([112,255,255])
  maskWhite = cv2.inRange(imgHSV,lowerWhite,upperWhite)
  return maskWhite

def warpImg(img,points,W,H):
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [W, 0], [0, H], [W, H]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(W,H))
    return imgWarp

def nothing(a):
    pass

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

 def drawPoints(copy,points):
     while(1):
       for x in range(0,1):
          print(x)
          print(y)

             cv2.circle(copy, (int(points[y][0]), int(points[y][1])), 7, (0, 255, 0), cv2.FILLED)
        for z in range(2,3):
            print(z)
        cv2.circle(copy, (int(points[z][0]), int(points[z][1])), 7, (0, 0,255), cv2.FILLED)
         for a in range(3,4):
         print(a)
           cv2.circle(copy, (int(points[a][0]), int(points[a][1])), 7, (0, 0, 255), cv2.FILLED)
           return copy






