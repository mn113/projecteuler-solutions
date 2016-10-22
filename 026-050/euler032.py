#! /usr/bin/env python
# Project Euler problem 032: pandigital products (a * b = c)

# 2 <= a <= 98
# 1234 <= c <= 9876
all_a = range(2,99)
all_c = range(1234,9877)

desired = []


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


def is_pandigital(a,b,c):
    # concatenate strings
    s = ''.join([`num` for num in [a, b, c]])
    if len(set(s)) == 9:
        return True
    else:
        return False


# start whittling down lists:
all_a = filter(lambda a: not has_dupe_digits(a) and not has_zeros(a), all_a)
all_c = filter(lambda c: not has_dupe_digits(c) and not has_zeros(c), all_c)

print len(all_a), len(all_c)
print all_a

# find valid products:
for c in all_c:
    for a in all_a:
        if c % a == 0:
            b = c/a
            if not has_zeros(b) and is_pandigital(a,b,c):
                print a, '*', b, '=', c
                desired.append(c)
                
# convert to set then sum:
total = 0
desired = set(desired)
for d in desired:
    total += d
print "\nTotal:", total