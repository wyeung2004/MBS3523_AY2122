import cv2
import numpy as np

EVT = 0
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global PNT
    global EVT
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # cv2.circle(img,(x,y),100,(255,0,0),-1)
        PNT = (x,y)
        EVT = event
        # print(event)
        # print(x,y)
    # if event == cv2.EVENT_RBUTTONUP: # RBUTTONUP --> event = 5
    #     EVT = event

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

cam = cv2.VideoCapture(0)

while True:
    _, img = cam.read()
    if EVT == 7:
        cv2.circle(img, PNT, 100, (255, 0, 0), -1)
        # ROI = np.zeros([500, 500, 3], dtype=np.uint8)
        # print(PNT)
        # ROI[:, :] = img[PNT[1], PNT[0]]
        # cv2.imshow('ROI', ROI)
        # EVT = 0
    # if EVT == 5:
    #     img[:,:]=img
    cv2.imshow('image',img)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.destroyAllWindows()