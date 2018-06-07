#!/usr/bin/python3

import cv2
import numpy as np

#load image
img = cv2.imread('path_to_image')

#check size and shape of img
#img.shape;img.size

#convert image to 2D using reshape
save_it = img.reshape(3,-1)

#check size and shape of save_it
#save_it.shape;save_it.size

np.savetxt('file_name.txt',save_it)


#HOW TO USE THIS TEXT FILE TO RECREATE THE IMAGE
#Check load_img_from_txt.py 

