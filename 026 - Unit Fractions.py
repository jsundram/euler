# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
#    1/2	= 	0.5
#    1/3	= 	0.(3)
#    1/4	= 	0.25
#    1/5	= 	0.2
#    1/6	= 	0.1(6)
#    1/7	= 	0.(142857)
#    1/8	= 	0.125
#    1/9	= 	0.(1)
#    1/10	= 	0.1
#
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
import sys

# TODO: Is there a nicer version of loop detection? This sometimes returns 66 instead of 6, or has an offset 
# e.g. finds the right loop length, but not the right loop start.
# test cases: 7, 19, 122, 384, 499, 
# correct answer: 983
debug = False
def cycle_length(n):
    """This isn't ideal, but it works."""
    seen = dict()
    moved = set() # don't want to move more than once.
    s = ''
    loop_index = -1
    loop_length = 0
    loop_start = -1
    
    print "#### looking at 1 / %d" % n
    for (i, c) in enumerate(get_digits(n, 2000)):
        s += c
        if debug: print s
        if c not in seen:
            seen[c] = i
            if debug: print "seeing %s for the first time." % c
            if 0 <= loop_index:
                #print "cancelling search due to new value: %s" % c
                loop_index = -1 # can't be a loop if we haven't seen this yet.
        else:
            if loop_index <= 0:
                loop_index = seen[c]
                assert(s[loop_index] == c)
                loop_length = i - loop_index
                loop_start = i
                if loop_length == 1 and c != '0':
                    #print "found a loop of length 1 for %d: %s" % (n, s)
                    return 1
                if debug: print "looking for a loop of length %d" % loop_length
            else:
                if i < loop_start + loop_length:
                    index = i - loop_length
                    if s[index] != c:
                        # this isn't a loop
                        if debug: print "breaking out of loop: %s != %s" % (s[index], c)
                        if s[loop_start] not in moved:
                            seen[s[loop_start]] = loop_start
                            moved.add(s[loop_start])
                            if debug: print "setting first instance of %s to index %d" % (s[loop_start], loop_start)
                        loop_index = -1
                else:
                    if debug: print "found a loop of length %d for %d: %s" % (loop_length, n, s[loop_index:loop_index + loop_length])
                    return loop_length
    if debug: print "returning whole string for %d: length %d: %s" % (n, len(s), s)
    return len(s)

# this is just digits rewritten as a generator
def get_digits(n, max_digits=100):
    """Return a string of digits that represent mantissa of the reciprocal of the input number.
        e.g. 1 / 2 -> 5
    """
    d = '' # to be real accurate, this should be '0.', but I don't need itself.
    dividend = 10
    remainder = 1 # Hack
    while remainder != 0 and len(d) < max_digits:
        if remainder < dividend:
            digit = dividend / n
            remainder = dividend - (digit * n)
        else:
            digit = 0
            remainder = dividend
        dividend = remainder * 10
        d += str(digit)
        yield str(digit)
        
# rewrite this as a generator
def digits(n, max_digits=100):
    """Return a string of digits that represent mantissa of the reciprocal of the input number.
        e.g. 1 / 2 -> 5
    """
    
    # Remember how we did division in elementary school? This is that.
    d = '' # to be real accurate, this should be '0.', but I don't need itself.
    dividend = 10
    remainder = 1 # Hack
    while remainder != 0 and len(d) < max_digits:
        if remainder < dividend:
            digit = dividend / n
            remainder = dividend - (digit * n)
        else:
            digit = 0
            remainder = dividend
            
        d += str(digit)
        
        dividend = remainder * 10
    return d

def brute_force():
    start = 7
    end = 0
    if 1 < len(sys.argv): 
        start = int(sys.argv[1])
    if 2 < len(sys.argv): 
        end = int(sys.argv[2])
    
    if end == 0:
        cycle_length(start)
        return
        
    max_cycle = (0, 0)
    for i in xrange(start, end+1): # 2, 1000 for the question asked
        n = cycle_length(i)
        if n > max_cycle[1]:
            max_cycle = (i, n)
    
    print "Max Cycle Length: %d for 1 / %d" % (max_cycle[1], max_cycle[0])

def elegant():    
    """According to MathWorld: http://mathworld.wolfram.com/DecimalExpansion.html
        The number of digits in the repeating portion of the decimal expansion of a rational number 
        can also be found directly from the multiplicative order of its denominator.
        We also know that the upper bound for the number of digits in 1 / n is n-1. 
    """
    def order(b, n):
        """The multiplicative order of n relative to b:
            http://mathworld.wolfram.com/MultiplicativeOrder.html
            
            NOTE: n and b must be relatively prime.
        """
        import itertools
        for i in itertools.count(1):
            if b ** i % n == 1:
                return i
    
    has_factor_of_10 = lambda x: x % 5 == 0 or x % 2 == 0
    relatively_prime_to_10 = lambda x : not has_factor_of_10(x)
    get_second = lambda x: x[1] # returns the second item in a tuple
    
    (n, repeat_length) =  max([(i, order(10, i)) for i in filter(relatively_prime_to_10, range(2, 1001))], key=get_second)
    print "Max Cycle Length: %d for 1 / %d" % (repeat_length, n)
    
def main():
    brute_force()
    elegant()
if __name__ == "__main__":
  sys.exit(main())