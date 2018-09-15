from __future__ import division
import math
import re, traceback

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


@O.k

def baseSym():
    s = Sym()
    s = s.syms(['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'n', 'n', 'n', 'n', 'n'])
    print(s.counts)
    assert (round(s.symEnt(), 4) == 0.9403)
