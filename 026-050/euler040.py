#! /usr/bin/env python
# Project Euler problem 040: furthest digits of decimal 0.123456789101112131415161718192021...

s = ''
for i in range(1,190000):
    s += `i`
    
print len(s), 'digits'
print s[0]
print s[9]
print s[99]
print s[999]
print s[9999]
print s[99999]
print s[999999]

