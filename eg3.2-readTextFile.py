#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'readTextFile.py -- read and display text file'

# get filename

fname = input('Enter filename')

# attempt to open file for reading 

try:
	fobj = open(fname,'r')   #open方法赋值后的fobj并非是存储文件内容的变量
except IOError,e:
	print('file open error',e)
else:
	# display contents to the screen
	for eachline in fobj:
		print(eachline)
	fobj.close()


