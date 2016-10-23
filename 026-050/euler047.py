#! /usr/bin/env python
# Project Euler problem 047: four consecutive integers having four distinct prime factors

import sys
sys.path.append('/Users/martin/Dropbox/Python/pythoncode/projecteuler/001-025')
import euler_sieve as euls
import time


def get_prime_factors(m):
    factors = set()
    for p in primes:
        while m % p == 0:
            m = m/p
            factors.add(p)
        if m == 1:
            break
    return factors



start = time.clock()

lim = 1000

# prime sieve, remove False values with set-list-set trickery:
primes = set(list(set(euls.euler_sieve(lim)))[1:])
print 'Primes ready.'

# find all the numbers with 4 prime factors, store in Boolean dict:
print 'Factorising...',
fourfactors = {}
for i in range(1,lim**2):
    if len(get_prime_factors(i)) == 4:
       fourfactors[i] = True
    else:
       fourfactors[i] = False
print 'done.'

# look for 4 consecutive ones:
print 'Searching for consecutive hits...'
for f in fourfactors:
    if fourfactors[f] and fourfactors[f+1] and fourfactors[f+2] and fourfactors[f+3]:
        print f, get_prime_factors(f)
        print f+1, get_prime_factors(f+1)
        print f+2, get_prime_factors(f+2)
        print f+3, get_prime_factors(f+3)
        break
else:
    print 'None found.'
        
print time.clock() - start, 'sec'