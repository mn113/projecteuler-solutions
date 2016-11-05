#! /usr/bin/env python
# Project Euler problem 079: shortest passcode from 50 login characters?

# break 3-ples down into 2-ples
# if (a,b) but no (b,a), we know something

trios = []
duos = []
counts = dict.fromkeys(range(10), 0)

# import list:
for line in open('euler079_keylog.txt'):
    trios.append(line.strip())

# break trios into duos:
for t in trios:
    duos.append(t[0]+t[1])
    duos.append(t[1]+t[2])
    duos.append(t[0]+t[2])

# extract useful info:
duos = set(duos)
for i in range(10):
    for d in duos:
        if d[0] == str(i):
            # log every time this char is first in a duo:
            counts[i] += 1

# sort:
for key, value in sorted(counts.iteritems(), reverse=True, key=lambda(k,v): (v,k)):
    print key, 'leads', value, 'times'