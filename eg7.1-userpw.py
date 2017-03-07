#!/usr/bin/env python3
# -*- coding:utf-8 -*-

db = {}

def newuser():
    prompt = 'login name:\n'
    while True:
        name = input(prompt)
        if name in db:
            prompt = 'name exists,try another\n'
            continue
        else:
            break
    pwd = input('password\n')
    db[name] = pwd
    print('new user has been added')

def olduser():
    prompt = 'login name:\n'
    while True:

        while True:
            name = input(prompt)
            if name not in db:
                prompt = 'name error,try again\n'
            else:
                break
        prompt = 'password\n'
        while True:
            pwd = input(prompt)
            if db[name] == pwd:
                print('welcome back')
                break
            else:
                prompt = 'password error,try again\n'
        break

def showmenu():
    prompt = '''
    (N)ew User Login
    (E)xisting User Login
    (Q)uit

    Enter choice\n'''



    while True:

        while True:

            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError,IndexError):
                choice = 'q'
            #else:
            if choice in 'neq':
                break
            else:
                print('invalid option,try again')

        if choice == 'q':break
        if choice == 'n':newuser()
        if choice == 'e':olduser()


if __name__ == '__main__':
    showmenu()








