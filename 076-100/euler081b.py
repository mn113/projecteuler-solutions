#! /usr/bin/env python
# Project Euler problem 081: find minimal sum traversing 80x80 matrix

import itertools


f = open('euler081_mini.txt')
# Retrieve lines:
rows = f.readlines()


# Build matrix:
matrix = {}

# Iterate over stored lines:
for i in range(len(rows)):
    row = rows[i]
    
    if row:
        nums = row.split(',')
        for j in range(len(nums)):
            matrix[(i,j)] = int(nums[j])
        
print matrix


# Navigate a path:
x,y = 0,0
mx,my = 4,4
total = matrix[(x,y)]
print x, y, matrix[(x,y)]

# Repeat until we hit last square:
while x < mx or y < my:

    # Edge cases:
    if x == mx:
        y += 1
    elif y == my:
        x += 1
    # Compare next two options and take smaller:
    elif matrix[(x+1,y)] < matrix[(x,y+1)]:
        x += 1
    else:
        y += 1

    print x, y, matrix[(x,y)]
    total += matrix[(x,y)]

print total

# this method too naive, doesn't find minimal sum