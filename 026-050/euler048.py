#! /usr/bin/env python
# Project Euler problem 048: sum of n**n for 1-1000

import time

start = time.clock()

tally = 0

for i in range(1,1001):
    p = i
    for k in range(1,i):
        p = (p * i) % 10000000000

    #print i, p
    tally += p
    
print tally % 10000000000

print time.clock() - start, 'sec'