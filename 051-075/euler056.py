#! /usr/bin/env python
# Project Euler problem 056: find maximum sum of digits for a^b with a,b < 100


def sum_digits(n):
    s = 0
    # sum the digits keeping int type, using modulo and division by 10:
    while n > 0:
        d = n % 10 # last digit
        s += d
        n = (n - d)/10
    return s


max_sum = 0

for a in range(1,100):
    e = 1
    for b in range(1,100):
        e *= a
        s = sum_digits(e)
        if s > max_sum:
            max_sum = s
            
print max_sum