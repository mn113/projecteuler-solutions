#! /usr/bin/env python
# Project Euler problem 060: continuation: find a fifth prime given pre-calculated tetrads


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


tetrads = [[3,7,109,673], [3,37,67,2377], [3,37,67,5923],
           [3,17,449,6599], [3,11,701,8747], [3,331,739,8431],
           [3,17,449,6353], [3,17,449,2069], [3,7,541,4159]]
basis = set([])
for tet in tetrads:
    for t in tet:
        basis.add(t)
print 'basis:', basis
"""

# Look for primes that start or end with a tetrad-member:
possibles = set([])
for n in basis:
    print 'Trying', n, '...'
    for p in primes:
        sp = str(p)
        sn = str(n)
        ln = len(sn)
        sk = ''
        if sp[:ln] == sn:		# start match
            sk = sp[ln:]
        elif sp[-ln:] == sn:	# end match
            sk = sp[:-ln]
        else:					# no match
            continue
        k = int('0' + sk)
        if len(str(k)) + ln == len(sp):	# lengths must add up, otherwise zeroes sneak in
            if k in loprimes:
                print n, k, ' & ', k, n, ' > ', p
                possibles.add(k)

print possibles, len(possibles)

# 946 possibles found from the basis of 8
# 143 possibles from the 9 tetrads

print '\nFifth prime:'
fifths = set([])
for p in possibles:
    count = 0
    for t in basis:
        conc = int(str(p) + str(t))
        if conc in primes:
            count = count + 1
            if count >= 4:
                fifths.add(p)
print fifths
"""                
               
fifths = [6529, 3, 7, 11, 6637, 8431, 17, 2707, 2069, 1051, 541, 31, 5281, 1699, 37, 1193, 557, 6451, 8629, 7369, 3769, 607, 701, 5449, 4159, 449, 67, 9157, 1607, 73, 823, 499, 5923, 1237, 8377, 2377, 331, 3931, 673, 2143, 739, 2789, 359, 3049, 109, 613, 229, 1907, 373, 7159, 4729, 191, 1019]

for tetrad in tetrads:
    print '---', tetrad, '---'
    for f in fifths:
        count = 0
        for t in tetrad:
            conc1 = int(str(f) + str(t))
            conc2 = int(str(t) + str(f))
            if conc1 not in primes or conc2 not in primes:	# not a fifth member
                break
            else:
                count = count + 1
                if count == 4:
                    print tetrad, '<>', f
