# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# E.G.  The proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
#       The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math

# d might better be called "sumProperDivisors"
def d(N):
    total = 1
    for i in xrange(2, math.sqrt(N)+1):
        if ((N % i) == 0):
            total += i
            dividend = N / i
            if ( dividend != i):
                total += dividend
    return total

# Testing:
#print d(220)
#print d(284)

total = 0
count = 0
bound = 10000
for i in xrange(1,bound):
    D = d(i)
    # to avoid double counting, make sure i < D
    if (i < D < bound and d(D) == i):
        print "d(", i, ") = d(", D, ")"
        count += 2
        total += D + i

print count, " amicable numbers, totalling ", total
