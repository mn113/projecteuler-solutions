#! /usr/bin/env python
# Project Euler problem 072: how many reduced fractions for denominator up to 1000000?


import sys

def get_prime_factors(m):
    factors = set()
    for p in primes:
        if p >= m:
            break
        while m % p == 0:
            m = m/p
            factors.add(p)
        if m == 1:
            break
    return factors


# Primes import from file:
primes = set([])
for line in open('primes_to_1000000.txt'):
    primes.add(int(line))
print len(primes), 'primes generated.'

limit = 100000
denoms = xrange(2,limit+1)
fractions = []

for d in denoms:
    pfd = get_prime_factors(d)
    numers = range(1,d)
    # Sieve numers:
    for f in pfd:
        ff = f
        while ff < d:
            numers.remove(ff)
            ff = ff + f
    # Now all of numers should be rel. prime to d
    for n in numers:
        fractions.append((n,d))

    # Progress indicator:
    pct = limit/100
    if d % pct == 0:
        sys.stdout.write(str(d/pct) + '%\r')
        sys.stdout.flush()

print len(fractions)