#!/usr/bin/env python3

def displayNumType(num):
	print(num,'is'),
	if isinstance(num,(int,long,float,comples)):
		print('a number of type:',type(nubmer).__name__)
	else:
		print('not a number at all')
