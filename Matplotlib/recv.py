#!/usr/bin/python2

import  socket,time

rec_ip="127.0.0.1"
myport=9999
#                 ipv4       ,  for UDP   
#   only  for rec                      
#  below method with argument creating a socket called  s 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  now connecting ip  and port 
s.bind((rec_ip,myport)) 
#  buffer size 
c = []

timeout = time.time() + 10
while time.time() < timeout:
	a = s.recvfrom(1000)[0]
	d = a.decode('utf-8')
	b = d.split()
	for i in range(len(b)):
		c.append(b[i])	
#		print(c)	

d=list(set(c))
print(d)
		
