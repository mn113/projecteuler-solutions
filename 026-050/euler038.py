#! /usr/bin/env python
# Project Euler problem 038: largest pandigital product of x with (1,2,...,n)



def has_zeros(n):
    if '0' in str(n):
        return True
    else:
        return False


def has_dupe_digits(n):
    # convert to set, check size
    if len(set(str(n))) == len(str(n)):
        return False
    else:
        return True


def is_pandigital(n):
    if len(set(str(n))) == 9:
        return True
    else:
        return False


#orig = 192
#n = 3

for n in range(2,10):
    for orig in range(1,10000):

        parts = []
        # do the multiplications
        mults = range(1,n+1)
        for m in mults:
            parts.append(orig * m)

        # concatenate the products
        result = ''.join([`p` for p in parts])
        #print result

        # test
        if not has_zeros(result) and not has_dupe_digits(result) and is_pandigital(result):
            print result, orig, n