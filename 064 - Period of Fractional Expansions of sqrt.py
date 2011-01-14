#!/usr/bin/env python
# encoding: utf-8
"""
064 - Period of Fractional Expansions of sqrt.py

Created by Jason Sundram on 2010-01-05.
Copyright (c) 2010. All rights reserved.

Problem 64
27 February 2004

All square roots are periodic when written as continued fractions and can be written in the form:

# Hard to represent, see http://projecteuler.net/index.php?section=problems&id=64

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?

"""
from timed import timed
from utils import root_expansion as expand

@timed
def original_solution():
    """runtime on mbp: 3103 ms"""
    def odd_expansion(n): 
        i = len(expand(n))-1
        return 0 < i and i % 2 == 1
    
    N = 10*1000 # 13 -> 4
    
    return len(filter(odd_expansion, xrange(1, N+1)))


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

