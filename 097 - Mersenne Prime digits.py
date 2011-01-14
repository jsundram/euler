#!/usr/bin/env python
# encoding: utf-8
"""
097 - Mersenne Prime digits.py

Created by Jason Sundram on 2010-08-07.
Copyright (c) 2010. All rights reserved.

Problem 97
10 June 2005

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 269725931; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433*2**7830457 + 1.

Find the last ten digits of this prime number.


Answer:
8739992577
"""
from timed import timed

@timed
def original_solution():
    """8739992577"""
    return int(str(28433 * 2**7830457 + 1)[-10:]) # python is awesome


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

