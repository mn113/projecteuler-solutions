#! /usr/bin/env python
# Project Euler problem 023: sum all integers not the sum of 2 abundant numbers

# Cannot be written as ab1 + ab2:
# 1-23
# All odd numbers
# 26, 28, 34, 46


def sum_list(lst):
    c = 0
    for i in lst:
        c += i
    return c


def divisors(n):
    d = []
    for i in range(1,(n/2)+1):
        if n%i == 0:
            d.append(i)
    return d
    

lim = 28124	# gives 6965 abundants
#lim = 2000	# gives 492 abundants
#lim = 200	# gives 45 abundants

# Build a list of abundant numbers
abundant = []
for x in range(1,lim):
    if sum_list(divisors(x)) > x:
        abundant.append(x)

#print abundant
print len(abundant), 'abundants' # ok


# Adding square:
abundant2 = abundant[:]
ab_sums = set()

for a1 in abundant:
    for a2 in abundant2:
        if a2 < a1:
            continue
        elif a1 + a2 > lim:
            continue
        else:
            ab_sums.add(a1 + a2)

#print sorted(ab_sums)
print len(ab_sums), 'sums'

# Remove sums from evens to give desired numbers:
hunted = set(range(1,lim)) - ab_sums
#print sorted(hunted)

print sum(list(hunted))