#!/usr/bin/env python3
# -*- coding:utf-8 -*-

stack = []

def pushit():
	#stack.append(input('Enter New String').strip())
	newstring = input('Enter New String\n').strip()
	stack.append(newstring)
	print(newstring,'is add to stack')

def popit():
	if stack == []:
		print('Error,cannot pop from an empty stack')
	else:
		delstring = stack.pop()
		print(delstring,'is delete from stack')

def viewstack():
	print(stack)

def showmenu():
	CMDs = {'u':pushit,'o':popit,'v':viewstack}
	pr ='''
		u = push
		o = pop
		v = view
		q = quit
		Enter choice:\n'''

	while True:
		while True:
			while True:
				try:
					choice = input(pr).strip().lower()
				except (EOFError,KeyboardInterrupt,IndexError):
					print('Error,invalid option,try again')
				else:
					break

			if choice not in 'uovq':
				print('invalid option,try again')
			else:
				break

		if choice == 'q':
			break
		else:
			CMDs[choice]()

if __name__ == '__main__':
	showmenu()



