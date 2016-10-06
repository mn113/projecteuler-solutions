#! /usr/bin/env python
# Project Euler problem 025: first Fibonacci term with 1000 digits

a, b, i = 1, 1, 1

while 1:
    a, b = b, a+b
    i += 1
    if len(str(a)) >= 1000:
        break
        
print a, i