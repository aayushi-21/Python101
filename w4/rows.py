from sample import *
from num import *
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



class data:

    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.Class=None
        self.rows = {}
        self.name = {}
        self._use = {}

    def indep(self,c):
        return not self.w[c] and self.Class!=c

    def dep(self,c):
        return not self.indep(c)
