#!/usr/bin/python3

import cv2 as cv

cap = cv.VideoCapture(0)
while cap.isOpened():
    status,frame = cap.read()
    only_red = cv.inRange(frame,(0,0,40),(20,20,255))
    cv.imshow('camera_real',frame)
    cv.imshow('camera_fake',only_red)
    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()
