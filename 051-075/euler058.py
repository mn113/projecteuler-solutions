#! /usr/bin/env python
# Project Euler problem 058: how many primes in the diagonals of a number spiral?
# c      b
#
#
#      n
# d      a
# See Ulam's spiral, Hardy & Littlewood's Conjecture F, polynomials

import math

# Primes import from file:
primes = set([])
for line in open('primes_to_20000000.txt'):	# can't get primes to 300mil yet, malloc error
    primes.add(int(line))
print len(primes), 'primes generated.'

# for maxi in range(14141,20001,2):

# Gather all the diagonals:
#maxi = 15811 # prime sieve must go up to this squared (and must be odd)
maxi = 981 # prime sieve must go up to this squared (and must be odd)
diags = set([1])
#for n in range(1,maxi,2):	# 1,3,5
#    a = (n+2)**2			# 9,25,49		or a = n**2 (for odd n)
#    n = n**2				# 1,9,25
#    b = n + (a-n)*1/4		# 3,13,31		or b = n**2 - n + 1 (for even n)
#    c = n + (a-n)*2/4		# 5,17,37		or c = n**2 + 1 (for even n)
#    d = n + (a-n)*3/4		# 7,21,43		or d = n**2 - n + 1 (for odd n)
#
#    diags |= set([a,b,c,d])

# odd n:
for n in range(1,maxi+2,2):	# 1,3,5
    a = n**2				# 1,9,25,49
    d = n**2 - n + 1		# 1,7,21,43

    diags |= set([a,d])

# even n:    
for n in range(2,maxi,2):	# 2,4,6
    b = n**2 + 1			# 5,17,37,65
    c = n**2 - n + 1		# 3,13,31,57

    diags |= set([b,c])


#print diags
# Sets intersection:
pdiags = diags & primes

print len(pdiags), '/', len(diags), '=', len(pdiags)/(len(diags)+0.0)
print 'max:', maxi

#    11 -> 47.6% prime
#    31 -> 37.7% prime
#    49 -> 28.9% prime
#   309 -> 19.9% prime
#   981 -> 14.9% prime
#  4001 -> 12.8% prime
#  9999 -> 11.2% prime
# 15811 -> 10.6% prime
#     ? ->  9.9% prime - cannot go big enough!


# EQ1: n**2			-> S
# EQ2: n**2     + 1 -> S+1
# EQ3: n**2 - n + 1	-> P+1

# density = sqrt(n) / log(n)

print "Trying Littlewood..."
for n in range(2,20000):
    p = math.sqrt(n) / math.log(n)
    if p < 0.1:
        print p, n
        break
        