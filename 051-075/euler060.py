#! /usr/bin/env python
# Project Euler problem 060: find 5 primes for which any 2 concatenate to produce a prime


def concat(p1,p2):
    return int(str(p1) + str(p2))


# Primes import from file:
limit = 20000000 # 100 mil absolute outside limit (8-digit primes covered)
primes = []
loprimes = []
for line in open('primes_to_'+str(limit)+'.txt'):
    p = int(line)
    primes.append(p)
    # Filter low primes:
    if p < 10000:
        loprimes.append(p)
loprimes.remove(2)
loprimes.remove(5)
print len(primes), 'primes generated.'

# Strip out any low primes which aren't friends with 3:
print 'Assuming 3 is a required member.'
toremove = []
for p in loprimes:
    if concat(3,p) not in primes or concat(p,3) not in primes:
        toremove.append(p)
toremove.remove(3)
for t in toremove:
    loprimes.remove(t)

print len(loprimes), 'low primes remain.'


# Dict for results:
results = {}

# Pairs search:
for i in xrange(len(loprimes)):
    a = loprimes[i]
    # Limit a to 2 digits below max:
    if a >= 1000:
        break
    results[a] = []

    for j in xrange(i+1, len(loprimes)):
        b = loprimes[j]
        # Limit b to 1 digit below max:
        if b >= 10000:
            break
        # Test concatenations for primeness:
        if concat(a,b) < limit: # quick length test
            if concat(a,b) in primes and concat(b,a) in primes:
                results[a].append(b)

# Printout:
for r,l in results.items():
    if len(l) > 0:
        print r, l, len(l)
        maxr = r
print r, 'was max a'    


# Take 3 as our starting point and find triads:
print '\nTriads:'
triads = {}
for p in results[3]:
    if p > maxr:
        break
    triads[p] = []

    for q in results[p]:
        if q in results[3]:
            # triad found
            triads[p].append(q)

# Printout:
for r,l in triads.items():
    if len(l) > 0:
        print r, l


print '\nTetrads:'
tetrads = {}
for b,l in triads.items():
    for c in l:
        if c in results and len(results[c]) > 0:
            for d in results[c]:
                if d in results[3] and d in results[b]:
                    # tetrad found
                    tetrads[d] = [3,b,c]
print tetrads

# Got 153 triads and 3 tetrads for limit=1000000
# Got 89  triads and 3 tetrads for limit=2000000
# Got 115 triads and 9 tetrads for limit=20000000
