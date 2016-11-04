#! /usr/bin/env python
# Project Euler problem 026: longest recurring decimal up to 1/1000

#loop thru prime factors to 1000
#string analysis: test for recurrent strings of length 2,3,4,5....

import math
import euler_sieve as euls
from decimal import *
# Set up Decimal type precision: 1000 decimal places (!!!!)
getcontext().prec = 1000

n = 1000
primes = euls.euler_sieve(n)
fractions = []
recurrences = {}
largest = 0

for p in primes:
    if p > 6:
        q = 1/Decimal(p)
        fractions.append(q)
        #print p, ':', q

        qdigits = str(q)
        #print qdigits,
        for n in range(1,1000):
            # Multiply substring by prime
            #print qdigits[2:2+n],
            prod = str(p * int(qdigits[2:2+n]))
            #print prod, set(prod)
            # If result is 9's, period of recurrence was found 
            if set(prod) == set(['9']):
                break
        
        # Store result
        recurrences[p] = n
        if n > largest and n != 999:
            largest = n
        #print n, 'digits'

print recurrences
print largest

# all the fractions are rational, therefore they all recur
        
#  2: 0
#  3: 1 digit
#  5: 0
#  7: 6 digit
# 11: 2 digit
# 13: 6 digit
# 17: 16 digits
# 19: 18 digits
# 23: 22 digits
# 29: 28 digits
# 31: 15 digits
# 37: 3 digit
# 41: 5 digit
# 43: 21 digits
# 47: 39 digits
# 53: 13
# 59: 58
# 61: 60
# 67: 33
# 71: 35
# 73: 8
# 79: 13
# 83: 41
# 89: 44
# 97: 96

# 983: 982 digits = solution!

