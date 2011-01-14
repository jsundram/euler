# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Check this out: http://mathworld.wolfram.com/Permutation.html
def factorial(x):
    product = 1
    for i in xrange(2, x+1):
        product *= i
    return product

# s is a string?
def permutation(k, s):
    n = len(s)
    f = factorial(n-1)

    for j in xrange(1, n-1):
        tempj = (k / f) % (n + 1 - j)

        temps = s[j+ tempj]

        for i in xrange(j+tempj, j+1, -1):
            s[i] = s[i - 1] #shift the chain right

        s[j] = temps

        f = f / (n- j)
        
    return s

print permutation(6, [0,1,2])
