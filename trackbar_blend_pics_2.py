import cv2

alpha_slider_max = 100

def on_trackbar(val):
    pass

src1 = cv2.imread('Resources/evil.jpg')
src2 = cv2.imread('Resources/anime.jpg')

cv2.namedWindow('Linear Blend')
cv2.createTrackbar('Alpha', 'Linear Blend', 0, alpha_slider_max, on_trackbar)

while True:
    src1 = cv2.imread('Resources/evil.jpg')
    src2 = cv2.imread('Resources/anime.jpg')
    val = cv2.getTrackbarPos('Alpha', 'Linear Blend')
    alpha = val / alpha_slider_max
    beta = (1.0 - alpha)
    dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
    cv2.imshow('Linear Blend', dst)
    if cv2.waitKey(5) & 0xff == 27:
        break

cv2.destroyAllWindows()
