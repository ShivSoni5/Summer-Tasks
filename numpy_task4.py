#!/usr/bin/python3

import numpy as np

list_for_array = []


while True:
	a=input("enter number for array: ")
	if a == "q":
		break
	list_for_array.append(int(a))
	

length_list = len(list_for_array)
array_shapes = []


def generate_shapes(list_for_array_shapes,length):
	for i in range(2, length//2 + 1):
		if (length % i) == 0:
			list_for_array_shapes.append((i,length//i))


generate_shapes(array_shapes,length_list)

if len(array_shapes)==0:
	print(0)
	new_num = int(input("Enter one more number to create a valid array: "))
	list_for_array.append(new_num)
	new_length = len(list_for_array)
	generate_shapes(array_shapes,new_length)

print("Shapes available are: ")
for i,shape in enumerate(array_shapes) :
	print(i,shape)

shape_index = int(input("Enter index of shape you wanted: "))
print(np.array(list_for_array).reshape(array_shapes[shape_index][0],array_shapes[shape_index][1]))
