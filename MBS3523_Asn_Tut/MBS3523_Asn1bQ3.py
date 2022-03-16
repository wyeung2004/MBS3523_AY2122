# This is the marking scheme of: MBS3523_Asn1bQ3-ans.py

import cv2
#import numpy as np
print(cv2.__version__)

# you may need to change the number inside () to 0 1 or 2,
# depending on which webcam you are using
capture = cv2.VideoCapture(0)
# Below 2 lines are used to set the webcam window size
capture.set(3,640) # 3 is the width of the frame
capture.set(4,480) # 4 is the height of the frame

Text = "MBS3523 Assignment 1b - Q3    Name: Winston Yeung"
x = 0
dx = 2
y = 200
dy = 3
# Start capturing and show frames on window named 'Frame'
while True:
    success, img = capture.read()
    cv2.putText(img,Text, (80,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0),2)
    cv2.rectangle(img, (x, y), (x + 80, y+80), (0, 0, 255), 2)
    x = x + dx
    if x >= 560 or x <= 0:
        dx = dx * (-1)
    y = y + dy
    if y >= 400 or y <= 0:
        dy = dy * (-1)

    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

capture.release()
cv2.destroyAllWindows()