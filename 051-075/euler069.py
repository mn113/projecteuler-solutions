#! /usr/bin/env python
# Project Euler problem 069: largest Totient value for n <= 1000000

def get_prime_factors(m):
    factors = set()
    for p in primes:
        while m % p == 0:
            m = m/p
            factors.add(p)
        if m == 1:
            break
    return factors


def phi(n):
    factors = get_prime_factors(n)
    for f in factors:
        # recursive math function:
        n = n * (1 - (1.0/f))
    return n


# Primes import from file:
primes = set([])
for line in open('primes_to_1000000.txt'):
    primes.add(int(line))
print len(primes), 'primes generated.'


# try all:
hi = 0
for n in range(10,1000000,10):
    p = phi(n)
    if n/p > hi:
        hi = n/p
        print n, p, n/p
    
print hi, 'was the highest'