import cv2
import numpy as np

cam = cv2.VideoCapture(0)
Text = "MBS3523 Assignment 1d - Q5    Name: Winston Yeung"

def nil(x):
    pass

cv2.namedWindow('MBS3523')

cv2.createTrackbar('X_POS','MBS3523',320,640,nil)
cv2.createTrackbar('Y_POS','MBS3523',240,480,nil)

while True:
    success, img = cam.read()
    x = cv2.getTrackbarPos('X_POS', 'MBS3523')
    y = cv2.getTrackbarPos('Y_POS', 'MBS3523')
    cv2.line(img, (x, 0), (x, 480), (255, 0, 0), 2)
    cv2.line(img, (0, y), (640, y), (255, 0, 0), 2)
    cv2.putText(img, Text, (80, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()