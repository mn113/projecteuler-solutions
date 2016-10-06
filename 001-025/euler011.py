#! /usr/bin/env python
# Project Euler problem 011: find greatest product of four-in-a-row in grid


f = open('011.in')
# Retrieve lines:
lines = f.readlines()


# Build matrix:
matrix = {}

# Iterate over stored lines:
for i in range(len(lines)):
    line = lines[i]
    
    if line:
        nums = line.split(' ')
        for j in range(len(nums)):
            matrix[(i,j)] = int(nums[j])
        
print matrix

largest = 0

# Vertical search:
for i in range(20):
    for j in range(17):
        nj = matrix[(i,j)]
        nk = matrix[(i,j+1)]
        nl = matrix[(i,j+2)]
        nm = matrix[(i,j+3)]
        
        prod = nj*nk*nl*nm
        if prod > largest:
            largest = prod
            print '(',i,',',j,')','V=>',prod

# Horizontal search:
for i in range(17):
    for j in range(20):
        nj = matrix[(i,j)]
        nk = matrix[(i+1,j)]
        nl = matrix[(i+2,j)]
        nm = matrix[(i+3,j)]
        
        prod = nj*nk*nl*nm
        if prod > largest:
            largest = prod
            print '(',i,',',j,')','H=>',prod

# Diagonal search:
for i in range(17):
    for j in range(17):
        nj = matrix[(i,j)]
        nk = matrix[(i+1,j+1)]
        nl = matrix[(i+2,j+1)]
        nm = matrix[(i+3,j+1)]
        
        prod = nj*nk*nl*nm
        if prod > largest:
            largest = prod
            print '(',i,',',j,')','D1=>',prod

# Backwards diagonal search:
for i in range(17):
    for j in range(19,2,-1):
        nj = matrix[(i,j)]
        nk = matrix[(i+1,j-1)]
        nl = matrix[(i+2,j-2)]
        nm = matrix[(i+3,j-3)]
        
        prod = nj*nk*nl*nm
        if prod > largest:
            largest = prod
            print '(',i,',',j,')','D2=>',prod
            
print largest