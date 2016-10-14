#! /usr/bin/env python
# Project Euler problem 070: find the largest Totient value for n which is a permutation of n

import math


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
    return int(n)


# Primes import from file:
limit = 100000
sqrl = math.sqrt(limit)
primes = []
loprimes = []
for line in open('primes_to_'+str(limit)+'.txt'):
    p = int(line)
    primes.append(p)
    if p < sqrl:
        loprimes.append(p)
print len(primes), 'primes generated.'


# try all:
minrat = 10
for n in range(10,10000):
    if n in primes:		# totient of a prime p is p-1: definitely not a perm
        continue
    p = phi(n)
    r = 1.0 * n/p
    if r < 1.1:			# high totient, good sign
        if sorted(str(p)) == sorted(str(n)):	# permutation match found so n is a real candidate
            if r < minrat:
                minrat = r
                print n, '/', p, '=', r


# results:
# 9983167 / 9973816 = 1.00093755489 - incorrect
# 7026037 / 7020736 = 1.00075504904 - incorrect
# 940417 / 917440 = 1.02504468957
# 880567 / 878560 = 1.00228441996 - incorrect
# 783169 / 781396 = 1.00226901597 - incorrect
# 474883 / 473488 = 1.00294622039

# Gonna need to speed up if we're testing to 10 million!
# n = 7026037 = 2693 * 2609
# multiply 2 low primes... phi(mn) = phi(m)*phi(n)
# start dict of {n:phi(n)}
# populate it multiplicatively
# answer lies within??

phitable = {}
for i in range(len(loprimes)):
    p = loprimes[i]
    for j in range(i+1,len(loprimes)):
        q = loprimes[j]
        m = p * q
        # Insert into dict:
        if m not in phitable:
            phitable[m] = phi(m)
print 'Phitable ready, length', len(phitable)
#print phitable

minrat = 100
for x,f in phitable.items():
    r = 1.0 * x/f
    if r < 1.1:			# high totient, good sign
        if sorted(str(x)) == sorted(str(f)):	# permutation match found so n is a real candidate
            if r < minrat:
                minrat = r
                print x, '/', f, '=', r

