#! /usr/bin/env python
# Project Euler problem 051: smallest prime which, by replacing some part, yields 8 primes


def subbits(n, bitmask, digit):
    n = str(n)
    m = ''
    for i in range(len(n)):
        if bitmask[i] == '1':
            m += str(digit)
        else:
            m += n[i]
    return int(m)


# mathematical bitmasking: -- now works
def subbits2(n, bitmask, digit):
    size = len(bitmask)
    m = 0.0
    #print bitmask
    while n > 0:
        # chop last bit off bitmask:
        bit = int(bitmask[-1])
        bitmask = bitmask[:-1]
        # process number little end first:
        u = n % 10
        if (bit == 1):
            m = m + (bit * digit)
        elif (bit == 0):
            m = m + u
        n = n / 10
        m = m / 10
    return int(m * (10**size))


import time

start = time.clock()
for x in range(1000000):
    subbits(33333,'10101',7)
print 'subbits:', time.clock() - start

start = time.clock()
for x in range(1000000):
    subbits2(33333,'10101',7)
print 'subbits2:', time.clock() - start