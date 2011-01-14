import operator
def factorial(n):
    return reduce(operator.mul, xrange(2, n+1), 1)

def proper_divisors(n):
    divisors = [1]
    for i in xrange(2, 1 + int(n**.5)):
        d, r = divmod(n, i)
        if (r == 0):
            divisors.append(i)
            divisors.append(d)
    return sorted(divisors)
    
def factor(n):
    """simple, stupid prime factorization. returns prime factors in sorted order"""
    def _factor(K):
        factors = []
        for i in xrange(2, 1+int(K**.5)):
            d, r = divmod(K, i)
            if (r == 0):
                factors.append(i)
                factors.append(d)
        return factors
    
    #print _factor(n)
    primes = [k for k in _factor(n) if len(_factor(k))==0]
    primes.sort()
    return primes

def get_primes(N=1000000):
    """Fastest primes yet, bool sieve with range assignment."""
    if N <=0: return []
    # Maybe could do better: look here: 
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python
    sqrt_N = 1 + int(N**.5)
    sieve = [True] * (N + 1)
    sieve[0] = False; sieve[1] = False
    
    for i in xrange(2, sqrt_N):
        if sieve[i]:
            m = N / i - i
            sieve[i*i:N+1:i] = [False] * (m + 1)
    
    return [i for i in xrange(N+1) if sieve[i]]
    
def is_prime(n):
    """Checks for odd divisors less than sqrt(n)"""
    if n < 2: return False
    elif n % 2 == 0: return n == 2
    
    stop = 1 + int(n ** .5)
    for i in xrange(3, stop, 2):
        if n % i == 0:
            return False
    return True

def gcd(x, y):
    """from http://blog.tomgraft.com/fast-gcd-in-python--36/. Faster than recursion"""
    while x:
        x, y = y % x, x
    return y

def is_perfect_square(n):
    s = n**.5
    return s == int(s)

def root_expansion(n):
    """Takes as input an integer n, and outputs the expansion of its square root up to where it would repeat."""
    # Used by 64-66
    class Frac(object):
        """Encapsulate the continued fraction expansion of the sqrt of input N"""
        # Expansion is of form (k*sqrt(q) + a) / n
        def __init__(self, num):
            self.Q = num
            self.K = 1
            self.A = 0
            self.N = 1
        
        def next(self):
            s = self
            int_part = int((s.K * s.Q**.5 + s.A) / s.N);
            s.A -= int_part * s.N
            
            k = s.K
            a = s.A
            
            s.K =  s.N * s.K
            s.A = -s.A * s.N
            s.N =  k*k * s.Q - a*a
            
            _gcd = reduce(gcd, [s.K, s.A, s.N])
            
            s.K /= _gcd
            s.A /= _gcd
            s.N /= _gcd
            
            return int_part, s.N == 1
        
        def expand(self):
            if is_perfect_square(self.Q):
                return [self.Q**.5]
            
            expansion = []
            done = False
            while not done:
                n, done = self.next()
                expansion.append(n)
            expansion.append(self.next()[0])
            return expansion
            
    f = Frac(n)
    return f.expand()


def convergents(A, n):
    """Returns the first n convergents as tuples, given root expansion A. See 66 for an example use."""
    
    # Since A is cyclic, just generate some more terms.
    m = len(A)
    while len(A) < n:
        A += A[1:m]
    
    @memoized # recursion + performance
    def p(n, a=A):
        if n == 0:
            return a[0]
        elif n == 1:
            return a[0] * a[1]  + 1
        
        return a[n] * p(n-1) + p(n-2)
    
    @memoized
    def q(n, a=A):
        if n == 0:
            return 1
        elif n == 1:
            return a[1]
            
        return a[n] * q(n-1) + q(n-2)
    
    f = lambda x : tuple([p(x), q(x)])
    
    return map(f, range(n+1))


# miller-rabin primality test courtesy of Eli Bendersky:
# http://eli.thegreenplace.net/2009/02/21/rabin-miller-primality-test-implementation/
from random import randint
def _bits_of_n(n):
    """ Return the list of the bits in the binary
        representation of n, from LSB to MSB
    """
    bits = []
    
    while n:
        bits.append(n % 2)
        n /= 2
    
    return bits

def _MR_composite_witness(a, n):
    """ Witness functions for the Miller-Rabin
        test. If 'a' can be used to prove that
        'n' is composite, return True. If False
        is returned, there's high (though < 1)
        probability that 'n' is prime.
    """
    rem = 1

    # Computes a^(n-1) mod n, using modular
    # exponentation by repeative squaring.
    #
    for b in reversed(_bits_of_n(n - 1)):
        x = rem
        rem = (rem * rem) % n
        
        if rem == 1 and x != 1 and x != n - 1:
            return True
        
        if b == 1:
            rem = (rem * a) % n
        
    return rem != 1

def is_prime_MR(n, trials=6):
    """ Determine whether n is prime using the
        probabilistic Miller-Rabin test. Follows
        the procedure described in section 33.8
        in CLR's Introduction to Algorithms

        trials:
            The amount of trials of the test.
            A larger amount of trials increases
            the chances of a correct answer.
            6 is safe enough for all practical
            purposes.
    """
    if n < 2:
        return False

    for ntrial in xrange(trials):
        if _MR_composite_witness(randint(1, n - 1), n):
            return False

    return True

# These are in itertools in python 2.6: 
# http://docs.python.org/library/itertools.html
def product(*args, **kwds):
    """ Cartesian product of input iterables.
        Equivalent to nested for-loops in a generator expression. 
        For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
    """
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = map(tuple, args) * kwds.get('repeat', 1)
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

def combinations(iterable, r):
    """ Return r length subsequences of elements from the input iterable.
        Combinations are emitted in lexicographic sort order. 
        So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
        Elements are treated as unique based on their position, not on their value. 
        So if the input elements are unique, there will be no repeat values in each combination.
    """
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

def bsearch(lo, hi, f, X):
    """ adapted from http://stackoverflow.com/questions/212358/binary-search-in-python
        the domain is [lo, hi). We find for x such that f(x) == X, or -1 if no such integer x exists.
    """
    while lo < hi:
        mid = (lo + hi) // 2
        # print "%d, %d, %d" % (lo, mid, hi)
        midval = f(mid)
        if midval < X:
            lo = mid + 1
        elif midval > X: 
            hi = mid
        else:
            return mid
    return -1

# from http://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = value = self.func(*args)
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__