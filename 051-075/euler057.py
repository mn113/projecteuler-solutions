#! /usr/bin/env python
# Project Euler problem 057: expansion of sqrt(2), counting the top-heavy terms

# Formula:
#sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + 1/2)))
#
#start with 2
#loop: inverse it, add 2

import math

# Standard way:
x = 2.0
for i in range(10):
    x = 1 / x
    x = x + 2
    print x - 1

print math.sqrt(2), 'really\n'


# Sticking to fractions:
x = (2,1)
count = 0
for i in range(1000):
    top, bot = x[1], x[0]
    top = top + bot
    # Reassign for next iteration:
    x = (top + bot, bot)
    print top, '/', bot
    # Test for top-heavy fraction:
    if len(str(top)) > len(str(bot)):
        count = count + 1

print count
