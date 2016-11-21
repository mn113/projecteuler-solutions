#! /usr/bin/env python
# Project Euler problem 092: how many numbers < 10million cycle to 89 instead of 1?


def sqadd(n):
    r = 0
    for c in str(n):
        r += int(c)**2
    return r
    

def minperm(j):
    sl = sorted(str(j)) # change int to char list
    v = ''.join(sl)
    return int(v)


if minperm(53927) != 23579:
    print minperm(53927)
    exit()


oners, eightyniners = set([1]), set([89]) # known chains
count1, count89 = 0, 0

for i in range(1,10000000):
    j = i
#    print j, ':'
    curchain = []
    while j not in (oners | eightyniners):
#        print j, '->', minperm(j)
        j = sqadd(j)
        j = minperm(j)    # 123 is equivalent to 321 so always test minimum permutation
        curchain.append(j)

    if j in oners:
        oners.update(curchain)
#        print 'oners', oners
        count1 += 1
    else:
        eightyniners.update(curchain)
#        print 'eightyniners', eightyniners
        count89 += 1

print oners
print count1, count89
