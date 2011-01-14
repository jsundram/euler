#!/usr/bin/env python
# encoding: utf-8
"""
041 - Pandigital Primes.py

Created by Jason Sundram on 2009-12-04.

Problem 41
11 April 2003

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""
from timed import timed

def primes_upto(limit):
    """Returns primes up to limit, via a generator"""
    is_prime = [True] * limit
    for n in xrange(2, limit):
        if is_prime[n]:
           yield n
           for i in range(n*n, limit, n): # start at ``n`` squared
               is_prime[i] = False
               
#taken from number 27
def is_prime(n):
    """Checks for odd divisors less than sqrt(n)"""
    if n < 2: return False
    elif n == 2: return True
    elif n % 2 == 0: return False
    
    stop = int(n**.5) + 1
    for i in xrange(3, stop, 2):
        if n % i == 0:
            return False
    return True


def all_perms(str):
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


@timed
def original_solution():
    pandigits = '123456789'
    for i in range(len(pandigits),1,-1):
        # Skip things that are obviously never going to be prime, e.g. multiples of 9
        if sum(range(i+1)) % 9 == 0: continue
        
        candidates = map(int, all_perms(pandigits[0:i]))
        for c in sorted(candidates, reverse=True):
            if is_prime(c):
                return c


def main():
    print 'The answer (original) is: %d' % original_solution()



if __name__ == '__main__':
    main()

