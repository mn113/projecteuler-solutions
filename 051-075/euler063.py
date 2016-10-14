#! /usr/bin/env python
# Project Euler problem 063: how many n-digit numers exist which are nth powers?

for n in range(1,25):
    mini = 10**(n-1)
    maxi = 10**(n)
    powers = [a**n for a in range(1,11)]
    print [p for p in powers if p >= mini and p < maxi]
