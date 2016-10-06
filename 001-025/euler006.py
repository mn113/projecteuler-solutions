#! /usr/bin/env python
# Project Euler problem 006: find difference between sum of squares 1-100 and square of sums

# 2 terms:
#(a + b)**2 == a**2 + 2ab + b**2

# 3 terms:
#(a + b + c)**2 == a**2 + b**2 + c**2 + 2ab + 2ac + 2bc


#  a b c d
#a s . . .
#b . s . .
#c . . s .
#d . . . s


#(square of sum) - (sum of squares) = 2(sum of factorials) = 2(a! + b! + c! + ...)


m, n = 0, 0

for i in range (1, 101):
    m += i
    n += i**2

print m**2 - n