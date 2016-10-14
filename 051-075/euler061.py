#! /usr/bin/env python
# Project Euler problem 061: find 6 cyclic 4-digit numbers which are 3,4,5,6,7,8-gonal

from itertools import permutations

tri, square, penta, hexa, hepta, octa = [''], [''], [''], [''], [''], ['']

n = 1
while 1:
    t = n*(n+1)/2
    if t >= 10000:
        break
    if t > 999:
        tri.append(str(t))
    n = n + 1    

n = 1
while 1:
    s = n*n
    if s >= 10000:
        break
    if s > 999:
        square.append(str(s))
    n = n + 1    
        
n = 1
while 1:
    p = n*((3*n)-1)/2
    if p >= 10000:
        break
    if p > 999:
        penta.append(str(p))
    n = n + 1    
        
n = 1
while 1:
    h = n*((2*n)-1)
    if h >= 10000:
        break
    if h > 999:
        hexa.append(str(h))
    n = n + 1    
        
n = 1
while 1:
    h = n*((5*n)-3)/2
    if h >= 10000:
        break
    if h > 999:
        hepta.append(str(h))
    n = n + 1    
        
n = 1
while 1:
    o = n*((3*n)-2)
    if o >= 10000:
        break
    if o > 999:
        octa.append(str(o))
    n = n + 1    


series_x6 = [tri,square,penta,hexa,hepta,octa]

for s in series_x6:
    s.remove('')
    print s, len(s)

series_x5 = [tri,square,penta,hexa,hepta]

    
for o in octa:
    # Assume it's 2 digits which bridge across:
    if o[2] == '0': # we don't want a zero here
        continue

    # Try each of 120 routes in turn:
    for route in permutations('01234'):
        s1 = series_x5[int(route[0])]
        for a in s1:
            if o[2:] == a[:2]:
                # Narrow series options:
                s2 = series_x5[int(route[1])]
                for b in s2:
                    if a[2:] == b[:2]:
                        # Narrow series options:
                        s3 = series_x5[int(route[2])]
                        for c in s3:
                            if b[2:] == c[:2]:
                                # Narrow series options:
                                s4 = series_x5[int(route[3])]
                                for d in s4:
                                    if c[2:] == d[:2]:
                                        # Narrow series options:
                                        s5 = series_x5[int(route[4])]
                                        for e in s5:
                                            if d[2:] == e[:2]:
                                                if e[2:] == o[:2]:    # cycle complete :)
                                                    print o, a, b, c, d, e
                                                    print sum([int(x) for x in [o,a,b,c,d,e]])
