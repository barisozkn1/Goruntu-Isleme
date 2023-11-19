import cv2
import numpy as np
record = cv2.VideoCapture(0)

a = 1
while a == 1:
    bc, cevir = record.read()
    hsv = cv2.cvtColor(cevir, cv2.COLOR_BGR2HSV)
    renk_min_sinir = np.array([0, 0, 0])
    renk_max_sinir = np.array([5, 255, 255])

    mask = cv2.inRange(hsv, renk_min_sinir,renk_max_sinir)
    red_return = cv2.bitwise_and(cevir, cevir, mask=mask)

    cv2.imshow("Lutfen kapatmak icin 'x' tusuna basiniz.", cevir)
    cv2.imshow("Kapatabilmek icin 'x' tusuna basiniz.", red_return)


    if cv2.waitKey(1) & 0xFF == ord('x'):
        a = 0
        break

record.release()
cv2.destroyAllWindows()
