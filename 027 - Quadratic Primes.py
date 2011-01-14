#!/usr/bin/env python
# encoding: utf-8
"""
027 - Quadratic Primes.py

Created by Jason Sundram on 2009-11-07.

# http://projecteuler.net/index.php?section=problems&id=27
Euler published the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly 
when n = 41, 41² + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for 
the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum 
number of primes for consecutive values of n, starting with n = 0.

"""

import sys
import os
import math


def is_prime(n):
    """Checks for odd divisors less than sqrt(n)"""
    if n < 2: return False
    elif n == 2: return True
    elif n % 2 == 0: return False
    
    stop = int(math.ceil(math.sqrt(n)))
    for i in xrange(3, stop, 2):
        if n % i == 0:
            return False
    return True
    
def count_primes(a, b):
    """Counts quadratic primes given a and b"""
    
    n = 0
    quad = lambda n : n * n + a * n + b 
    while True:
        x = quad(n)
        if is_prime(x):
            n += 1
        else:
            return n

def main():
    m = 0
    v= (0,0)
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            c = count_primes(a,b)
            if m < c:
                m = c
                v = (a,b)
    print "Max run of primes is: %d, with a = %d, b = %d" % (m, v[0], v[1])
    print "product is: %d" % (v[0] * v[1])


if __name__ == '__main__':
    main()

