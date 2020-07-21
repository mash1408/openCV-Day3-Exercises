import cv2
img = cv2.imread('hand.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # Converting Image to Grayscale
gray=cv2.resize(gray,(300,300))
blurred = cv2.GaussianBlur(gray, (11, 11), 0)  #  Blurring the Image
edged = cv2.Canny(blurred, 20, 150)           #   Detecting Edges
cv2.imshow('',edged)
cv2.waitKey(0)

'''contours of my hand'''
cnts, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))
hand_=img.copy()
hand_=cv2.resize(hand_,(300,300))
cv2.drawContours(hand_, cnts, -1, (255, 255, 128), 2)
cv2.imshow('',hand_)
cv2.waitKey(0)


cv2.destroyAllWindows()

cv2.destroyAllWindows()