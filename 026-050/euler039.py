#! /usr/bin/env python
# Project Euler problem 039: what value of triangle perimeter p <= 1000 gives most solutions for side lengths?

highscore = 0
champion = False

limit = 1000

# build lookup-table of squares:
sq = {}
for i in range(1,1+(limit/2)):
    sq[i] = i**2

# start by setting the perimeter:
for p in range(2,limit+1,2):
    # count the solutions for each p:
    count = 0
    for a in range(1, 1+(limit/2)):
        for b in range(1, 1+(limit/2)):
            # avoid dupes by keeping strict size ordering:
            if a > b:
                continue
            # now find c:
            c = p - a - b
            if c <= 0 or c > limit/2:
                continue            
            # get squares from lookup table:
            if sq[a] + sq[b] == sq[c]:
                # valid solution found!
                print a,b,c, '>', p
                count += 1
                if count > highscore:
                    highscore = count
                    champion = p

print highscore, 'solutions for perimeter', champion	# runs in 59 seconds!