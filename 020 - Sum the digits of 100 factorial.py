# Find the sum of the digits in the number 100!
import time
def factorial(x):
    product = 1
    for i in xrange(2, x+1):
        product *= i
    return product

start_time = time.time()
answer = sum(int(ch) for ch in str(factorial(100)))
total_time = time.time() - start_time

print answer
print "Elapsed: ", total_time, "seconds"
