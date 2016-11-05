#! /usr/bin/env python
# Project Euler problem 089: find minimal form of Roman numerals
#    M = 1000
#    D = 500
#    C = 100
#    L = 50
#    X = 10
#    V = 5
#    I = 1

rr2d = {'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9, 'IV':4}
r2d  = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
d2r  = dict([(v, k) for (k, v) in dict(rr2d.items() + r2d.items()).iteritems()])

print [(k,d2r[k]) for k in sorted(d2r.iterkeys(), reverse=True)]


def read_roman(s):
    vals = []
    tot = 0
    for c in str(s).upper():
        if c in r2d:
            vals.append(r2d[c])
    for i in range(len(vals)):
        # look for char pairs:
        if i < len(vals) - 1 and vals[i+1] > vals[i]:
            tot -= vals[i]
        # process single char:
        else:
            tot += vals[i]
    return tot


def make_roman(n):
    out = ''
    while n > 0:
        for d in sorted(d2r.iterkeys(), reverse=True): # won't find multiple instances
            while n >= d:
                n = n - d
                out += d2r[d]
    return out


# process input:
saving = 0
for line in open('euler089_roman.txt'):
    line = ''.join(line.split())
    a = len(line)
    print '  ', line, a
    cleaned = make_roman(read_roman(line))
    b = len(cleaned)
    print '=>', cleaned, b
    saving += (a - b)
    
print saving, 'chars saved'