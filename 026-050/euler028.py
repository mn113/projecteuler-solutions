#! /usr/bin/env python
# Project Euler problem 028: sum of diagonals in a 1001x1001 spiral

count = 0
i = 1 # index
v = 1 # initial value
j = 2 # jump

while 1:
    if v > 1001**2:
        break
    # Count the value we're on
    print v,
    count += v
    # Jump to the next value
    v += j
    # Increase jump when we move to a new ring
    if i % 4 == 0:
        j += 2
    # Increment i
    i += 1

print '\n', count
