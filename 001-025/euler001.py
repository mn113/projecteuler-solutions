#! /usr/bin/env python
# Project Euler problem 001: sum all multiples of 3 or 5 below 1000

count = 0

for x in range(1000):

    if x % 5 == 0:
        count += x
    elif x % 3 == 0:
        count += x
        
print count