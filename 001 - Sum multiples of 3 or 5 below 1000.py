# Find the sum of all the multiples of 3 or 5 below 1000.

import math

N = 1000
p = 3
q = 5

# The sum of multiples of p up to N
def SumOfMultiples(p, N):
    numMultP = math.floor((N-1) / p)
    return p * (numMultP + 1) * (numMultP / 2.0)

sumMultP = SumOfMultiples(p,N)
sumMultQ = SumOfMultiples(q,N)
sumMultPQ = SumOfMultiples(p*q, N)

# Get the sum for all p, the sum for all q, and subtract the interesection.
print sumMultP + sumMultQ - sumMultPQ

#Runtime:
# constant. 2 divisions and 3 multiplications for each of 3 terms.
