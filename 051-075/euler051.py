#! /usr/bin/env python
# Project Euler problem 051: smallest prime which, by replacing some part, yields 8 primes

import itertools
   

def subbits(plen, n, bitmask, digit):
    n = str(n)
    m = ''
    for i in range(plen):
        if bitmask[i] == '1':
            m += str(digit)
        else:
            m += n[i]
    return int(m)


# Primes import from file:
primes = []
for line in open('primes_to_1000000.txt'):
    if len(line) - len(set(line)) >= 2:	# very likely our prime will have multiple repeated digits
        primes.append(int(line))
print len(primes), 'primes generated.'
       
plen = 6
target = 8 # size of prime family sought
digits = range(10)

# Filter out primes above and below chosen length:
primes[:] = [p for p in primes if p >= 10**(plen-1) and p < 10**plen]
print len(primes), 'primes remain'


# how many digits to replace?
bitmasks = set([])
for sublen in range(1, plen):
    # calculate all perms as bitmasks:
    source = '1'*sublen + '0'*(plen - sublen) # ok
    print 'src:', source
    perms = list(itertools.permutations(source, plen)) # ok
    bitmasks.update([x for x in perms if x[-2] == '1' and x[-1] == '0']) # no point cycling last digit (as evens not prime)
print 'bm:', bitmasks

# substitute in bits
i = 0
for p in primes:
    if i % 100 == 0:
        print p, 'testing...'
    i = i + 1

    # try every combination:
    for bm in bitmasks:
        solution = []
        failcount = 0
        # for replacement digit 0-9:
        for d in digits:
            # perform replacement:
            q = subbits(plen, p, bm, d)
            # result needs to be prime
            if q not in primes:
                failcount = failcount + 1
            else:
                solution.append(q)
            # looking for a family of 8 => only 2 fails allowed:
            if failcount > 10 - target:
                break
        if failcount < 10 - target:
            print p, bm, 10 - failcount
        if failcount == 10 - target:
            print solution
            exit()
    
    # p's variations gave no results so p can be discarded from master list
    primes.remove(p)
            

# plen=2, maxcount=6
# plen=3, maxcount=6
# plen=4, maxcount=6
# plen=5, maxcount=7, time=2sec,  1717  candidate primes (90007)
# plen=6, maxcount=8, time=26sec, 27000 candidate primes (121313)


# certain bitmasks are going to make large prime families:
#     10 good
#    010 good
#   1010 good
#   0110 good
#  00110 good
# 101010 good
