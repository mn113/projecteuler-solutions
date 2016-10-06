#! /usr/bin/env python
# Project Euler problem 004: find largest palindromic product of two 3-digit numbers

import math

count = 0
largest = 0

def is_palindrome(n):
    # Test for non-palindromicity:
    for ax in range(0, int(math.ceil(len(n)/2))):
        zx = (-1*ax) - 1
        if n[ax] != n[zx]:
            palindrome = False
            break
    else:
        palindrome = True
        
    return palindrome


for i in range(100, 1000, 1):
    for j in range(100, 1000, 1):
        count += 1
        palindrome = True
        p = str(i*j)
        print i, '*', j, '=', p
        if is_palindrome(p):
            print p, 'is a palindrome'
            if int(p) > largest:
                largest = int(p)
                print largest

print 'Numbers evaluated:', count        
print 'Largest palindrome:', largest

