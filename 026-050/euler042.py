#! /usr/bin/env python
# Project Euler problem 042: sum alphanumeric values of words, find which are triangular

trinums = []
for n in range(1,25):
    trinums.append(int(0.5*n*(n+1)))
    
count = 0

for line in open('042words.txt'):
    words = line.split(',')
    for w in words:
        score = 0
        for l in w[1:-1]:
            score += ord(l) - 64
        if score in trinums:
            print w, score
            count += 1

print count