#! /usr/bin/env python
# Project Euler problem 012: find the first triangular number with over 500 factors

def factorise(n):
    factors = []
    for x in xrange(1,n):
        if x**2 > n:
            break
        if n % x == 0:
            factors.append(x)
    
    return factors


# Build list of triangular numbers
i, t = 1, 1
triangulars = []
while t < 100000000:
    triangulars.append(t)
    flist = factorise(t)
    n = 2*len(flist)
    print t,n
    if n > 500:
        break
    i += 1
    t += i
    
#print triangulars

#checks = [300,301,302,303,304,305]
#for check in checks:
    
#    flist = factorise(triangulars[check])
#    print 'Term', check,'(', triangulars[check], ') has', 2*len(flist), 'factors:', flist