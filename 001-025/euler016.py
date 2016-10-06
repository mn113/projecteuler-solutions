#! /usr/bin/env python
# Project Euler problem 016: find the sum of digits of 2^1000

n = 2**1000
print n

count = 0

# Stringify:
w = str(n)
# Sum digits:
for i in range(len(w)):
    count += int(w[i])
    
print '\n', count