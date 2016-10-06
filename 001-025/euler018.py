#! /usr/bin/env python
# Project Euler problem 018: what is the greatest sum route through the pyramid? (not brute-forcing)


# Convert text-file pyramid to dict-structure:
pyr = {}
i = 0
for line in open('067.in'):
    pyr[i] = {}
    words = line.strip().split(' ')
    for w in range(len(words)):
        # Store the number as a nested nested nested dict:
        pyr[i][w] = {'val': int(words[w]), 'tot': 0}
    i += 1

size = i

print pyr

print '\nTraversing:'
# Fix first row total:
pyr[0][0]['tot'] = pyr[0][0]['val']
# Traverse pyramid and insert beside each number the max of its two 'parents'
for tier in pyr:
    if tier > 0:
        for pos in pyr[tier]:
            val = pyr[tier][pos]['val']
            newval = 0
            # Case the-first:
            if pos == 0:
                newval = val + pyr[tier-1][0]['tot']  
            # Case the-last:
            elif pos == tier:
                newval = val + pyr[tier-1][tier-1]['tot']  
            # Central ones:
            else:
                newval = val + max(pyr[tier-1][pos-1]['tot'], pyr[tier-1][pos]['tot'])
            # Write new value back to pyramid:
            pyr[tier][pos]['tot'] = newval
            
print pyr

# Compare last row totals to find max:
total = pyr[size-1][0]['tot']
for i in range(size):
    print pyr[size-1][i]['tot'],
    if pyr[size-1][i]['tot'] > total:
        total = pyr[size-1][i]['tot']

print '\n', total, 'was the maximal route found!'
