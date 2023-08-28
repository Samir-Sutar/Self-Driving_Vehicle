import cv2
import numpy as np

def getHistogram(img,minpercent=0.1,region=1 ):

   # if region ==1:
     # histogramValue = np.sum(img,axis=0)
    #else:
    histogramValue = np.sum(img[img.shape[0]//region:,:], axis=0)

    maximumValue = np.max(histogramValue)
    minimumValue= minpercent * maximumValue


    indexarray = np.where(histogramValue >= minimumValue)
    Basepoint = int(np.average(indexarray))



    imgHist=np.zeros((img.shape[0],img.shape[1],3) ,np.uint8)

    for x ,intensity in enumerate(histogramValue):
        print(intensity)
        if intensity > minimumValue: color=(255,0,255)
        cv2.line(imgHist,(x,img.shape[0]),(x,img.shape[0]-intensity//255//region),(255,0,255),1)
        cv2.circle(imgHist,(Basepoint,img.shape[0]),20,(0,255,255),cv2.FILLED)
        return Basepoint,imgHist
