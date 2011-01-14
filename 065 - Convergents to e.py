#!/usr/bin/env python
# encoding: utf-8
"""
065 - Convergents to e.py

Created by Jason Sundram on 2010-02-26.
Copyright (c) 2010. All rights reserved.

Problem 65
12 March 2004

What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""
from timed import timed
from utils import convergents
from math import ceil

def e_expansion(n):
    """Get at least n digits of the fractional expansion of e."""
    A = [2]
    
    m = int(ceil(n / 3.0))
    for x in range(m): 
        A.extend([1, 2*(x+1), 1])
    
    return A

@timed
def original_solution():
    c = convergents(e_expansion(100), 99) # there's an off-by-one thing going on in convergents, I think
    p, q = c[-1] # numerator, denominator of last term
    
    return sum(map(int, str(p)))


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

