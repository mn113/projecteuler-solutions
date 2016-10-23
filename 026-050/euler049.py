#! /usr/bin/env python
# Project Euler problem 049: 3 equidistant 4-digit primes which are digit-permutations

import sys
sys.path.append('/Users/martin/Dropbox/Python/pythoncode/projecteuler/001-025')
import euler_sieve as euls
import time


def get_permutations(n):
    digits = str(n)
    d1,d2,d3,d4 = [],[],[],[]
    s = set()

    for d in digits:
        d4.append(int(d))
        d3.append(int(d) * 10)
        d2.append(int(d) * 100)
        d1.append(int(d) * 1000)

    for w in d1:
        for x in d2:
            for y in d3:
                for z in d4:
                    perm = w + x + y + z
                    # only accept it if digits match original:
                    if sorted(str(perm)) == sorted(str(n)):
                        s.add(perm)

    l = list(s)
    l.sort
    return l



start = time.clock()

# prime sieve, remove False values with set-list-set trickery:
primes = set(list(set(euls.euler_sieve(10000)))[1:])
print 'Primes ready.'

#print get_permutations(1234)

for p in primes:
    if p < 1000:
        continue

    perms = get_permutations(p)
    for q in perms:
        if q > p and q in primes:
            # found one prime permutation, now look for next:
            for r in perms:
                if r > q and r in primes:
                    # found a second, now compare distances:
                    if r - q == q - p:
                        # arithmetic series
                        print p, q, r
                        break

print time.clock() - start, 'sec'