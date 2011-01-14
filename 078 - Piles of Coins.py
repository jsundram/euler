#!/usr/bin/env python
# encoding: utf-8
"""
078 - Piles of Coins.py

Created by Jason Sundram on 2010-08-11.
Copyright (c) 2010. All rights reserved.

Problem 78
10 September 2004

Let p(n) represent the number of different ways in which n coins can be separated into piles. 
For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""
from timed import timed
#import psyco; psyco.full()

@timed
def original_solution():
    """ original_solution took 9729.187 ms. The answer (original) is: 55374
        with psyco, 860.079 ms.
        adapted from http://blog.dreamshire.com/2009/04/19/project-euler-problem-78-solution/
        also http://oeis.org/classic/A000041
    """
    # generate and cache pentagonal numbers
    k = []
    for i in xrange(1, 250): 
        p = i * (3 * i - 1) / 2
        k.extend([p, p + i])
    
    n = 0
    P = [1]
    sign = [1,1,-1,-1]
    # Calculate p(n) by expanding generating function
    while P[n] != 0:
        p, i = 0, 0
        n += 1
        while k[i] <= n:
            #sign = -1 if i % 4 > 1 else 1
            p += sign[i % 4] * P[n - k[i]]
            i += 1
        #print "p(%d) = %d" % (n, p)
        P.append(p % 1e6)
    return n
    

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

