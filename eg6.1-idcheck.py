#!/usr/bin/env python3

'check identify only for identifier more than 2 char'

import string

nums = string.digits
alphas = string.letters + '_'

print('Welcome to the Identifier checker v1.0 \n Testees must be at least 2 chars long')
myInput = input('Identifier to test?')

if len(myInput) >= 2:
	if myInput[0] not in alphas:
		print('invalid:first symbol must be alphabetic')
	else:
		for otherChar in myInput[1:]:
			if otherChar not in alphas + nums:
				print('invalid:remaining symbols must be alphanumeric')
				break
		else:	#for-else 循环语句只在for循环完整时没有遇到break，else才会执行
		    print('okay as an identigier')



