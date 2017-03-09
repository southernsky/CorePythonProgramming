#!/usr/bin/env python3
# -*-coding:utf=8 -*-

def convert(fun,seq):
    'convert sequence of numbers to same type'
    return [fun(eachnum) for eachnum in seq]

seq = [123,45.67,-6.2e8,99999]

print(convert(int,seq))
print(convert(float,seq))

