import numpy as np
import cv2
import utlis
import Threshoulding
import Wraping
import TrackBarInitilization
import drawpoint

def getLaneCurve(img):
    copy = img.copy()
    imgThres = Threshoulding.threshoulding(img)
    h,w,c= img.shape
    points = TrackBarInitilization.valTrackbars()
    imgwarp = Wraping.warpImg(imgThres, points,w,h)
    imgWarpPoints = drawpoint.drawPoints(copy,points)

    cv2.imshow('Thres',imgThres)
    cv2.imshow('Warp',imgwarp)
    cv2.imshow('Warp point', imgWarpPoints)

    return None


cap = cv2.VideoCapture('test3.mp4')
intialTracbarVals =[88,124,0,240]
initializeTrackbars(intialTracbarVals)


while(cap.isOpened()):

    ret, frame = cap.read()


    if ret:
        img =cv2.resize(frame,(480,240))
        cv2.imshow("ORIGINAL", img)
        getLaneCurve(img)



    else:
       print('no video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    if cv2.waitKey(15) & 0xFF == ord('q'):
       break

cap.release()
cv2.destroyAllWindows()