#! /usr/bin/env python
# Project Euler problem 029: how many distinct numbers a**b for a,b in 2-100

import time


# list all duplicate cases:

#  4**b == 2**2b
#  8**b == 4**1/5b == 2**3b
#  9**b == 3**2b
# 16**b == 8**4/3b == 4**2b == 2**4b
# 25**b == 5**2b
# 27**b == 9**3/2b == 3**3b
# 32**b == 16**5/4b == 8**5/3b == 4**5/2b == 2**5b
# 36**b == 6**2b
# 49**b == 7**2b
# 64**b == 32**6/5b == 16**6/4b == 8**2b == 4**3b == 2**6b
# 81**b == 27**4/3b == 9**2b == 3**4b
#100**b == 10**2b


lim = 100

print (lim-1)**2, 'terms'

prods = []
count = 0
skipped = 0

time_start = time.time() 

for a in range(lim,1,-1):
    for b in range(lim,1,-1):
        if a == 100 and 2*b <= 100: # because 100**2 == 10**4, 3==6, 4==8, 5==10, 100**25 == 10**50
            skipped += 1
            continue

        elif a == 81 and 2*b <= 100: # 9**2b case
            #print 'CAUGHT DUPE a:', a, b
            skipped += 1
            continue
        elif a == 81 and 4*b <= 100: # 3**4b case
            #print 'CAUGHT DUPE b:', a, b
            skipped += 1
            continue
        elif a == 81 and (4*b/3) <= 100 and (4*b)%3 == 0: # 27**4/3b case
            #print 'CAUGHT DUPE c:', a, b
            skipped += 1
            continue

# 64**b == 32**6/5b == 16**6/4b == 8**2b == 4**3b == 2**6b

        elif a == 64 and 2*b <= 100: # 8**2b case
            #print 'CAUGHT DUPE a:', a, b
            skipped += 1
            continue
        elif a == 64 and 3*b <= 100: # 4**3b case
            #print 'CAUGHT DUPE:b', a, b
            skipped += 1
            continue
        elif a == 64 and 6*b <= 100: # 2**6b case
            #print 'CAUGHT DUPE c:', a, b
            skipped += 1
            continue
        elif a == 64 and (6*b/5) <= 100 and (6*b)%5 == 0: # 32**6/5b case
            #print 'CAUGHT DUPE d:', a, b
            skipped += 1
            continue
        elif a == 64 and (6*b/4) <= 100 and (6*b)%4 == 0: # 16**6/4b case
            #print 'CAUGHT DUPE e:', a, b
            skipped += 1
            continue

        elif a == 49 and 2*b <= 100:
            skipped += 1
            continue
        elif a == 36 and 2*b <= 100:
            skipped += 1
            continue

        elif a == 32 and 5*b <= 100: # 2**5b case
            skipped += 1
            continue
        elif a == 32 and (5*b/2) <= 100 and (5*b)%2 == 0: # 4**5/2b case
            skipped += 1
            continue
        elif a == 32 and (5*b/3) <= 100 and (5*b)%3 == 0: # 8**5/3b case
            skipped += 1
            continue
        elif a == 32 and (5*b/4) <= 100 and (5*b)%4 == 0: # 16**5/4b case
            skipped += 1
            continue

        elif a == 27 and 3*b <= 100: # 3**3b case
            skipped += 1
            continue
        elif a == 27 and (3*b/2) <= 100 and (3*b)%2 == 0: # 9**3/2b case
            skipped += 1
            continue

        elif a == 25 and 2*b <= 100:
            skipped += 1
            continue

        elif a == 16 and 2*b <= 100: # 4**2b case
            skipped += 1
            continue
        elif a == 16 and 4*b <= 100: # 2**4b case
            skipped += 1
            continue
        elif a == 16 and (4*b/3) <= 100 and (4*b)%3 == 0: # 8**4/3b case
            skipped += 1
            continue

        elif a == 9 and 2*b <= 100: # 3**2b case
            skipped += 1
            continue

        elif a == 8 and 3*b <= 100: # 2**3b case
            skipped += 1
            continue
        elif a == 8 and (3*b/2) <= 100 and (3*b)%2 == 0: # 4**3/2b case
            skipped += 1
            continue

        elif a == 4 and 2*b <= 100: # 2**2b case
            skipped += 1
            continue

        else:
            prods.append(a**b)
            count += 1
            
print count, 'distinct terms'
print skipped, 'skipped'
# Incorrect guesses: 9277, 9550
print sorted(prods)[:50]

time_end = time.time() 
print "time taken", time_end-time_start

# Would have been faster just to brute force the list of 10000 and setify:

biglist = []
for a in range(lim,1,-1):
    for b in range(lim,1,-1):
        biglist.append(a**b)
        
time_end2 = time.time()
print "time taken", time_end2-time_end
print 'Brute-forced distinct terms', len(set(biglist))
