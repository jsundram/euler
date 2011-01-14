#!/usr/bin/env python
# encoding: utf-8
"""
038 - Pandigital products.py

Created by Jason Sundram on 2009-12-04.

Problem 38
28 February 2003

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

from timed import timed # helper for timing.


def cat_product(i, n):
    products = map(lambda x: str(i*x), range(1, n+1))
    return ''.join(products)

def is_pandigital(s):
    return len(s) == 9 and set(s) == set('123456789')
    
@timed
def original_solution():
    """Establish limits for n and i by common sense."""
    m = 0
    for n in range(1, 10):
        for i in xrange(1, 9999):
            s = cat_product(i, n)
            if m < int(s) and is_pandigital(s):
                print "i = %d, n = %d => %s" % (i, n, s)
                m = int(s)
    return m


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

