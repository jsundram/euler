# What is the largest prime factor of the number 317584931803?

# N.B. Pollard-Strassen is the fastest known deterministic algorithm,
# according to Mathworld: http://mathworld.wolfram.com/PrimeFactorizationAlgorithms.html
#
# Quadratic Sieve is probably easier to implement:
# http://en.wikipedia.org/wiki/Quadratic_sieve#The_algorithm
import math


# Brain-dead approach
K = 317584931803


def factor(K):
    factors = []
    for i in xrange(2, math.floor(math.sqrt(K))):
        if (K % i == 0):
            factors.append(i)
            factors.append(K / i)
    factors.sort()
    return factors
    
primes = []
for k in factor(K):   
    if (len(factor(k)) == 0):
        primes.append(k)
primes.sort()

print primes[len(primes)-1]

# Runtime:
# if n is the number of factors of the integer N
# O(sqrt(N)/2) (to find the factors)
# O(n*sqrt(N)) to test primality of each of them. Not really N, but something smaller than it.
