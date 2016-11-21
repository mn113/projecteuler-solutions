#! /usr/bin/env python
# Project Euler problem 243: find smallest denominator with resilience below 15499/94744 (= 0.164)

# d gives d-1 proper fractions: 1/d, 2/d, 3/d etc.
# how many of these fractions x/d can be cancelled down? -> common factor between x & d
# we simply need list all of factors of d (the more the better)

# d = 30	-> 1,7,11,13,17,19,23,29	-> Resilience 8/29 = 0.276
# d = 24	-> 1,5,7,11,13,17,19,23	-> Resilience 8/23 = 0.348
# d = 18	-> 1,5,7,11,13,17		-> Resilience 6/17 = 0.353
# d = 12	-> 1,5,7,11		-> Resilience 4/11 = 0.363 (quite low)
# d = 11	-> all			-> Resilience 10/10 (pointless to look at primes)
# d = 10	-> 1,3,7,9		-> Resilience 4/9
# d = 9		-> 1,2,4,5,7,8	-> Resilience 6/8
# d = 8		-> 1,3,5,7		-> Resilience 4/7

# d should probably be a multiple of 2,3 & 5, maybe more

# n needs to be coprime to d to speed up search
# find first few prime factors of d
# if any divide n, discard n

import sys


def are_coprime(a,b):
    # factorise a
    factors = []
    for i in range(2,a+1):
        if a % i == 0:
            factors.append(i)
    # check factors into b
    for f in factors:
        if b % f == 0:
            # common factor found
            return True
    else:
        return False
        

def list_factors(d):
    notcoprimes = []
    for n in range(1,d):
        if not are_coprime(n,d):
            notcoprimes.append(n)
    return notcoprimes


def resilience(d):
    return 1.0 * (d - len(list_factors(d))) / d


# Primes import from file:
primes = []
for line in open('../051-075/primes_to_1000000.txt'):
    primes.append(int(line))
print len(primes), 'primes loaded.'


# Testing from 12 up:
denoms = xrange(12,1000001)
for d in denoms:
    coprimes = []
    limit = d * 15499.0 / 94744 # not allowed more than this many resilient fractions
    for n in range(1,d):
        if are_coprime(n,d):
              coprimes.append(n)
              if len(coprimes) >= limit: # one too many resilients found, break and proceed to next d
                  break
    # If limit not reached, we have found a good d:
    print d, "has", len(coprimes), "coprimes:", coprimes
    print "R(d) =", resilience(d)
    break

