#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from operator import add,sub
from random import randint,choice

ops = {'+':add,'-':sub}


def doprob():
    nums = [randint(1,10) for i in range(2)]
    #nums = [randint(1,0),randint(1,10)]
    nums.sort(reverse=True)
    op = choice('+-')
    ans = ops[op](*nums)
    pr = '%d %s %d = ' % (nums[0],op,nums[1])
    Maxtry = 3

    while True:
        try:
            if Maxtry == 0:
                print('answer is',ans)
                break

            if ans == int(input(pr)):
                print('correct')
                break
            else:
                Maxtry -= 1
                print('incorrect,try again,you have %s chance' % Maxtry)

        except (IOError,KeyboardInterrupt,EOFError,ValueError):
            print('invalid input,try again\n')

def main():
    while True:
        doprob()
        try:
            opt = input('Again?[y]\n').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt,EOFError):
            break

if __name__ == '__main__':
    main()








