#!/usr/bin/env python
# encoding: utf-8
"""
063 - Nth Powers of N-digit Numbers.py

Created by Jason Sundram on 2010-01-05.
Copyright (c) 2010. All rights reserved.

Problem 63
13 February 2004

The 5-digit number, 16807=7^(5), is also a fifth power. Similarly, the 9-digit number, 134217728=8^(9), is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
from timed import timed
from itertools import takewhile, count

@timed
def original_solution():
    """runtime on mbp: .667ms. That's right. Less than ONE MILLISECOND!"""
    # Don't want to hard-code an upper limit, but know that as soon as 9**x has fewer digits than x, we can stop.
    powers = list(takewhile(lambda x: x <= len(str(9**x)), count(1)))
    test = lambda i, n : len(str(i**n)) == n
    return len([(i,n) for i in xrange(1,10) for n in powers if test(i,n)])


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

