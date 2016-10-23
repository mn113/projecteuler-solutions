#! /usr/bin/env python
# Project Euler problem 041: largest pandigital prime

# pmax = 987654321


import sys
sys.path.append('/Users/martin/Dropbox/Python/pythoncode/projecteuler/001-025')
import euler_sieve as euls
import time

def has_zeros(n):
    if '0' in str(n):
        return True
    else:
        return False


def has_dupe_digits(n):
    # convert to set, check size
    if len(set(str(n))) == len(str(n)):
        return False
    else:
        return True


def minimal_digits(n):
    for d in str(n):
        # a digit greater than its length will invalidate it
        if int(d) > len(str(n)):
            return False
    else:
        return True

start = time.clock()

primes = euls.euler_sieve(7654321)

# output largest prime in sieve
i = 0
while 1:
    i -= 1
    if primes[i]:
        print primes[i]
        break


for p in primes:
    if p > 1000 and not has_zeros(p) and not has_dupe_digits(p) and minimal_digits(p):
        print p
      
print time.clock() - start, 'sec'