from row import rows
from num import Num
import traceback,re
from dom import doms
import math
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

def super(data):
    rows = data.rows
    goal = len(rows[1]) -1
    enough = len(rows) ** 0.5
    most = 0
    cut_var_n = []
    col_split_val = []

    def band(c, lo, hi):
        if lo == 0:
            return ".." + str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c]) + ".."
        else:
            return str(rows[lo][c]) + ".." + str(rows[hi][c])

    def argmin(c, lo, hi):
        mu = 0
        cut = None
        xl, xr = Num(), Num()
        yl, yr = Num(), Num()
        for i in range(lo,hi+1):
            xr.numInc(rows[i][c])
            yr.numInc(rows[i][goal])
        bestx = xr.sd
        besty = yr.sd
        mu = yr.mu

        for i in range(lo, hi + 1):
            x = rows[i][c]
            y = rows[i][goal]
            xl.numInc(x)
            xr.numDec(x)
            yl.numInc(y)
            yr.numDec(y)
            if xl.n >= enough and xr.n >= enough:
                tmpx = Num.numXpect(xl, xr) * 1.0
                tmpy = Num.numXpect(yl, yr) * 1.0
                if tmpx < bestx and tmpy < besty:
                    (cut, bestx, besty) = i, tmpx, tmpy
        return cut,mu

    def cuts(c, lo, hi, pre):
        txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
        cut,mu = argmin(c, lo, hi)
        if cut:
            print(txt)
            cuts(c, lo, cut, pre + "|.. ")
            cuts(c, cut + 1, hi, pre + "|.. ")
        else:
            s = band(c, lo, hi)
            print(txt + " (" + math.floor(100*mu) + ")")
            for r in range(lo, hi + 1):
                rows[r][c] = s


    def stop(c, t):
        for i in range(len(t) - 1, -1, -1):
            if t[i][c] != "?": return i
        return 0

    for c in data.indeps:
        if c in data.nums:
            rows = sorted(rows, key=lambda x: str(x[c]))
            most = stop(c, rows)
            print("\n---------- Output ----------")
            cuts(c, 0, most, "|.. ")
    print("\n")
    title = data.name
    title = ' '.join(title)
    print(title)
    for s in rows:
        print(*s)

def mainsuper(s):
    print("WeatherLong.csv")
    super(rows(s))

@O.k
def testsuper():
    mainsuper("Weather.csv")
