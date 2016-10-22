#! /usr/bin/env python
# Project Euler problem 034: sum of all numbers equal to the sum of the factorial of their digits


def factorial(n):
    prod = 1
    while n > 0:
        prod *= n
        n -= 1
    return prod


def sum_fact_digits(n):
    global facts
    s = 0
    # look up digit's factorial from hash table:
    for d in `n`:
        s += facts[int(d)]
    return s


# store factorial for digits 1-9:
facts = {}
facts[0] = 1
for i in range(1,10):
    facts[i] = factorial(i)

print facts

total = 0

for x in range(1,1000000):
    y = sum_fact_digits(x)
    if x == y and x > 2:
        print x, '=', y
        total += x
        
print total