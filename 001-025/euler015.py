#! /usr/bin/env python
# Project Euler problem 015: how many routes through 20x20 grid?

#20 across moves
#20 down moves
#40 moves total

#how many permutations?


# Calculate 40!
m = 1
for i in range(1,41):
    m *= i
    
# Calculate 20!
n = 1
for j in range(1,21):
    n *= j

# nPk = 40!/20!/20!
ans = m/(n**2)
print ans