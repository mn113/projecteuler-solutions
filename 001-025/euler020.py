#! /usr/bin/env python
# Project Euler problem 020: sum the digits in 100!

# Calculate 100!
n = 1
for j in range(1,101):
    n *= j

count = 0

# Stringify:
w = str(n)
# Sum digits:
for i in range(len(w)):
    count += int(w[i])
    
print '\n', count
