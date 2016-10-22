#! /usr/bin/env python
# Project Euler problem 033: find 4 fractions like 49/98 which can be cancelled unorthodoxly

import math

def is_prime(p): # STOP USING THIS LETHARGIC FUNCTION
    """ Returns True if p is prime, False if not. """

    for q in range(2, 1 + int(math.floor(math.sqrt(p)))):
        if p % q == 0:
            return False
    else:
        return True


def are_coprime(a,b):
    # factorise a
    factors = []
    for i in range(2,a+1):
        if a % i == 0:
            factors.append(i)
    # check factors into b
    for f in factors:
        if b % f == 0:
            # common factor found
            return True
    else:
        return False


def have_common_digit(a,b):
    a_digits = set(`a`)
    for d in a_digits:
        if d in set(`b`):
            return True
    else:
        return False
        

# for valid numerators and denominators
valid = []

for i in range(10,100):
    # no trailing zeroes:
    if i % 10 == 0:
        continue
    # no doubles:
    if i % 11 == 0:
        continue
    # no primes:
    if is_prime(i):
        continue
    # if none of the above, we keep it:  
    valid.append(i)

print valid


# Find all simplified (1-digit) fractions:
simplified = []
for i in range(1,10):
    for j in range(1,10):
        sf = (i + 0.0) / j
        if i < j:
            simplified.append(sf)

simp_set = set(simplified)
#print simp_set

count = 0
findings = []

for num in valid:
    for denom in valid[:]:
        # discard top-heavy fractions
        if num >= denom:
            continue
        # discard relatively prime pairs:
        if not are_coprime(num, denom):
            continue
        # discard uncancellable pairs
        if not have_common_digit(num, denom):
            continue

        frac = (num + 0.0)/denom # 0.0 forces floats
        if frac not in simp_set:
            continue
        print num, '/', denom, '=', frac
        count += 1

        # separate the digits:
        n1, n2 = math.floor(num/10.0), num % 10.0
        d1, d2 = math.floor(denom/10.0), denom % 10.0

        # simplify by cancelling a common digit:
        if n2 == d2:
            sfrac = n1/d1
        elif n2 == d1:
            sfrac = n1/d2
        elif n1 == d2:
            sfrac = n2/d1
        elif n1 == d1:
            sfrac = n2/d2

        if frac == sfrac:
            findings.append((num,denom))
            
print len(valid), 'numerators and denominators'
print count, 'possibles found'
print findings

# 49 / 98 = 4/8
# 26 / 65 = 2/5
# 16 / 64 = 1/4
# 19 / 95 = 1/5
