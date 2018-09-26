from __future__ import division
import math
import re, traceback


class Sym:

    def equal(x):
        return x

    def __init__(self):
        self.counts = {}
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None

    def syms(self, t,f=equal):
        s = Sym()
        for i, x in enumerate(t):
            s.symInc(f(x))
        return s

    def symInc(self, x):
        if x is None:
            return x
        self._ent = None
        self.n += 1
        old = self.counts.get(x, 0)
        new = old and old + 1 or 1
        self.counts[x] = new
        if new > self.most:
            self.most, self.mode = new, x
        return self

    def symDec(self, x):
        self._ent = None
        self.n -= 1
        self.counts[x] = (self.counts.get(x, 0) - 1)
        return x

    def symEnt(self):
        if not self._ent:
            self._ent = 0
        for x, n in self.counts.items():
            p = n / self.n
            self._ent = self._ent - p * math.log(p, 2)
        return self._ent

