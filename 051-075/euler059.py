#! /usr/bin/env python
# Project Euler problem 059: decrypt an ASCII string using a three-letter KeyboardInterrupt

import string
from random import randrange


def text_to_ints(text):
    return [ord(ch) for ch in text]


def ints_to_text(ints):
    return ''.join([chr(i) for i in ints])
    

def xor(n1, n2):	# XORs all members of 2 integer lists
    o = []
    for i in range(len(n1)):
        o.append(n1[i] ^ n2[i]) # XOR operation
    return o


# Memo:
print ord('A'), '=', chr(65) # 65 = A
print 6 ^ 10   # 12
print 26**3, 'possible keys'


# Tests
#plaintext    = "Python is my fave language"		# str
#plain_ints   = text_to_ints(plaintext)				# list
#key          = 'abc'
#lkey         = key * ((len(plaintext) / 3) + 1)	# str
#lkey_ints    = text_to_ints(lkey)					# list
#ciphertext   = xor(plain_ints, lkey_ints)			# list
#decoded_ints = xor(ciphertext, lkey_ints)			# list
#decoded_text = ints_to_text(decoded_ints)			# str
#print plaintext
#print plain_ints
#print lkey
#print lkey_ints
#print ciphertext
#print decoded_ints
#print decoded_text


# our ciphertext is comma-separated integers as strings
# import:
for line in open('euler059_cipher1.txt'):
    words = line.split(',')
    ciphertext = [int(w) for w in words]
#print ciphertext
print 'Decoding...'

letterpairs = ['th','he','an','re','er','in','on','at','nd','st']
trigrams    = ['the','and','tha','ent','ing','ion','tio','for','nde','has','nce','edt','tis','oft','sth','men']


# Iterate thru possible keys and try decryption:
lower = string.ascii_lowercase
for i in lower:
    for j in lower:
        for k in lower:
            testkey = ''.join([i,j,k])
            
            lkey         = testkey * ((len(ciphertext) / 3) + 1)
            lkey_ints    = text_to_ints(lkey)
            decoded_ints = xor(ciphertext, lkey_ints)
            decoded_text = ints_to_text(decoded_ints)
            # Frequency analysis: look for 3 English letter pairs:
            pcount = 0
            for p in trigrams:
                if p in decoded_text:
                    pcount = pcount + 1
                    if pcount > 4:
                        print '---', testkey, '---', decoded_text
                        break

thekey = 'god'
lkey         = thekey * ((len(ciphertext) / 3) + 1)
lkey_ints    = text_to_ints(lkey)
decoded_ints = xor(ciphertext, lkey_ints)
total = sum(decoded_ints)
print total