#! /usr/bin/env python
# Project Euler problem 027: find equation coefficients such that n^2 +an +b produces many consecutive primes

# Maybe build a prime sieve up to 5000?

# Need a prime testing function

import sys
sys.path.append('/Users/martin/Desktop/Python/pythoncode/projecteuler/001-025')
import time
import euler_sieve as euls

primes = euls.euler_sieve(3000)

def is_prime(p):
    if p in primes:
        return True
    else:
        return False


# Example 1:
#for n in range(41):
#    p = n**2 + n + 41
#    print p, is_prime(p), n
#print '\n'

# Example 2:
#for n in range(81):
#    p = n**2 - 79*n + 1601
#    print p, is_prime(p), n
#print '\n'

# Testing my result:
time_start = time.time() 
for n in range(72):
    p = n**2 - 61*n + 971
    print p, is_prime(p), n
time_end = time.time() 
print "time taken", time_end-time_start
print '\n'


# My stuff:
for a in range(-1000,1000):
    for b in range(-1000,1000):
        n = 0
        while 1:
            p = n**2 + a*n + b
            if not is_prime(p):
                # Print any chains over 40
                if n > 40:
                    print n, a, b, p
                break;
            n += 1