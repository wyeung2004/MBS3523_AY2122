import cv2
print(cv2.__version__)

cam = cv2.VideoCapture(0) # try 1, 2 or 3 if you have error

while True:
    success , frame = cam.read()
    # print(success)
    cv2.imshow('MBS3523', frame)
    if cv2.waitKey(5) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
