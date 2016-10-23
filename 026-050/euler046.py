#! /usr/bin/env python
# Project Euler problem 046: smallest odd composite not expressable as prime + 2*n^2

import sys
sys.path.append('/Users/martin/Dropbox/Python/pythoncode/projecteuler/001-025')
import euler_sieve as euls
import time

start = time.clock()

lim = 6000

# prime sieve:
primes = set(euls.euler_sieve(lim))

# squares lookup:
squares = set([x**2 for x in range(1,lim)])

# build a Goldbach set of (supposedly) all the odd composites:
print 'Building Golbach set...',
goldbach = set()
for p in primes:
    if p and p > 2:
        for s in squares:
            g = p + 2*s
            if not (g % 2 == 0) and g not in primes:
                goldbach.add(g)
print 'done.'

# now sequentially test every odd composite for Golbach membership:
print 'Testing candidates...'
i = 1
while 1:
    i += 1
    # ignore evens:
    if i % 2 == 0:
        continue
    # ignore primes:
    if i in primes:
        continue

    if i not in goldbach:
        # the number disproves Goldbach's conjecture
        print i, 'fails'
        break

print time.clock() - start, 'sec'