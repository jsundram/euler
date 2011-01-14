# Find the sum of all the primes below two million.

import math, time

# Make a sieve that goes up to 2 Million
# fill sieve with integers from 2 to 2 million.
# go through and set entries to zero as you move through.
# calculate sum of sieve.

start_time = time.time()
UPPER_BOUND = 2000000
sieve = range(0,UPPER_BOUND)
total = 0;
for i in xrange(2, UPPER_BOUND):
    if (sieve[i] != 0):
        total += sieve[i]
        for j in xrange(i, UPPER_BOUND, i):
            sieve[j] = 0

print total
print "Elapsed Time: ", time.time() - start_time, "second(s)"
