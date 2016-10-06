#! /usr/bin/env python
# Project Euler problem 022: sum alphanumeric values of names file


def sum_word(w):
    sum = 0
    for l in w.upper():
        sum += ord(l) - 64 # ASCII offset
    return sum


# Read in the file:
f = open('022.in')
names = f.readlines()

namelist = names[0].split(',')
#print namelist

total = 0
i = 1

# Sort and sum the list:
for n in sorted(namelist):
    total += i * sum_word(n[1:-1])
    i += 1
    
print total

# 1 LINDA		= 40
# 2 MARY		= 57	= 114
# 3 PATRICIA	= 77	= 231		= 385


