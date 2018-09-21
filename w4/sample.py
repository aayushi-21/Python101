from __future__ import division
import random
from math import floor
import re, traceback

class Config:
    def __init__(self):
        self.lo = 10**32
        self.hi = 10**32

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

class Sample:
    def __init__(self, myMax=Config().hi):
        self.max = myMax
        self.n = 0
        self.sorted = False
        self.some = []

    def sampleInc(self, x):
        self.n += 1
        now = len(self.some)
        if (now < self.max):
            self.sorted = False
            self.some.insert(now+1,x)
        elif (random.uniform(0,1) < (now / self.n)):
            self.sorted = False
            self.some[floor(0.5 + (random.uniform(0,1) * now))-1] = x
        return x

    def sampleSorted(self):
        if not self.sorted:
            self.sorted = True
            self.some.sort()
        return self.some

    def nth(self, n):
        s = self.sampleSorted()
        temp = floor(0.5 + (len(s) * n))
        temp = max(0, temp)
        return s[min(len(s), temp)]

@O.k
def sampleTest():
    random.seed(1)
    s = []
    for i in range(5, 10):
        s.append(Sample(2 ** i))

    for i in range(1,10001):
        y = random.uniform(0,1)
        for t in s:
            t.sampleInc(y)

    for t in s:
        print(t.max, t.nth(0.5))
        assert abs(t.nth(0.5) - 0.5) < 0.2
