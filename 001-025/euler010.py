#! /usr/bin/env python
# Project Euler problem 010: find sum of all primes under 2,000,000

import math

n = 2000000

def euler_sieve(v):
    """ Uses Euler's sieve algorithm to quickly return the list of all primes up to v. """

    global pfactors

    # Build table of odd numbers:
    num_tab = range(1,v,2) # starts 1,3,5,7,9,11...
    num_tab[0] = 2
    i = 1
    # Our biggest number in initial table:
    highestval = num_tab[-1]

    while 1:
        cx = num_tab[i]
        # Skip any empty values:
        if cx == False:
            i += 1
            continue
        # If we're beyond sqrt(n) there are no more primes
        if cx**2 > v:
            break
                        
        toRemove = []
        for j in xrange(i, len(num_tab)):
            # Find the second operator:
            cy = num_tab[j]
            if cy == False:
                continue
            cut = cx*cy
            if cut > highestval:
                # Gone too high
                break
            toRemove.append(cut)
            
        # Now sieve out the values:
        for d in toRemove:
            ind = (d-1)/2
            num_tab[ind] = False
    
        # Find the new highest value remaining by counting backwards:
        hiind = -1
        while num_tab[hiind] == False:
            hiind -= 1
        highestval = num_tab[hiind]
        
        i += 1

    return num_tab
    
primes = euler_sieve(n)

print primes
print sum(primes)