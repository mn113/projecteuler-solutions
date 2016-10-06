#! /usr/bin/env python
# Project Euler problem 021: sum of all amicable numbers below 10000

# divisors of 220 are: 1,2,4,5,10,11,20,22,44,55,110 => sum = 284
# divisors of 284 are: 1,2,4,71,142 => sum = 220

# 220 and 284 are amicable and go in the count


def sum_list(lst):
    c = 0
    for i in lst:
        c += i
    return c


def divisors(n):
    d = []
    for i in range(1,n):
        if n%i == 0:
            d.append(i)
    return d
    

lim = 10000

# Build an array of sums of divisors:
divsums = {}
for x in range(1,lim):
    divsums[x] = sum_list(divisors(x))

divsums[0] = 0	# Special case needed to avoid lookup errors
print divsums, '\n'

# Test against each other:
count = 0
for d in sorted(divsums):
    b = divsums[d]
    if b < lim and d == divsums[b] and d != b:
        print d,
        count += d
        
print '\n\n', count