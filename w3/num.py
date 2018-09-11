from __future__ import division
import random
from math import floor
import re, traceback

from sample import *

class O():
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f

class Num:

    def __init__(self, no=[]):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = 10**32
        self.hi = -10**32
        self.some = Sample()
        self.w = 1
        for x in no:
            self.nums(x)

    def nums(self,x):
        self.numInc(x)

    def numInc(self,x):
        if x is None:
            return x
        self.n += 1
        self.some.sampleInc(x)
        d = x - self.mu
        self.mu += (d / self.n)
        self.m2 += (d * (x - self.mu))
        if (x > self.hi):
            self.hi = x
        if (x < self.lo):
            self.lo = x
        if (self.n >= 2):
            self.sd = ((self.m2 / (self.n - 1 + (10 ** -32))) ** (.5))
        return x


    def numDec(self, x):
        if x in None:
            return x
        if (self.n == 1):
            return x
        self.n -= 1
        d = x - self.mu
        self.mu -= (d / self.n)
        self.m2 -= (d * (x - self.mu))
        if (self.n >= 2):
            self.sd = ((self.m2 / (self.n - 1 + (10 ** -32))) ** (.5))
        return x


    def numNorm(self, x):
        return (x - self.lo) / (self.hi - self.lo + (10 ** -32))


    def numXpect(i, j):
        n = i.n + j.n + .0001
        return i.n / n * i.sd + j.n / n * j.sd

@O.k
def numOkay():
        n = Num([4, 10, 15, 38, 54, 57, 62, 83, 100, 100, 174, 190, 215, 225,
                 233, 250, 260, 270, 299, 300, 306, 333, 350, 375, 443, 475,
                 525, 583, 780, 1000])
        print(n.mu)
        print(round(n.sd, 3))
