#!/usr/bin/env python
# encoding: utf-8
"""
048 - Sum of powers.py

Created by Jason Sundram on 2009-12-08.
Copyright (c) 2009. All rights reserved.

Problem 48
18 July 2003

The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.

Find the last ten digits of the series, 1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).

"""
from timed import timed

@timed
def original_solution():
    n = sum(map(lambda x:x**x, xrange(1, 1001)))
    s = str(n)
    return int(s[-10:])
    


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

