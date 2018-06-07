#!/usr/bin/python3

import cv2
import numpy as np

#load image
load_image = numpy.loadtxt('file_name.txt').astype('uint8')

#reshape image to its original diimension
show_image = load_image.reshape(480,640,3)

#show image
cv2.imshow('window_name',show_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
