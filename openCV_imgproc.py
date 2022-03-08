import cv2
import numpy as np
print(cv2.__version__)

kernel = np.ones((5,5), np.uint8)

img = cv2.imread('Resources/lena.png')
img1 = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img3 = cv2.GaussianBlur(img2, (5,5), 0)
img4 = cv2.Canny(img, 100, 100)
img5 = cv2.dilate(img4, kernel, iterations=1)

cv2.imshow('LENA', img)
cv2.imshow('small LENA', img1)
cv2.imshow('Gray LENA', img2)
cv2.imshow('Blur LENA', img3)
cv2.imshow('Canny LENA', img4)
cv2.imshow('Dilate LENA', img5)

cv2.waitKey(0)