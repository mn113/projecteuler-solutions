#! /usr/bin/env python
# Project Euler problem 043: find pandigital numbers with prime-divisible strings

import time


def has_dupe_digits(n):
    # convert to set, check size
    if len(set(str(n))) == len(str(n)):
        return False
    else:
        return True


def is_pandigital(z,n):
    # concatenate strings
    if len(set(n)) == z:
        return True
    else:
        return False


def find_overlaps(str1, str2):
    # str 1 is the little endianest
    out = []
    for s1 in str1:
        for s2 in str2:
            if s1[:2] == s2[-2:]:
                # we have an overlap of 2; glue it
                o = s2[:-2] + s1
                if not has_dupe_digits(o):
                    out.append(o)
    return out


start = time.clock()

# build it from the back!
stringbook = {}
for x in [17,13,11,7,5,3,2]:
    stringbook[x] = list()

for x in stringbook:
    for i in range(1, 1000/x):
        prod = str(i * x).zfill(3)
        if int(prod) < 1000 and not has_dupe_digits(prod):
            stringbook[x].append(prod)        


# now try to concatenate overlapping strings together:
conc_str = find_overlaps(stringbook[17], stringbook[13])
conc_str = find_overlaps(conc_str, stringbook[11])
conc_str = find_overlaps(conc_str, stringbook[7])
conc_str = find_overlaps(conc_str, stringbook[5])
conc_str = find_overlaps(conc_str, stringbook[3])
conc_str = find_overlaps(conc_str, stringbook[2])


# we got the last 9 digits, now add the missing first digit:
collection = []
for s in conc_str:
    for i in range(1,10):
        if is_pandigital(10,`i`+s):
            collection.append(int(`i`+s))
            break

print collection

# and sum them:
tally = 0
for x in collection:
    tally += x
print tally

print time.clock() - start