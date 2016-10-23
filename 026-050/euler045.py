#! /usr/bin/env python
# Project Euler problem 045: a triangular, pentagonal and hexagonal number

# Because every hexagonal number is also triangular, we can ignore the tris

import time

def get_tri(n):
    return n*(n+1)/2
    

def get_pent(n):
    return n*((3*n)-1)/2
    

def get_hexa(n):
    return n*((2*n)-1)


start = time.clock()

lim = 150000

pents = []
hexas = []

# build list of hexagonals:
print 'Generating hexas...',
for i in range(1,lim):
    hexas.append(get_hexa(i))
print len(hexas)

# build list of pentagonals:
print 'Generating pents...',
for i in range(1,lim):
    pents.append(get_pent(i))
print len(pents)

# fastest method of getting common elements:
print set(pents).intersection(set(hexas))

print time.clock() - start, 'sec'
