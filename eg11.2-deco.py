#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from time import ctime,sleep

def tsfun(fun):
    def wrappendFun():
        print('[%s] %s() called' % (ctime(),fun.__name__)




@tsfun
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    foo()
    sleep(1)

