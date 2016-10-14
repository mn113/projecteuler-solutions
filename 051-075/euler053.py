#! /usr/bin/env python
# Project Euler problem 053: for n in 1-100, how many nCr values are over 1 million?


def nCr(n,r):
    return factorials[n]/(factorials[r]*factorials[n-r])


# build factorial lookup to assist in combinatoric computations:
factorials = {}
factorials[0] = 1
f = 1
for i in range(1,101):
    f *= i
    factorials[i] = f

print factorials

count = 0

for n in range(1,101):
    for r in range(1,n+1):
        if nCr(n,r) > 1000000:
            count += 1
            
print count, 'greater than 1 million'