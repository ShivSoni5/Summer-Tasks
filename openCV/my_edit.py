#!/usr/bin/python3

import cv2 as cv

img1 = cv.imread('/home/raj/Pictures/mysnaps/snap10.png')
img2 = cv.imread('/home/raj/Pictures/mysnaps/snap21.png')
img3 = cv.imread('/home/raj/Pictures/mysnaps/snap48.png')
img4 = cv.imread('/home/raj/Pictures/mysnaps/snap88.png')
img5 = cv.imread('/home/raj/Pictures/mysnaps/snap93.png')
#cv.add(img1,img2,img3,img4,img5)
cv.add(img2,img3)
cv.add(img4,img5)
new_right = cv.addWeighted(img2,1.0,img3,0.8,1)
new_left = cv.addWeighted(img4,1.0,img5,0.8,1)
new = cv.add(new_right,new_left)
cv.add(img1,new)
show = cv.addWeighted(img1,1.0,new,0.8,1)
cv.imshow('show',show)
cv.waitKey(0)
cv.destroyAllWindows()

