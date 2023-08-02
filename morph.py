import cv2 as cv
import numpy as np

while(True):
    img=cv.imread('img.jpeg');
    kernal=np.ones((5,5),np.uint8)
    img1=cv.erode(img,kernal,iterations=1)
    img2=cv.dilate(img,kernal,iterations=1)
    cv.imshow('img',img)
    cv.imshow('img erode',img1)
    cv.imshow('img dilate',img2)
    cv.waitKey(0)
    
    
    

