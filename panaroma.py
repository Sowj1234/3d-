import cv2 as cv
import numpy as np

dim=(1028,768)
img3=cv.imread('img1.jpeg',cv.IMREAD_COLOR)
img3=cv.resize(img3,dim,interpolation=cv.INTER_AREA)

img4=cv.imread('img2.jpeg',cv.IMREAD_COLOR)
img4=cv.resize(img4,dim,interpolation=cv.INTER_AREA)

images=[]
images.append(img3)
images.append(img4)

sticher=cv.Stitcher.create()
ret,pano=sticher.stitch(images)

if ret==cv.STITCHER_OK:
    cv.imshow('panaroma',pano)
    cv.waitkey(0)