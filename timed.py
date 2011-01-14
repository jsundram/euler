#!/usr/bin/env python
# encoding: utf-8
"""
timed.py

Copyright (c) 2009 The Echo Nest. All rights reserved.
"""

import sys
import os
import time

def timed(func):
    """See how long a function takes to run."""
    def wrapper(*arg):
        t1 = time.time()
        e = None
        try:
            res = func(*arg)
        except KeyboardInterrupt, e: # Just KeyboardInterrupt?
            pass
        
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        
        if e:
            raise e
        return res
    return wrapper


# TODO: could use threading.Timer to report every n seconds instead of every n loop iterations
class loop_timer(object):
    """
    A class to estimate the completion of a loop.
    Use as follows: for x in loop_timer(some_iterable, interval): # do stuff

    Since this wraps an iterable, it is iterable:
    http://www.bearfruit.org/prolixities/tech/simple-iterable-objects-in-python
    """
    def __init__(self, iterable, measurement_interval=100):
        self.stuff = iterable
        self.counter = 0
        self.interval = measurement_interval
        self.start = time.time()
        try:
            self.len = len(self.stuff)
        except Exception:
            self.len = 10 * measurement_interval ** 2 # assign an arbitrary len for generators

    def __len__(self):
        return self.len

    def str(self, t):
        "Represents a time interval as a duration in HH:MM:SS"
        return "%d:%02d:%02d" % (t / 3600, (t % 3600) / 60, t % 60)

    def time(self, t):
        "Returns a time of day that is the current time + the given interval"
        return time.strftime("%I:%M %p", time.localtime(time.time() + t))

    def print_progress(self):
        i = self.counter
        if i != 0 and i % self.interval == 0:
            elapsed = time.time() - self.start
            remaining = elapsed * ((float(self.len) / i) - 1)
            print "%d items processed in %s. (%s remaining for %d [ETA: %s, est. total:%s])" % (i, self.str(elapsed), self.str(remaining), self.len-i, self.time(remaining), self.str(elapsed + remaining))            

    def next(self):
         if self.counter >= self.len:
             self.counter = 0
             print "Total Duration for %d items: %s" % (self.len, self.str(time.time() - self.start))
             raise StopIteration
         else:
             c = self.counter
             self.print_progress()
             self.counter = c + 1
             return self.stuff[c] # this won't work for generators

    def __getitem__(self, item):
        return self.stuff[item]

    def __iter__(self):
      return self
      
def main():
    pass


if __name__ == '__main__':
    main()

