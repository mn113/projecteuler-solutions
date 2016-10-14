#! /usr/bin/env python
# Project Euler problem 071: find reduced fraction closest to but under 3/7

# n needs to be coprime to d to speed up search
# find first few prime factors of d
# if any divide n, discard n

import sys


def fewfactors(x):
    return [i for i in [2,3,5,7,11] if x % i == 0]


denoms = xrange(1,1000001)

ts = 3.0 / 7	# 0.428571
hi = 0.426
hif = (0,0)

for d in denoms:
    a = int(d * hi)		# lower bound for numerator
    z = int(d * ts)		# upper bound for numerator
    for n in range(a,z):
        for i in fewfactors(d):
            if n % i == 0:		# discard this n if n & d share common prime factors
                continue
        f = 1.0 * n / d
        if f < hi:		# fraction too low, keep incrementing n
            continue
        elif f >= ts:	# fraction too high, stop
            break
        if f > hi:		# new max
            hi = f
            hif = (n,d)

    # Progress indicator:
    if d % 10000 == 0:
        sys.stdout.write(str(d/10000) + '%\r')
        sys.stdout.flush()

print '\n', hif[0], '/', hif[1], '=', hi

# answer was 428570 / 999997