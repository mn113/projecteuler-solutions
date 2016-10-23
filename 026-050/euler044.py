#! /usr/bin/env python
# Project Euler problem 044: closest pair of pentagonal numbers with pentagonal sum and difference

def pentagonalise(n):
    return n*((3*n)-1)/2


# build list of pentagonal number sequence:
pents = []
for i in range(1,2500):
    pents.append(pentagonalise(i))
print pents

# make boolean array for pentagonal checks:
pent_bools = {}
print 'Building boolean array...'
for i in range(1,20000000):
    pent_bools[i] = False
for i in pents:
    pent_bools[i] = True

results = []
# loop and analyse:
for p in pents:
    for q in pents:
        # keep strict size order, p < q:
        if p >= q:
            continue
        #if q - p in pents:
        if pent_bools[q - p]:
            print q, '-', p, '= pentagonal'
            #if p + q in pents:
            if pent_bools[p + q]:
                print p, '+', q, '= pentagonal'
                results.append((p,q))
                break
                
print results
