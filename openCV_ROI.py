import cv2
import numpy as np
cam = cv2.VideoCapture(0)
frame = np.zeros([500,500,3],dtype=np.uint8)

while True:
    unuse , img = cam.read()
    # print(img.shape)
    # img[100:200, 100:200] = 180
    # imgCrop = img[100:300, 300:500]
    # img[:, :, 1] = 0
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(imgGray.shape)
    # imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
    # print(imgGray[100,100])
    # imgGray[100:300, 300:500] = imgCrop
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img2 = cv2.cvtColor(img1, cv2.COLOR_HSV2BGR)
    print(type(img2))
    cv2.imshow('img', img)
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('Frrame', frame)
    # cv2.imshow('imgCrop', imgCrop)
    # cv2.imshow('imgGray', imgGray)
    if cv2.waitKey(5) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()

