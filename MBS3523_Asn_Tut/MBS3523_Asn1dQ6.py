import cv2
import numpy as np

EVT = 0
# mouse callback function
def draw_rectangle(event,x,y,flags,param):
    global PNT1
    global PNT2
    global EVT
    if event == cv2.EVENT_LBUTTONDOWN:
        PNT1 = (x,y)
        EVT = event
        # print(event)
    if event == cv2.EVENT_LBUTTONUP:
        PNT2 = (x,y)
        EVT = event
    if event == cv2.EVENT_RBUTTONUP: # RBUTTONUP --> event = 5
        EVT = event

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rectangle)

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    if EVT == 4:
        cv2.rectangle(img, PNT1,PNT2, (255, 0, 0), 3)
        imgROI = img[PNT1[1]:PNT2[1], PNT1[0]:PNT2[0]]
        cv2.imshow('image ROI', imgROI)
    if EVT == 5:
        img[:,:]=img
        cv2.destroyWindow('image ROI')
        EVT = 0
    # img = cv2.flip(img,1)
    cv2.imshow('image',img)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()