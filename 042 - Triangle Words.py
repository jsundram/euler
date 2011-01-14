#!/usr/bin/env python
# encoding: utf-8
"""
042 - Triangle Words.py

Created by Jason Sundram on 2009-12-04.
The n^(th) term of the sequence of triangle numbers is given by, t_(n) = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t_(10). 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""

import sys
import os
from timed import timed
import operator

def score(s):
    d = {}
    # words are all uppercase (or could call to upper on s)
    d.update( zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(1,27)))
    lookup = lambda x : d[x]
    return reduce(operator.add, map(lookup, s))


def is_triangular(n):
    """Searches. Could store a list and check for membership."""
    triangle = lambda x : int(.5 * x * (x + 1))
    i = 0; t = 0
    while t < n:
        t = triangle(i)
        
        if t == n:
            return True
        i += 1
    
    return False;


@timed
def original_solution():
    f = open('./042 - Triangle Words.txt', 'r')
    line = ''.join(f.readlines())
    words = map(lambda x:x.strip('"'), line.split(','))
    f.close()
    
    return len([word for word in words if is_triangular(score(word))])


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

