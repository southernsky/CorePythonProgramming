#!usr/bin/env python3
# -*- coding:utf-8 -*-

def testit(func,*nkwargs,**kwargs):
    try:
        retval = func(*nkwargs,**kwargs)
        result = (True,retval)
    except Exception as e:
        result = (False,e)
    return result

def test():
    funcs = (int,float)
    vals = (91234,12.34,'1234','12.34')
    for eachfun in funcs:
        for eachval in vals:
            retval = testit(eachfun,eachval)

            if retval[0]:
                pr='%s(%s) = %s' % (eachfun.__name__,eachval,retval[1])
                print(pr)

            else:
                print('%s(%s)= Failed:invalid literal for %s() :%s' % (eachfun.__name__,
                eachval,eachfun.__name__,eachval))


if __name__ =='__main__':
    test()


