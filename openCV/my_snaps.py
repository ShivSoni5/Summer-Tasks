#!/usr/bin/python3

import cv2 as cv

cap = cv.VideoCapture(0)

i=0

while(cap.isOpened()):
    i+=1
    ret, frame = cap.read()

    cv.imwrite(f'/home/raj/Pictures/mysnaps/snap{i}.png',frame)

    cv.imshow('my_video',frame)
    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
