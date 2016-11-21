#! /usr/bin/env python
# Project Euler problem 099: greatest power in file?

import math

# Logarithms: log(a^b) == b*log(a)

maxi = 0
lino = 0

for line in open('euler099_base_exp.txt'):
    lino += 1    # count line number
    (base, exp) = line.split(',')

    # to integers:
    base, exp = int(base), int(exp)

    # log it:
    log = exp * math.log(base)
    
    if log > maxi:
        maxi = log
        maxlino = lino
        
print maxi, 'greatest (line ', maxlino , ')'
