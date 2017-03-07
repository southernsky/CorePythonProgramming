#!/usr/bin/env python3
# -*- coding:utf-8 -*-

queue = []

def enQ():
    queue.append(input('Enter a string\n').strip())

def deQ():
    if len(queue) == 0:
        print('cannot pop from an empty queue!')
    else:
        print('Removed',queue.pop(0))

def viewQ():
    print(queue)

def showmenu():

    CMDs = {'e':enQ,'d':deQ,'v':viewQ}
    pr = '''
    e = enqueue
    d = dequeue
    v = view
    q = quit
    Enter choice:\n'''

    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except (EOFError,KeyboardInterrupt,IndexError):
                choice = 'q'

            print('you picked:%s' % choice)
            if choice not in 'devq':
                print('invalid option,please try again')
            else:
                break

        if choice == 'q':
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()

