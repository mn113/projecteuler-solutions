#! /usr/bin/env python
# Project Euler problem 097: calculate last 10 digits of 28433*(2^7830457)+1

import time

start = time.clock()

a = 1
pwr = 7830457
binpwr = bin(pwr)[2:] # lose the '0b' prefix
#print binpwr
l = len(binpwr)
#print l
for d in range(l):
    pos = l-1-d
    if int(binpwr[pos]) == 1:
        a *= 2**(2**d)

print 28433 * a % (10**10) + 1

mid = time.clock()
print mid - start, 'sec'

print 28433 * (2**7830457) % (10**10) + 1

print time.clock() - mid, 'sec'