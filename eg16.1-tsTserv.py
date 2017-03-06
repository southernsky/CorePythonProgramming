#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from socket import *
from time import ctime

HOST = ''
PORT = 21600
ADDR = (HOST,PORT)
bufsize = 1024

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
	print('waiting for connection...')
	tcpCliSock,addr = tcpSerSock.accept()
	print('...connected from',addr)

while True:
    data = tcpCliSock.recv(bufsize)
    if not data:
        break
    tcpCliSock.send('[%s] %s' % (ctime(),data))
    tcpCliSock.close()
tcpSerSock.close()



