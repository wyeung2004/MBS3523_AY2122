import cv2
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

Text = "MBS3523 Assignment 1c - Q4 Challenge   Name: WY"

while True:
    success , img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR) # Gray image with 3 dimensional array

    (thresh, imgBnW) = cv2.threshold(imgGray, 120, 255, cv2.THRESH_BINARY) # imgBnW - Black and White Image
    imgBnW_final = cv2.cvtColor(imgBnW, cv2.COLOR_GRAY2BGR)

    cv2.putText(imgBnW_final, Text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
        roiImg = img[y:y + h, x:x + w].copy()
        imgBnW_final[y:y + h, x:x + w] = roiImg
    cv2.imshow('MBS3523 - imgBnW_final', imgBnW_final)
    cv2.imshow('MBS3523 - BnW', imgBnW)
    if cv2.waitKey(5) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()