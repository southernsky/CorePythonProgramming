#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def safe_float(object):
    'safe version of float()'
    try:
        retval = float(object)
    except (ValueError,TypeError) as e:
        retval = str(e)
    return retval



def main():
    'handles all the data processing'

    log = open('/users/southernsky/desktop/cardlog.txt','w')
    try:
        ccfile = open('/users/southernsky/desktop/carddata.txt','r')
    except IOError as e:
        log.write('no txns this month\n')
        log.close()
        return

    total = 0.0
    for eachline in ccfile:
        result = safe_float(eachline)
        if isinstance(result,float):
            total += result
            log.write('data....processed\n')
        else:
            log.write('ignored:%s \n' % str(result))

    print('%.2f (new balance)\n' % total)
    log.close()

if __name__ == '__main__':
    main()






'''
def main():
    x = 0.0
    try:
        log = open('/users/southernsky/desktop/log.txt','w')
    except IOError:
        print('file error')

    with open('/users/southernsky/desktop/carddata.txt','r') as f:
        for eachline in f:
            y = safe_float(eachline)
            if isinstance(y,str):
                log.write('ignored invalid literal for float()\n')
            else:
                x += y
                log.write('data....processed\n')
        log.write(str(x))
    log.close()

if __name__ == '__main__':
    main()

'''

