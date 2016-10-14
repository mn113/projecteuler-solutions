#! /usr/bin/env python
# Write a text file of primes up to a limit

import math
import sys
sys.path.append('/Users/martin/Dropbox/Python/pythoncode/projecteuler/001-025')
import euler_sieve as euls


def segmentize(lim):
    """ Splits inputs exceeding 100 million into manageable segments for sieving. """

    #for x in range(0,lim,100000000):
        


def euler_sieve(v):
    """ Uses Euler's sieve algorithm to quickly return the list of all primes up to v. """

    global pfactors

    # Build table of odd numbers:
    num_tab = range(1,v,2) # starts 1,3,5,7,9,11...
    num_tab[0] = 2
    print 'table ready'
    i = 1
    # Our biggest number in initial table:
    highestval = num_tab[-1]

    while 1:
        cx = num_tab[i]
        # Skip any empty values:
        if cx == False:
            i += 1
            continue
        # If we're beyond sqrt(n) there will be no more primes remaining
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
        print 'sieving...'
        for d in toRemove:
            ind = (d-1)/2 # weird way...
            num_tab[ind] = False

        # Find the new highest value remaining by counting backwards:
        hiind = -1
        while num_tab[hiind] == False:
            hiind -= 1
        highestval = num_tab[hiind]

        i += 1

    return num_tab


# Atkin sieve:
def atkin_sieve(limit):
    """ Uses Atkin's sieve algorithm to quickly return the list of all primes up to v.
        Supposed to be slightly faster and more memory-efficient than Euler's.
    """

    # arbitrary search limit
    lim_sqrt = int(math.ceil(math.sqrt(limit)))

    # initialize the sieve as a dict
    is_prime = {}
    for i in range(0,limit):
        is_prime.setdefault(i, False)

    # put in candidate primes: 
    # integers which have an odd number of representations by certain quadratic forms
    for x in range(int(math.ceil(math.sqrt(limit / 4)))):
        for y in range(int(math.ceil(math.sqrt(limit - 4*x*x)))):
            n = 4*x*x + y*y
            if (n > limit):
                break
            if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            n = 3*x*x + y*y
            if (n <= limit) and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x*x - y*y
            if (x > y) and (n <= limit) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]

    # eliminate composites by sieving
    for n in range(5, lim_sqrt):
        if is_prime[n]:
            # n is prime, omit multiples of its square; this is sufficient because composites
            # which managed to get on the list cannot be square-free
            m = n*n
            for p in range(1, limit):
                is_prime[p*m] = False

    # collect in list:
    result = [2,3]
    for n in range(5, limit):
        if is_prime[n]:
            result.append(n)
    return result


# Deal with arguments:
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print 'Usage: primewriter.py limit'
        sys.exit(0)
    lim = sys.argv[1]

outputfile = 'primes_to_'+lim+'.txt'


# Generate:
primes = list(set(euler_sieve(int(lim))))[1:]
primes.sort()
#primes = atkin_sieve(int(lim))		# also works
print len(primes), 'primes generated up to', lim


# Write out:
o = open(outputfile, 'w')
for p in primes:
    o.write(str(p)+'\n')
o.close()
print 'Written to ', outputfile