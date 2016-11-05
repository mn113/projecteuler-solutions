#! /usr/bin/env python
# Project Euler problem 081: find minimal sum traversing 80x80 matrix

from itertools import *


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
total = 0

# Scout ahead within 3x3 box:
#paths = ['AADD', 'ADDA', 'ADAD', 'DAAD', 'DADA', 'DDAA']
paths = list(combinations('AD', 4))
print paths

# Repeat until we hit last square:
while x < mx or y < my:

    # Reset the values for the box to be scouted:
    boxtotal = 0
    boxmin = 5000
    print '@', x, y, matrix[(x,y)]
    # Try every path through the 3x3:
    for path in paths:
        print path
        dx,dy = 0,0
        boxtotal = matrix[(x,y)]
        # Take one step:
        for step in path:

            # Edge cases:
            if x+dx == mx:
                step = 'A'                
            elif y+dy == my:
                step = 'D'

            # Follow step cases:
            if step == 'D':
                dx += 1
            elif step == 'A':
                dy += 1

            # Add new square:
            print dx, dy, matrix[(x+dx,y+dy)]
            boxtotal += matrix[(x+dx,y+dy)]

        print path, boxtotal
        if boxtotal < boxmin:
            boxmin = boxtotal
            boxminpath = path
    
    print 'min:', boxmin, '(', boxminpath, ')'
    
    
    # Move 1 place:
    if boxminpath[0] == 'D':
        x += 1
    elif boxminpath[0] == 'A':
        y += 1
    
    print 'step to (', x, ',', y, ')'
