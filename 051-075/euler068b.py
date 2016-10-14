#! /usr/bin/env python
# Project Euler problem 064: magic 3-gon solutions of 16 or 17 digits -> longest string?

# a + b + f = tot
# b + c + d = tot
# c + a + e = tot






def discard(somelist, unwanted):
    return [n for n in somelist if n != unwanted]

answers = []

# solve the equations by brute force:
for tot in range(9,13):
    print "\n--- ", tot, "---\n"
    values6 = [1,2,3,4,5,6]

    # fill the inner 3 spaces:
    for v in values6:
        values5 = discard(values6, v)
        a = v

        for w in values5:
            values4 = discard(values5, w)
            b = w
            f = tot - a - b
            if f not in values4: continue
            values3 = discard(values4, f)

            for x in values3:
                values2 = discard(values3, x)
                c = x
                d = tot - b - c
                e = tot - c - a
                        
                solution = [a,b,c,d,e,f]
                # see if remaining values match solution:
                if d not in values2 or e not in values2: continue
                if sorted(solution) == values6:
                    print tot, solution, 'solution!'

                    # stringify & produce result string:
                    [sa,sb,sc,sd,se,sf] = map(str, [a,b,c,d,e,f])
                    # find starting index:
                    outernums = [f,e,d]
                    loidx = outernums.index(min(outernums))
                    strs = [0,0,0,0,0,0]
                    strs[0] = ''.join([sf,sb,sa])
                    strs[1] = ''.join([se,sa,sc]) 
                    strs[2] = ''.join([sd,sc,sb])
                    strs[3] = strs[0]
                    strs[4] = strs[1]
                    strs[5] = strs[2]
                    answers.append((strs[loidx], strs[loidx+1], strs[loidx+2], f+b+a))

print "\n"
for t in set(answers):
    # join tuple:
    print t[3], ' '.join([t[0], t[1], t[2]])