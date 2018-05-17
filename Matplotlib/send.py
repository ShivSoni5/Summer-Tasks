#!/usr/bin/python2

import  socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

a="hiiii this is my naeme"
b=a.encode('utf-8')

s.sendto(b,("127.0.0.1",9999))


