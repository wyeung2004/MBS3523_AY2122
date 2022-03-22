import cv2
import numpy as np

def HueLow(x):
    global HueLow
    HueLow = x
    print('Hue Low = ', HueLow)
def HueHigh(x):
    global HueHigh
    HueHigh = x
    print('Hue High = ', HueHigh)
def SatLow(x):
    global SatLow
    SatLow = x
    print('Sat Low = ', SatLow)
def SatHigh(x):
    global SatHigh
    SatHigh = x
    print('Sat High = ', SatHigh)
def ValLow(x):
    global ValLow
    ValLow = x
    print('Val Low = ', ValLow)
def ValHigh(x):
    global ValHigh
    ValHigh = x
    print('Val High = ', ValHigh)

cv2.namedWindow('Trackbars')

cv2.createTrackbar('HueLow','Trackbars',10,179,HueLow)
cv2.createTrackbar('HueHigh','Trackbars',150,179,HueHigh)
cv2.createTrackbar('SatLow','Trackbars',10,255,SatLow)
cv2.createTrackbar('SatHigh','Trackbars',255,255,SatHigh)
cv2.createTrackbar('ValLow','Trackbars',10,255,ValLow)
cv2.createTrackbar('ValHigh','Trackbars',250,255,ValHigh)


# Set up webcam
# cam = cv2.VideoCapture(0)
# cam.set(3,640)
# cam.set(4,480)

# Start capturing and show frames on window
while True:
    # success, img = cam.read()
    img = cv2.imread('Resources/smarties.png')
    cv2.imshow('Frame', img)
    # cv2.moveWindow('Frame', 100,20)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hueLow = cv2.getTrackbarPos('HueLow','Trackbars')
    hueHigh = cv2.getTrackbarPos('HueHigh', 'Trackbars')
    satLow = cv2.getTrackbarPos('SatLow', 'Trackbars')
    satHigh = cv2.getTrackbarPos('SatHigh', 'Trackbars')
    valLow = cv2.getTrackbarPos('ValLow', 'Trackbars')
    valHigh = cv2.getTrackbarPos('ValHigh', 'Trackbars')

    FGmask = cv2.inRange(hsv, (hueLow,satLow,valLow),(hueHigh,satHigh,valHigh))
    cv2.imshow('FGmask',FGmask)

    FG = cv2.bitwise_and(img,img,mask=FGmask)
    cv2.imshow('FG', FG)

    BGmask = cv2.bitwise_not(FGmask)
    cv2.imshow('BGmask', BGmask)

    BG = cv2.cvtColor(BGmask,cv2.COLOR_GRAY2BGR)

    finalImg = cv2.add(FG,BG)
    cv2.imshow('FinalImage', finalImg)

    if cv2.waitKey(5) & 0xff == 27:
        break

# cam.release()
cv2.destroyAllWindows()