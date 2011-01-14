#!/usr/bin/env python
# encoding: utf-8
"""
062 - Cube Permutations.py

Created by Jason Sundram on 2010-01-05.
Copyright (c) 2010. All rights reserved.

Problem 62
30 January 2004

The cube, 41063625 (345^(3)), can be permuted to produce two other cubes: 56623104 (384^(3)) and 66430125 (405^(3)). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""
from timed import timed
from collections import defaultdict

@timed
def original_solution():
    """runtime: 361ms on mbp"""
    N = 5
    LIMIT = 10 ** N # just a guess
    
    cube = lambda x : x**3
    order = lambda x : ''.join(sorted(str(x)))
    
    d = defaultdict(list)
    for c in map(cube, xrange(LIMIT)):
        s = order(c)
        d[s].append(c)
        if len(d[s]) == N:
            return d[s][0] # TODO: show that there are ONLY 5 cubes in this permutation group.
    
    return -1


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

