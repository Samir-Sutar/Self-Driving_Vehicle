import cv2
import numpy as np

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

