#!/usr/bin/env python
# encoding: utf-8
"""
037 - Truncatable Primes.py

Created by Jason Sundram on 2009-12-04.

Problem 37
14 February 2003

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""
from timed import timed # helper for timing.



@timed
def get_primes(upper_bound=1000000):
    """constructs a sieve and returns primes"""
    sieve = range(0, upper_bound)
    sieve[1] = 0 # 1 is not prime
    stop = 1 + int(upper_bound**.5)
    for i in xrange(2, stop):
        if sieve[i] != 0:
            # if you are feeling fancy someday, could directly assign 0 to a slice of the sieve.
            for j in xrange(i*i, upper_bound, i): sieve[j] = 0
    return [p for p in sieve if p != 0]

primes = set(get_primes())

def get_truncations(n):
    """Generator. Returns all truncations (L-R and R-L) of n, BUT NOT n."""
    to_int = lambda l: int(''.join(l))
    digits = lambda n: list(str(n))
    
    d = digits(n)
    for i in xrange(1, len(d)):
        yield to_int(d[i:])
        yield to_int(d[:i])

def truncatable(p):
    for t in get_truncations(p):
        if t not in primes: 
            return False
    return True

@timed 
def functional_solution():
    return sum([p for p in primes if truncatable(p) and 10 < p])


@timed
def original_solution():
    truncatable_primes = []
    for p in primes:
        if 10 < p and truncatable(p):
            truncatable_primes.append(p)
    
    print truncatable_primes, len(truncatable_primes)
    return sum(truncatable_primes)



def main():
    print 'The answer (original) is: %d' % original_solution()
    print 'The answer (functional) is: %d' % functional_solution()


if __name__ == '__main__':
    main()

