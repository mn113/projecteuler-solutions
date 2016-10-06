#! /usr/bin/env python
# Project Euler problem 014: find longest Collatz chain starting under 1 million

def collatz(n):
    chain = 0
    while 1:
        print n,
        chain += 1
        if n == 1:
            break
        elif n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    
    return chain
            

longest = 0

for start in range(999999,1,-1):       
    chain = collatz(start)
    print '=>',chain
    if chain > longest:
        longest = chain
        best = start

print '\nLongest:', longest, '(from', best , ')'