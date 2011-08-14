# What is the 10001st prime number?
# Answer 104,743 - see http://primes.utm.edu/nthprime/index.php#nth
# 
# But let's do it manually:
# By the prime number theorem, there are pi(n) primes < n, where
# pi(n) = n / ln(n)
#
# Since we are looking for the 10,001th prime, pi(n) = 10,001. What's n?
# 10,0001 = n / ln(n)
# So, we can safely use n to be roughly 150,000.

from timed import timed

@timed
def original_solution():
    # 1) Construct a sieve
    # 2) Find the 10,0001st prime in it.
    UPPER_BOUND = 150000
    sieve = range(0, UPPER_BOUND)
    counter = 0
    for i in xrange(2, UPPER_BOUND):
        if sieve[i] != 0:
            counter += 1 # prime!
            if counter == 10001:
                return sieve[i]
            else:
                for j in xrange(i, UPPER_BOUND, i):
                    sieve[j] = 0

def main():
    print 'The answer (original) is: %d' % original_solution()


if __name__ == '__main__':
    main()



