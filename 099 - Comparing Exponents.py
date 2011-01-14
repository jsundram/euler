#!/usr/bin/env python
# encoding: utf-8
"""
099 - Comparing Exponents.py

Created by Jason Sundram on 2010-08-11.
Copyright (c) 2010. All rights reserved.

Problem 99
01 July 2005

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048  37 = 2187.

However, confirming that 63238^2518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, 
determine which line number has the greatest numerical value.


"""
from timed import timed
from math import log

@timed
def golfed():
    def key(t):
        base, exp = t[1].split(',')
        return int(exp) * log(int(base))
    return max(enumerate(open(__file__.replace('.py', '.txt'))), key=key)[0] + 1
    
@timed
def original_solution():
    """ original_solution took 3.107 ms
        The answer (original) is: 709
    """
    maxV, maxL = 0, 0
    for i, l in enumerate(open(__file__.replace('.py', '.txt'))):
        base, exp = l.split(',')
        v = int(exp) * log(int(base))
        if maxV < v:
            maxV, maxL = (v, i)
    
    return maxL + 1 # 0-based


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

