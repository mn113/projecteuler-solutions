#! /usr/bin/env python
# Project Euler problem 019: how many Sunday the firsts in 20th Century?

years = range(1901, 2001)
leapyears = []

# Populate leapyears:
for y in years:
    leap = False
    if y % 4 == 0:
        leap = True
        if y % 100 == 0:
            leap = False
            if y % 400 == 0:
                leap = True
    
    if leap:
        leapyears.append(y)

#first day
#-31--28--31--30--31--30--31--31--30--31--30--31
#mon-thu-thu-sun-tue-fri-sun-wed-sat-mon-thu-sat		2
#tue-fri-fri-mon-wed-sat-mon-thu-sun-tue-fri-sun		2
#wed-sat-sat-tue-thu-sun-tue-fri-mon-wed-sat-mon		1
#thu-sun-sun-wed-fri-mon-wed-sat-tue-thu-sun-tue		3
#fri-mon-mon-thu-sat-tue-thu-sun-wed-fri-mon-wed		1
#sat-tue-tue-wed-sun-wed-fri-mon-thu-sat-tue-thu		1
#sun-wed-wed-thu-mon-thu-sat-tue-fri-sun-wed-fri		2

#leap year
#-31--29--31--30--31--30--31--31--30--31--30--31
#mon-thu-fri-mon-wed-sat-mon-thu-sun-tue-fri-sun		2
#tue-fri-sat-tue-thu-sun-tue-fri-mon-wed-sat-mon		1
#wed-sat-sun-wed-fri-mon-wed-sat-tue-thu-sun-tue		2
#thu-sun-mon-thu-sat-tue-thu-sun-wed-fri-mon-wed		2
#fri-mon-tue-fri-sun-wed-fri-mon-thu-sat-tue-thu		1
#sat-tue-wed-sat-mon-thu-sat-tue-fri-sun-wed-fri		1
#sun-wed-thu-sun-tue-fri-sun-wed-sat-mon-thu-sat		3

suns_in_year = [2,2,1,3,1,1,2]
suns_in_leap_year = [2,1,2,2,1,1,3]

sunCount = 0

start = 1 # Tuesday 1 Jan 1901

for y in years:
    if y in leapyears:
        sunCount += suns_in_leap_year[start]
        start = (start + 2) % 7    
    else:
        sunCount += suns_in_year[start]
        start = (start + 1) % 7    
        
print sunCount

# Quick method:
# 100 years = 1200 first days
# split equally between 7 possible days
# sunCount = 1200 / 7
# print sunCount