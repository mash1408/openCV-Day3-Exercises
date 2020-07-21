import cv2
import numpy as np

img  = cv2.imread('KingCobra.jpg')
img=cv2.resize(img,(400,300))
''' Edge Detection With Blurring '''
gaussian = cv2.GaussianBlur(img.copy(), (5,5), 0)
cv2.imshow('edge', gaussian)
cv2.waitKey(0)
edge = cv2.Canny(img, 230, 250)
cv2.imshow('edge', edge)
ret, thresh = cv2.threshold(edge, 170, 255, cv2.THRESH_BINARY)  # Thresholding
cv2.imshow('',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()