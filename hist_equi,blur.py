import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('img.jpeg');
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY);
hist=cv.calcHist([img],[0],None,[256],[0,255])
cv.imshow('img',img)
plt.plot(hist)


img2=cv.equalizeHist(img)
eq_hist=cv.calcHist([img2],[0],None,[256],[0,255])
cv.imshow('equi img',img2)
plt.plot(eq_hist)
plt.show()

blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('blurred img',blur)

canny=cv.Canny(img,125,175)
cv.imshow("edge detected img",canny)
cv.waitKey(0)

