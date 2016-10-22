#! /usr/bin/env python
# Project Euler problem 036: numbers palindromic in deceimal and binary

import binascii

def is_palindromic(n):
    s = `n`
    if s[::-1] == s:
        return True
    else:
        return False
        

total = 0

for i in range(1,1000000):
    if is_palindromic(i):
        b = bin(i)
        bs = `b` # this generates '0b1001011', need to remove some chars
        if is_palindromic(bs[3:-1]):
            print i, b, '*'
            total += i
                        
print 'Answer:', total