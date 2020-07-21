import cv2
import numpy as np

filter  = cv2.imread('signal.jpg')
filter = cv2.resize(filter, (300,300))
# It converts the BGR color space of image to HSV color space
hsv = cv2.cvtColor(filter,cv2.COLOR_BGR2HSV) 
cv2.imshow('',hsv)
cv2.waitKey(0)   
# Threshold of red in HSV space 
lower_blue = np.array([169, 10, 40])         
upper_blue = np.array([189, 255, 255])      
 # preparing the mask to overlay 
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# The black region in the mask has the value of 0, 
# so when multiplied with original image removes all non-blue regions 
result = cv2.bitwise_and(filter, filter, mask = mask)
cv2.imshow('',result)
cv2.waitKey(0) 
cv2.imshow('',mask)
cv2.waitKey(0) 
cv2.destroyAllWindows()