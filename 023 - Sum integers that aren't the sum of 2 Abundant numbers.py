# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
# which means that 28 is a perfect number.
#
# A number whose proper divisors are less than the number is called deficient and 
# a number whose proper divisors exceed the number is called abundant.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 
# can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though
# it is known that the greatest number that cannot be expressed as the sum of two abundant numbers 
# is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

UPPER_LIMIT = 28124

import math
import cProfile
from bisect import bisect
def sum_divisors(N):
    total = 1
    for i in xrange(2, math.sqrt(N)+1):
        if (N % i == 0):
            total += i
            if ((i * i) != N):
                total += (N / i)
    return total

abundant = []
for i in xrange(11, UPPER_LIMIT):
    if (sum_divisors(i) > i):
        abundant.append(i)


print "found: ", len(abundant), " abundant numbers less than ", UPPER_LIMIT
print "highest abundant number: ", abundant[-1]

# Smart: compute all the sums of the abundant numbers we have. Store everything in an array.
def AddIntegersNotExpressibleAsTheSumOfTwoAbundantNumbers():
    # Create an array that is zero everywhere, then punch out the number
    # that are expressible as the sum of two abundant numbers
    integers = [0] * UPPER_LIMIT
    for i in xrange(0, len(abundant)):
        for j in xrange(i, len(abundant)):
            addend = abundant[i] + abundant[j]
            if (addend < UPPER_LIMIT):
                integers[addend] = 1
            else:
                break; #don't bother going this high

    # We've filled in the array. Now do the sum
    return sum(i for i in xrange(0, UPPER_LIMIT) if integers[i] == 0)

#cProfile.run('AddIntegersNotExpressibleAsTheSumOfTwoAbundantNumbers()')
print AddIntegersNotExpressibleAsTheSumOfTwoAbundantNumbers()


# Somebody else (norvig) did this, which is really slick!
def norvig():
    abundants = set(i for i in range(1,28124) if sum_divisors(i) > i)
    def abundantsum(i):
        return any(i-a in abundants for a in abundants)
    return sum(i for i in range(1,28124) if not abundantsum(i))

            
                            
