import cv2
import numpy as np

width = 640
height = 480
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
print(width,height)
def nil(x): pass

cv2.namedWindow('MBS3523')

cv2.createTrackbar('RED','MBS3523',125,255,nil)
cv2.createTrackbar('GREEN','MBS3523',125,255,nil)
cv2.createTrackbar('BLUE','MBS3523',125,255,nil)

cv2.createTrackbar('RADIUS','MBS3523',125,240,nil)
cv2.createTrackbar('CENTER_X','MBS3523',int(width/2),width,nil)
cv2.createTrackbar('CENTER_Y','MBS3523',int(height/2),height,nil)

while True:
    success, img = cam.read()
    red = cv2.getTrackbarPos('RED', 'MBS3523')
    green = cv2.getTrackbarPos('GREEN', 'MBS3523')
    blue = cv2.getTrackbarPos('BLUE', 'MBS3523')
    # img[:,:,2]=red
    # img[:, :, 1] = green
    img[:, :, 0] = blue

    x = cv2.getTrackbarPos('CENTER_X', 'MBS3523')
    y = cv2.getTrackbarPos('CENTER_Y', 'MBS3523')
    R = cv2.getTrackbarPos('RADIUS', 'MBS3523')
    cv2.circle(img,(x,y),R, (255,0,0), 3)

    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

# cam.release()
cv2.destroyAllWindows()