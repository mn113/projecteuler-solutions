#! /usr/bin/env python
# Project Euler problem 009: find a Pythagorean triplet for which a + b + c == 1000

import math

for a in range(1,300):
    for b in range(1,500):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print a,b,c
            print a*b*c
else:
    print 'no result'
    