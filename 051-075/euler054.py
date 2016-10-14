#! /usr/bin/env python
# Project Euler problem 054: comparing poker hands
# high card:		 0 000 000 000 + 14 13 12 11 09
# pair:				20 000 000 000 + 14 14 13 12 10
# two pair:			40 000 000 000 + 14 14 12 12 10
# three:			50 000 000 000 + 14 14 14 12 10
# straight:			60 000 000 000 + 14 13 12 11 10
# flush:			65 000 000 000 + 14 13 11 10 09
# full house:		70 000 000 000 + 14 14 14 12 12
# poker:			80 000 000 000 + 14 14 14 14 10
# straight flush:  125 000 000 000 + 13 12 11 10 08
# royal flush:	   125 000 000 000 + 14 13 12 11 10

picturecards = {'A':'14', 'K':'13', 'Q':'12', 'J':'11', 'T':'10'}
billion = 1000000000

def handval(hand):
    print hand,

    score = 0
    vals, suits, svals = [], [], []
    # split values from suits:
    for c in hand:
        vals.append(c[0])
        suits.append(c[1])

    # convert values to 2-digit numeric strings:
    for i, v in enumerate(vals):
        if v in picturecards.keys():
            vals[i] = picturecards[v]
        else:
            vals[i] = vals[i].zfill(2)

    # order cards desc:
    vals.sort(reverse=True) # 

    # test for flush:
    if len(set(suits)) == 1:
        score += 65 * billion
    
    # test for straight:
    nums = map(int, vals)
    gaps = []
    for i in range(4):
        gaps.append(nums[i] - nums[i+1])
    if set(gaps) == set([1]): # all gaps are 1
        straights.append(hand)
        score += 60 * billion
    
    # test for 4:
    for v in vals:
        if vals.count(v) == 4:
            svals.extend([v,v,v,v])
            vals[:] = [w for w in vals if w != v] # remove matching group
            score += 80 * billion
            pokers.append(hand)
            break
    
    # test for 3:
    for v in vals:
        if vals.count(v) == 3:
            svals.extend([v,v,v])
            vals[:] = [w for w in vals if w != v] # remove matching group
            score += 50 * billion
            break
    
    # test for pairs:
    for v in vals:
        if vals.count(v) == 2:
            svals.extend([v,v])
            vals[:] = [w for w in vals if w != v] # remove matching group
            score += 20 * billion

    # remaining singletons go on end:
    svals.extend([v for v in vals])

    # add decimal string of card values to score:
    score += int(''.join(svals))

    print score
    return score


pa_count = 0
# import:
for line in open('euler054_poker.txt'):
    c = line.split()
    pa = [c[0], c[1], c[2], c[3], c[4]]
    pb = [c[5], c[6], c[7], c[8], c[9]]
    
    if handval(pa) > handval(pb):
        pa_count += 1
        
print pa_count
