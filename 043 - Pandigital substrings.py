#!/usr/bin/env python
# encoding: utf-8
"""
043 - Pandigital substrings.py

Created by Jason Sundram on 2009-12-05.

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d_(1) be the 1^(st) digit, d_(2) be the 2^(nd) digit, and so on. In this way, we note the following:

    * d_(2)d_(3)d_(4)=406 is divisible by 2
    * d_(3)d_(4)d_(5)=063 is divisible by 3
    * d_(4)d_(5)d_(6)=635 is divisible by 5
    * d_(5)d_(6)d_(7)=357 is divisible by 7
    * d_(6)d_(7)d_(8)=572 is divisible by 11
    * d_(7)d_(8)d_(9)=728 is divisible by 13
    * d_(8)d_(9)d_(10)=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.

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

def permutations(str):
    if len(str) <=1:
        yield str
    else:
        for perm in permutations(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

pairs = zip(range(1,8), primes_upto(18))
def check(s):
    # Not pandigital if has a leading 0
    if s[0] == '0': return False 
    for (i, n) in pairs:
        if int(s[i:i+3]) % n != 0:
            return False
    return True
        
@timed
def original_solution():
    return sum([int(s) for s in permutations('0123456789') if check(s)])


def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()

