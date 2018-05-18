#!/usr/bin/python2

import  socket 
from time import sleep
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

a="hiiii this is my naeme"
b=a.encode('utf-8')

while True:
	sleep(3)
	s.sendto(b,("127.0.0.1",9999))


