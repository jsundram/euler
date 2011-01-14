#!/usr/bin/env python
# encoding: utf-8
"""
098 - Square Anagrams.py

Created by Jason Sundram on 2010-09-21.
Copyright (c) 2010. All rights reserved.

Problem 98
17 June 2005

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 
1296 = 36**2. 
What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 
9216 = 96**2. 

We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, 
neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
containing nearly two-thousand common English words, find all the square anagram word pairs 
(a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""
from collections import defaultdict
import time
from timed import timed
#import psyco; psyco.full()


def get_anagrams(l):
    f = lambda x : ''.join(sorted(x)) # hash the words
    anagrams = defaultdict(list)
    for i in l:
        anagrams[f(i)].append(i)
    return anagrams

def to_pairs(anagrams):
    candidates = []
    for key, wordlist in anagrams.iteritems():
        for i, w1 in enumerate(wordlist):
            for w2 in wordlist[i+1:]:
                candidates.append((w1, w2))
    return candidates

def match(c1, c2, squares):
    # TODO: might be faster to figure out a function to permute c1 to c2, and apply that to each of the squares.
    m = 0
    for s1, s2 in squares:
        d1 = dict(zip(c1, s1))
        if len(set(d1.values())) == len(d1) and map(d1.get, c2) == list(s2):
            m = max(m, int(s2))
        # d2 = dict(zip(c1, s2))
        # if len(set(d2.values())) == len(d2) and map(d2.get, c2) == list(s1):
        #    m = max(m, max(int(s1), int(s2)))
    return m

@timed
def original_solution():
    """ original_solution took 49.690 ms (35.843 ms with psyco)
        738.863 ms (searching squares up to length 9)
        The answer (original) is: 18769
    """
    words = open(__file__.replace('.py', '.txt')).read().replace('"', '').split(',')
    
    anagrams = get_anagrams(words)  # Find anagrams
    candidates = to_pairs(anagrams) # List all pairs
    # longest = len(max(candidates, key=lambda x: len(x[0]))[0]) # figure out how many number pairs we need to generate
    # use the fact that there are only two anagrams with length longer than 7: 
    # via: print dict((i, [s for s in candidates if len(s[0]) == i]) for i in xrange(2, 10))
    # 8 -> [('CREATION', 'REACTION')], 9-> [('INTRODUCE', 'REDUCTION')]}
    # if we don't get the answer with this, we can do the much longer search up to 9
    longest = 9
    
    anagrams = get_anagrams((str(i*i) for i in xrange(4, int((10**longest)**.5)+1)))
    squares = to_pairs(anagrams)
    s_n = dict((i, [s for s in squares if len(s[0]) == i]) for i in xrange(2, 10))
    
    return max(match(c1, c2, s_n[len(c1)]) for c1, c2 in candidates)


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

