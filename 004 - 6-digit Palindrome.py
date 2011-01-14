# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is:
#   9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

### Bounds: 317**2 > 100,000 999x999 = 998,001
def factor(K):
    factors = []
    for i in xrange(2, math.floor(math.sqrt(K))):        
        if (K % i == 0):
            factors.append(i)
            factors.append(K / i)
    factors.sort()
    return factors

def isPalindrome(s):
    if (len(s) != 6):
        return False

    return (s[0] == s[5] and s[1] == s[4] and s[2] == s[3])

palindrome = 0;
for i in xrange(100,999):
     for j in xrange(100,999):
          product = i * j
          if (product > palindrome and isPalindrome(str(product))):
              palindrome = product

print palindrome

#runtime: O(N)
