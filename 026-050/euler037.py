#! /usr/bin/env python
# Project Euler problem 037: find sum of 11 truncatable primes

import sys
sys.path.append('/Users/martin/Dropbox/Python/pythoncode/projecteuler/001-025')
import euler_sieve as euls


def is_bi_truncatable(p):
    # from the right:
    q = p
    while 1:
        # truncate 1 digit:
        r = int(`q`[:-1])
        if r not in primes:
            return False
        if r < 10:
            break
        q = r
        
    # now from left:
    s = p
    while 1:
        # truncate 1 digit:
        t = int(`s`[1:])
        if t not in primes:
            return False
        if t < 10:
            break
        s = t
    
    # no non-prime substrings were found:
    return True    


def has_even_digit(n):
    s = str(n)
    # test for even digits:
    for i in [0,2,4,5,6,8]:
        if `i` in s[1:]:  # make an exception for first digit
            return True
    else: return False


primes = euls.euler_sieve(800000)

truncs = []

for p in primes:
    if p > 10 and not has_even_digit(p) and is_bi_truncatable(p):
        print p
        truncs.append(p)
        
print truncs
print len(truncs), 'of them'

total = 0
for t in truncs:
    total += t
print total