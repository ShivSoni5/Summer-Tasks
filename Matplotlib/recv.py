#!/usr/bin/python3

import  socket,time
import matplotlib.pyplot as plt

rec_ip="127.0.0.1"
myport=9999
#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  now connecting ip  and port 
s.bind((rec_ip,myport)) 
#  buffer size 
list_of_words = []

timeout = time.time() + 10
while time.time() < timeout:
	rec_data = s.recvfrom(1000)[0]
	decoded_data = rec_data.decode('utf-8')
	split_words = decoded_data.split()
	for i in range(len(split_words)):
		list_of_words.append(split_words[i])	
#		print(list_of_words)	

set_of_words=list(set(list_of_words))
#print(set_of_words)

x={}

for i in range(len(set_of_words)):
	x[set_of_words[i]] = list_of_words.count(set_of_words[i])

print(x)		

x_axis_label = list(x.keys()) 

x_axis_cor = list(range(1,len(x_axis_label)+1))

y_axis_height = list(x.values())

plt.bar(x_axis_cor, y_axis_height, tick_label = x_axis_label, width = 0.8)

plt.title("data visualization")

plt.xlabel('words --->')

plt.ylabel('frequency -->')

plt.show()



	
