#! /usr/bin/env python
# Project Euler problem 017: how many letters to write numbers 1-1000?

onewords = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teenwords = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tenwords = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

count = 0

tens = huns = thous = False

for i in range(1,1001):
    words = []
    num = str(i)
    print num, ':',

    # Split up digits:
    ones = int(num[-1])
    if len(num) >= 2: tens = int(num[-2])
    if len(num) >= 3: huns = int(num[-3])
    if len(num) >= 4: thous = int(num[-4])

    # Build words:    
    if thous:
        words.append(onewords[thous]) 
        words.append('thousand') 
        print onewords[thous], 'thousand',
    if huns:    
        words.append(onewords[huns]) 
        words.append('hundred') 
        print onewords[huns], 'hundred',
    if huns and (tens or ones):    
        words.append('and')
        print 'and',

    if tens == 1:
        # Special case:
        words.append(teenwords[ones])
        print teenwords[ones], '=>', len(''.join(words)) 
    elif tens:
        words.append(tenwords[tens]) 
        words.append(onewords[ones])
        print tenwords[tens],
        print onewords[ones], '=>', len(''.join(words)) 
    else:
        words.append(onewords[ones])
        print onewords[ones], '=>', len(''.join(words)) 

    # Count letters:
    count += len(''.join(words))

print count

#21124 correct