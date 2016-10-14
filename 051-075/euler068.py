#! /usr/bin/env python
# Project Euler problem 064: magic pentagon solutions of 16 or 17 digits -> longest string?

# a + b + h = tot
# b + c + i = tot
# c + d + j = tot
# d + e + f = tot
# e + a + g = tot

# assume: 13 <= tot <= 20


def discard(somelist, unwanted):
    return [n for n in somelist if n != unwanted]

answers = []

# solve the equations by brute force:
for tot in range(13,20):
    print "\n--- ", tot, "---\n"
    values10 = [1,2,3,4,5,6,7,8,9,10]

    # fill the inner 5 spaces:
    for v in values10:
        values9 = discard(values10, v)
        a = v

        for w in values9:
            values8 = discard(values9, w)
            b = w
            h = tot - a - b
            if h not in values8: continue
            values7 = discard(values8, h)

            for x in values7:
                values6 = discard(values7, x)
                c = x
                i = tot - b - c
                if i not in values6: continue
                values5 = discard(values6, i)

                for y in values5:
                    values4 = discard(values5, y)
                    d = y
                    j = tot - c - d
                    if j not in values4: continue
                    values3 = discard(values4, j)

                    for z in values3:
                        values2 = discard(values3, z)
                        e = z
                        f = tot - d - e
                        g = tot - e - a
                        
                        solution = [a,b,c,d,e,f,g,h,i,j]
                        # see if remaining values match solution:
                        if f not in values2 or g not in values2: continue
                        if sorted(solution) == values10:
                            print tot, solution, 'solution!'

                            # stringify & produce result string:
                            [sa,sb,sc,sd,se,sf,sg,sh,si,sj] = map(str, [a,b,c,d,e,f,g,h,i,j])
                            # find starting index:
                            outernums = [h,g,f,j,i]
                            loidx = outernums.index(min(outernums))
                            strs = [0,0,0,0,0,0,0,0,0,0]
                            strs[0] = ''.join([sh,sb,sa])
                            strs[1] = ''.join([sg,sa,se]) 
                            strs[2] = ''.join([sf,se,sd])
                            strs[3] = ''.join([sj,sd,sc])
                            strs[4] = ''.join([si,sc,sb])
                            strs[5] = strs[0]
                            strs[6] = strs[1]
                            strs[7] = strs[2]
                            strs[8] = strs[3]
                            strs[9] = strs[4]
                            answers.append((strs[loidx], strs[loidx+1], strs[loidx+2], strs[loidx+3], strs[loidx+4], h+b+a))

print "\n"
for t in set(answers):
    # join tuple:
    print t[5], ' '.join([t[0], t[1], t[2], t[3], t[4]])