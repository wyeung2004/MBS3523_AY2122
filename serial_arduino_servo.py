import cv2
import numpy as np
import serial
import time

ser = serial.Serial('COM7',baudrate=115200,timeout=1)
time.sleep(2)
servoPos1 = 90

def nothing(x): pass

cv2.namedWindow('Trackbars')

cv2.createTrackbar('ServoPos1','Trackbars',90,180,nothing)
# cv2.createTrackbar('ServoPos2','Trackbars',0,180,nothing)

while True:
    servoPos1 = cv2.getTrackbarPos('ServoPos1','Trackbars')
    # You need to send a String to Arduino with a CR as ending
    servoPos1 = str(servoPos1)+'\r'
    # servoPos2 = cv2.getTrackbarPos('ServoPos2', 'Trackbars')
    ser.write(servoPos1.encode())
    print(servoPos1)
    print(type(servoPos1))
    # print(servoPos2)
    time.sleep(0.1)

    if cv2.waitKey(1) & 0xff == 27:
        break

ser.close()