#!/usr/bin/env python
# encoding: utf-8
"""
057 - Root 2.py

Created by Jason Sundram on 2009-12-16.
Copyright (c) 2009. All rights reserved.

Problem 57
21 November 2003

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

"""
from timed import timed
from math import log10 as log

def digits(x):
    return 1 + int(log(x)) # could do len(str(x)) instead and avoid an import
    
@timed
def original_solution():
    """ By algebra, we know that if a given term is expressed as n / d (numerator / denominator),
        Then the next term is (n + d + d) / (n + d)."""
    f = lambda n, d : (n + d + d, n + d)
    (n, d) = (1, 1)
    count = 0
    for i in xrange(1, 1001):
        (n, d) = f(n, d)
        if digits(d) < digits(n):
            count += 1
        # print "%d / %d" % (n, d)
    
    return count


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

