#! /usr/bin/env python
# Project Euler problem 062: smallest cube whose digits permute to make five other cubes?


def toSortedString(n):
    return ''.join(sorted(str(n)))


# build cubes list:
cubes = [i**3 for i in range(1,10000)]

# transform cube ints to char-sorted strings
scubes = []
for c in cubes:
    scubes.append(toSortedString(c))

# count reoccurring cubestrings:
for c in scubes:
    n = scubes.count(c)
    if n > 2:
        print c, n
        # get the original cubes that match the sorted cubestring
        print [d for d in cubes if toSortedString(d) == c]
        scubes.remove(c)
    if n == 5:
        break
