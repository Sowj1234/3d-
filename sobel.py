import cv2 as cv
import numpy as np
img=cv.imread('sobel1.jpeg');
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gradients_sobelx=cv.Sobel(img,-1,1,0)
gradients_sobely=cv.Sobel(img,-1,0,1)

gradients_sobelxy=cv.addWeighted(gradients_sobelx,0.5,gradients_sobely,0.5,0)
cv.imshow("sobel",gradients_sobelxy)

canny=cv.Canny(img,125,175)
cv.imshow("edge detected img",canny)
cv.waitKey(0)