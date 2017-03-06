#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from socket import *

HOST = 'localhost'
PORT = 21600
ADDR = (HOST,PORT)
BUFSIZE = 1024

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = input('please input a word')
	if not data:
		break
	tcpCliSock.send(data)
	DATA = tcpCliSock.recv(BUFSIZE)
	if not DATA:
		break
	print(DATA)
tcpCliSock.close()
