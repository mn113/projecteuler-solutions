#! /usr/bin/env python
# Project Euler problem 002: sum all even Fibonacci numbers below 4,000,000

count = 0
a, b = 1, 1

while a < 4000000:
    print a,
    if a % 2 == 0:
        count += a  
    a, b = b, a+b
        
print '\n', count