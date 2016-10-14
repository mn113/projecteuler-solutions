#! /usr/bin/env python
# Project Euler problem 055: how many Lychrel numbers under 10000?

import math

count = 0

def is_palindrome(n):
    # Test for non-palindromicity:
    n = str(n)
    for ax in range(0, int(math.ceil(len(n)/2))):
        zx = (-1*ax) - 1
        if n[ax] != n[zx]:
            return False
    else:
        return True


def reverse(n):
    word = str(n)
    pal = ''
    for i in range(len(word)):
        pal += word[-1-i]
    return int(pal)


for n in range(10001):
    i = 0
    while i <= 50:
        n += reverse(n)
        if is_palindrome(n):
            break
        i += 1
    else:
        print n, i
        count += 1
        
print count, 'Lychrel numbers found'