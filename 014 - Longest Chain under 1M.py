# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
#
# Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time
start_time = time.time()

def getNext(N):
    if (N & 1):
        return 3*N + 1
    else:
        return N >> 1

chainlength = {1:1} # Poor man's memoization
def length(N):
    if (chainlength.has_key(N)):
        return chainlength[N]
    ret = 1 + length(getNext(N))
    chainlength[N] = ret
    return ret

longest = 0
generator = 0
for i in xrange(1, 1000000):
    l = length(i)
    if (l > longest):
        longest = l
        generator = i
    
time_elapsed = time.time() - start_time

print generator, ":", longest
print "Time elapsed: ", time_elapsed, " second(s)"

# Naive approach takes 122 seconds, so
# I did some adhoc memoization to get it to 6 seconds
    
    
