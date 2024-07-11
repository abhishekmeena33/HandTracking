import cv2 as cv
import numpy as np
import time
import HandTrackingModule as htm

###########################
wCam, hCam = 980, 720
###########################
cap = cv.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.HandDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw = False)
    if len(lmList) != 0:
        print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cv.circle(img, (x1, y1),15, (255, 0, 255), cv.FILLED)
        cv.circle(img, (x2, y2), 15, (255, 0, 255), cv.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv.putText(img, f'FPS: {int(fps)}', (40,70), cv.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 3)

    cv.imshow("Image", img)
    cv.waitKey(1)