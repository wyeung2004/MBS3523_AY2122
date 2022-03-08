import cv2
# import numpy as np

cam = cv2.VideoCapture(0)

while True:
    success, img = cam.read()
    # img[100:200,100:200,1] = 80
    img[100,100] = (0,0,255)
    # print(img)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print(type(imgGray))
    # print(np.shape(imgGray))
    imgCrop = img[100:300,300:500]
    imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)
    imgGray[100:300,300:500] = imgCrop

    cv2.imshow('img', img)
    cv2.imshow('imgGray', imgGray)
    cv2.imshow('imgCrop', imgCrop)
    if cv2.waitKey(1) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()