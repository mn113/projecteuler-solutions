#! /usr/bin/env python
# Project Euler problem 024: millionth lexicographic permutation of 0123456789


# first: 0123456789
# there are 3.6 million up to 10

# 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3,628,800 possibilities

# process:
#n = n - (362880 * a)
#n = n - (40320 * b)
#n = n - (5040 * c)
#n = n - (720 * d)
#n = n - (120 * e)
#n = n - (24 * f)
#n = n - (6 * g)
#n = n - (2 * h)
#n = n - (1 * i)

# 2 * 362880 = 725760, leaving 274240	=> 2
# 6 * 40320  = 241920, leaving 32320	=> 7
# 6 * 5040   = 30240,  leaving 2080		=> 8
# 2 * 720    = 1440,   leaving 640		=> 3
# 5 * 120    = 600,    leaving 40		=> 9
# 1 * 24     = 24,     leaving 16		=> 1
# 2 * 6      = 12,     leaving 4		=> 5
# 2 * 2      = 4,      leaving 0		=> 6

# Find factorials:
factorials = []
x = 1
for v in range(1,10):
    x *= v
    factorials.append(x)

factorials = sorted(factorials, reverse=True)


# Start reducing n to eliminate possibilities
n = 999999 # We want the millionth, so find this many
f = 0
i = 0
indices = []

# Loop for subtracting all factorials
while 1:
    # Loop for subtracting one factorial
    while 1:
        n -= factorials[f]
        i += 1
        if n < 0:
            # Gone too far, add one back
            n += factorials[f]
            i -= 1
            # Store the index
            indices.append(i)
            # Reset the index
            i = 0
            break
    f += 1
    #print n

    if f == 9 or n == 0:
        break
    
print indices

# Put the digits in the right order:
digits = range(10)
for j in indices:
    print digits.pop(j),

# Remaining digits must ascend:
for last in digits:
    print last,
