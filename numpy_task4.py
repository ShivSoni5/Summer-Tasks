#!/usr/bin/python3

import numpy as np

list_for_array = [10,11,33,22,11,22,33,44,5,6,5,33,6,33,44,55,6,10,2,3]

"""
i=0

while i != "q":
	a=input("enter number for array: ")
	list_for_array.append(a)
	
"""

length_list = len(list_for_array)
array_shapes = []

for i in range(2, length_list//2 + 1):
	if (length_list % i) == 0:
		array_shapes.append((i,length_list//i))

print("Shapes available are: ")

if len(array_shapes)==0:
	print(0)
else:
	for i,shape in enumerate(array_shapes) :
		print(i,shape)

shape_index = int(input("Enter index of shape you wanted: "))
print(np.array(list_for_array).reshape(array_shapes[shape_index][0],array_shapes[shape_index][1]))
