#! /usr/bin/env python
# Project Euler problem 013: find the first ten digits of 100 summed numbers


f = open('013.in')
# Retrieve lines:
lines = f.readlines()

count = 0

# Iterate over stored lines:
for i in range(len(lines)):
    line = lines[i]
    
    if line:
        n = int(line[0:15])
        print n
        count += n
        
print str(count)[0:10]