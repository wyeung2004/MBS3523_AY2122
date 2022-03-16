import cv2
print(cv2.__version__)

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)

Text = "MBS3523 Assignment 1c - Q4    Name: Winston Yeung"

while True:
    success , img = cam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgGray = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR) # Gray image with 3 dimensional array

    cv2.putText(imgGray, Text, (80, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
        roiImg = img[y:y + h, x:x + w].copy()
        imgGray[y:y + h, x:x + w] = roiImg

    cv2.imshow('MBS3523 - Gray', imgGray)
    if cv2.waitKey(5) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()