import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0)


while True:
    success , frame = cam.read()

    cv2.rectangle(frame, (200, 200), (350, 350), (0, 125, 125), 3)
    # cv2.putText(frame, "W Yeung", (200, 220), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255),2)

    cv2.imshow('MBS3523', frame)
    if cv2.waitKey(5) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()