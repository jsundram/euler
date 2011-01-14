#Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed one million.

import math

# Golden Ratio
ROOT_5 = math.sqrt(5)
X = (1.0 + ROOT_5) / 2.0

# Closed form for the Nth fibonacci number
def Fibonnaci(n):
    return math.floor(((X ** n) / ROOT_5) + .5)

# Every 3rd term in the fibonacci sequence is even, so we can just sum those. 
index = 0
total = 0;
ONE_MILLION = 1000000
while (True):
    index += 3
    evenFib = Fibonnaci(index)
    if (evenFib >= ONE_MILLION):
        break;
    total += evenFib
    
print total

# Runtime - 1 exponentiation and a division for every even fibonacci number < 1M.
# There are log(K * ROOT_5) / log(X) fibonacci numbers (+/- 1) less than K.
# So our runtime is O( log(K * sqrt(5)) / 3*log(X)), since we only compute a third of the numbers.
# For K = 1000000, we have 30 fibonacci numbers, of which we compute 10.
