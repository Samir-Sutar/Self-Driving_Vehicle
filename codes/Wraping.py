import cv2
import numpy as np

def warpImg(img,points,W,H,inverse= False):

    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [W, 0], [0, H], [W, H]])
    if inverse:
      matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
      matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarp = cv2.warpPerspective(img,matrix,(W,H))
    return imgWarp