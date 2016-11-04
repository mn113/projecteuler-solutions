#! /usr/bin/env python
# Project Euler problem 050: longest sequence of consecutive primes which sums to a prime < 1000000

import math

# Primes import from file:
primes = []
for line in open('../051-075/primes_to_1000000.txt'): # adjust
    primes.append(int(line))
l = len(primes)
print l, 'primes generated.'
percentile = 99 # adjust
# Copy list:
bigprimes = primes[int(math.floor(l * percentile/100)):]
print primes[0], 'is first prime,', primes[-1], 'is last,', bigprimes[0], 'is at', percentile, 'th percentile, ', len(bigprimes), 'above it'

import time
start = time.clock()

# Loop over chain length, decreasing:
chlen = 501 # adjust to be close to expected result
while 1:

    # Sum first chain of terms:
    chainsum = sum(primes[:chlen])
    for init in range(len(primes)-chlen):
        found = False
        # Test for primeness:
        if chainsum in bigprimes:
            print chlen, chainsum, init, time.clock() - start, 'sec'
            found = True
            break
        # Find next chainsum by adding next term, subtracting first:
        chainsum += primes[init + chlen]
        chainsum -= primes[init]
        
    if found:
        chlen += 10 # try longer chain
    else:
        chlen -= 2 # skip even length chains

# for 1000,   longest chain is 21,  sum 953,    found in 0.01 sec
# for 100000,         chain of 183, sum 92951,  found in 2 sec (90th percentile)
# for 200000,         chain of 251, sum 198197, found in 4 sec (98th percentile)
# for 500000,         chain of 393, sum 499607, found in 4 sec (99th percentile)
# for 1000000,        chain of 543, sum 997651, found in 16 sec (99th percentile)
