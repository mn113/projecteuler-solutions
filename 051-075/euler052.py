#! /usr/bin/env python
# Project Euler problem 052: smallest x such that digits of x, 2x, 3x, 4x, 5x and 6x are same


def same_digits(a,b):
    if set(str(a)) == set(str(b)):
        return True
    else:
        return False
        
i = 0    
while 1:
    i += 1
    if same_digits(i,2*i) and same_digits(i,3*i) and same_digits(i,4*i) and same_digits(i,5*i) and same_digits(i,6*i):
        print i
        break
    if i > 1000000:
        break