#! /usr/bin/env python
# Project Euler problem 035: how many circular primes under 1,000,000

import sys
sys.path.append('/Users/martin/Dropbox/Python/pythoncode/projecteuler/001-025')
import euler_sieve as euls


def is_circular_prime(p):
    # p is original, q is first copy
    q = p
    while 1:
        # rotate digits by 1:
        r = int(`q`[1:] +`q`[0])
        # test for full circle:
        if r == p:
            break
        # test for failing prime test:
        if r not in primes:
            return False
        # reload for next loop:
        q = r
    # all rotations were prime
    return True


def has_even_digit(n):
    # exception:
    if n == 2:
        return False
        
    s = str(n)
    # test for even digits:
    for i in range(0,9,2):
        if `i` in s:
            return True
    else: return False


primes = euls.euler_sieve(1000000)

count = 0

for p in primes:
    if p > 1 and not has_even_digit(p) and is_circular_prime(p):
        print p
        count += 1
        
print count, 'circular primes'
