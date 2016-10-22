#! /usr/bin/env python
# Project Euler problem 031: number of combinations to make 2 quid

coins = {200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}

tot = 0

def build_trie(trie):
    global tot
    for k,v in trie.iteritems():
        # Add to running total:
        v += k
        #print 'node/tot:', k, v
        # Check for terminator:
        if k <= 0:
            break
        elif v == 200:
            # Add success terminator:
            #print 'end'
            k = 0
            # Count the terminator towards final answer:
            tot = tot + 1
        elif v > 200:
            # Add failure terminator:
            k = -1
        else:
            # Add branch, but not heavier than parent:
            k = dict((c,v) for c,t in coins.iteritems() if c <= k)
            #print 'adding branch',
            #print k
            if len(k) > 0:
                # Go deeper:
                build_trie(k)
    return tot
            

# Build additive trie:
trie = coins
build_trie(trie)


print tot