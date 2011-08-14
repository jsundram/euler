# What is the largest prime factor of the number 317584931803?

# N.B. Pollard-Strassen is the fastest known deterministic algorithm,
# according to Mathworld: http://mathworld.wolfram.com/PrimeFactorizationAlgorithms.html
#
# Quadratic Sieve is probably easier to implement:
# http://en.wikipedia.org/wiki/Quadratic_sieve#The_algorithm
import math
from timed import timed

# Brain-dead approach
def factor(K):
    factors = []
    for i in xrange(2, int(math.sqrt(K))):
        if K % i == 0:
            factors.append(i)
    print K, factors
    return factors

@timed
def golfed(n):
    return max(k for k in factor(n) if len(factor(k)) == 0)

@timed
def original_solution(n):
    """runtime on mba is 80ms""" 
    primes = []
    for k in factor(n):   
        if len(factor(k)) == 0:
            primes.append(k)

    print "primes:",  primes
    return max(primes)

# Runtime:
# if n is the number of factors of the integer N
# O(sqrt(N)/2) (to find the factors)
# O(n*sqrt(N)) to test primality of each of them. Not really N, but something smaller than it.
def main():
    N = 317584931803
    print 'The answer (original) is: %d' % original_solution(N) # golfed(N)

if __name__ == '__main__':
    main()
