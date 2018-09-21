#!/usr/bin/python2

import  socket 
from time import sleep
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
        a = input()
        b = a.encode('utf-8')
        s.sendto(b,("127.0.0.1",9999))
        sleep(2)


