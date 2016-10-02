#! /usr/bin/env python
# Project Euler problem 003: find largest prime factor of 600851475143

import math

n = 1234567890123
n = 600851475143
#n = 31851475143 # 
#n = 2851475143 # 
#n = 851475143 # malloc error
#n = 223092870 # gives 23 in 44 sec
#n = 51475143 # gives 12497 in 15 sec
#n = 9699690 # gives 19 in 1.2 sec
#n = 931957 # gives 17 in 0.3 sec
#n = 13195 # gives 29 in 0.03 sec

m = n # Will be the shrinking quotient of n

def is_prime(p): # STOP USING THIS LETHARGIC FUNCTION
    """ Returns True if p is prime, False if not. """

    for q in range(2, int(math.floor(math.sqrt(p)))):
        if p % q == 0:
            return False
    else:
        return True


def euler_sieve(v):
    """ Uses Euler's sieve algorithm to quickly return the list of all primes up to v. """

    global m, n, pfactors
    done = False
    
    # Eliminate factor 2:
    if v % 2 == 0:
        v = v/2
        pfactors.add(2)
        
    # Build table of odd numbers:
    if v > 100000000:
        w = int(math.floor(math.sqrt(v)))
        num_tab = range(1,w,2) # starts 1,3,5,7,9,11...
    else:
        num_tab = range(1,v,2) # starts 1,3,5,7,9,11...
    num_tab[0] = 2
    i = 1
    # Our biggest number in initial table:
    highestval = num_tab[-1]

    while not done:
        cx = num_tab[i]
        # Skip any empty values:
        if cx == False:
            i += 1
            continue
        # If we're beyond sqrt(n) there are no more primes
        if cx**2 > v:
            break
        # Test for being a factor of n:
        if v % cx == 0:
            # Found one:
            pfactors.add(cx)
            m = v/cx # The quotient, for our next iteration
            print m, '=', v, '/', cx 
            euler_sieve(m)
            done = True
                        
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

    return
    
# Start finding prime factors of n:
pfactors = set()
euler_sieve(n)
pfactors.add(m) # Final factor found during the loop

print pfactors
print max(pfactors)
