#! /usr/bin/env python
# Project Euler problem 030: all numbers whose digits, to power 5, summed, equal them

lim = 360000
total = 0

for i in range(2,lim):
    score = 0
    for c in str(i):
        score += int(c)**5
    if score == i:
        print i
        total += score
        
print 'Total:', total