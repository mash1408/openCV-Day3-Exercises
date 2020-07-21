import cv2
import numpy as np
import matplotlib.pyplot as plt



#Loading the image and converting it into grayscale
king = cv2.imread('dolphin.png')
king=cv2.resize(king,(300,300))

gray=cv2.cvtColor(king,cv2.COLOR_BGR2GRAY)
#computr median of pixel intensities
v = np.median(gray)
lower = int(max(0, (1.0 - 0.43) * v))
upper = int(min(255, (1.0 + 0.43) * v))

gaussian = cv2.GaussianBlur(gray.copy(), (7,7), 0)
edge = cv2.Canny(gaussian, lower,upper)
#cv2.imshow('Edged Dinosaur',edge)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.imshow('',edge)
cv2.waitKey(0)

cv2.destroyAllWindows()