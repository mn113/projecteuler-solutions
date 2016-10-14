#! /usr/bin/env python
# Project Euler problem 065: sum of digits in numerator of 100th convergent of the continued fraction for e?

# coeffs = [2; 1,2,1, 1,4,1, 1,6,1, ..., 1,66,1]
# k:        1  2 3 4  5 6 7  8 9           99 100

import math

def divisors(n):
    d = []
    for i in range(2, 1000): # only simple divisors need to be checked
        if n%i == 0:
            d.append(i)
    return d


# build series:
coeffs = [0] # term 0 will not be used
for k in range(1,101):
    coeffs.append(1)
    if k % 3 == 0:
        coeffs[k] = k*2/3
coeffs[1] = 2
print coeffs


# work backwards through expansion:
for k in range(2, 101):
    print k,
    # start val (bottom term):
    frac = (coeffs[k], 1)

    while 1:
        # inverting:
        frac = (frac[1], frac[0])
    
        # adding term:
        t = (coeffs[k-1] * frac[1], 1 * frac[1])
        frac = (t[0] + frac[0], frac[1])
    
        # iterate backwards:
        k = k - 1
        if k <= 1: break

    # simplify fraction:
    for d in divisors(frac[0]):
        if frac[1] % d == 0:
            frac = (frac[0]/d, frac[1]/d)

    print frac

print str(frac[0])
print sum([int(d) for d in str(frac[0])])