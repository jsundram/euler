#!/usr/bin/env python
# encoding: utf-8
"""
040 - Nth Digit of Irrational Number.py

Created by Jason Sundram on 2009-12-04.

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12^(th) digit of the fractional part is 1.

If d_(n) represents the n^(th) digit of the fractional part, find the value of the following expression.

d_(1) × d_(10) × d_(100) × d_(1000) × d_(10000) × d_(100000) × d_(1000000)
"""
from timed import timed # helper for timing.
import operator

@timed
def original_solution():
    d = ''.join(map(str, xrange(1000001)))
    get = lambda n: int(d[n])
    ds = map(get, [10**i for i in range(7)])
    return reduce(operator.mul, ds)


def main():
    print 'The answer (original) is: %d' % original_solution()

if __name__ == '__main__':
    main()

