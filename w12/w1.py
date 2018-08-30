import re,traceback
from cmath import exp
from functools import partial
from collections import Counter

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

class O:
  y=n=0
  @staticmethod
  def report():
    print("\n# pass= %s fail= %s %%pass = %s%%"  % (
          O.y,O.n, int(round(O.y*100/(O.y+O.n+0.001)))))
  @staticmethod
  def k(f):
    try:
      print("\n-----| %s |-----------------------" % f.__name__)
      if f.__doc__:
        print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
      f()
      print("# pass")
      O.y += 1
    except:
      O.n += 1
      print(traceback.format_exc())
    return f


@O.k
def WhiteSpace_Testing():
    sum = 10.1 + \
            3
    assert sum == 13.1

@O.k
def Module_Testing():
    import math
    root = math.sqrt(9)
    assert root == 3

@O.k
def Arithmetic_Testing():
    variable_one = 5 / 2
    variable_two = 5 // 2
    assert variable_one != variable_two

@O.k
def Function_Testing():
    double = lambda x:x*2
    assert 10 == double(5)

def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32

@O.k
def Functional_Testing():

    KelvinToFahrenheit(273)

@O.k
def String_Testing():
    quoted_string = "FFS is Fun"
    assert len(quoted_string) == 10
@O.k
def Exception_Testing():
    try:
        var = FFS_Class
    except NameError:
        var = 6
    assert var == 6

@O.k
def List_Testing():
    sorted_list = [1,2,3,4,5]
    sorted_list.append(0)
    assert sorted_list[-1] < sorted_list[-2]

@O.k
def List_testing():
    _, y = [1, 2]
    assert y==2

@O.k
def Tuple_Testing():
    x, y = 5, 7
    x, y = x + y, y + x
    assert x == y

@O.k
def Dictionary_Tetsing():
    spanish = dict()
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    assert 'uno' in spanish.values()
    assert len(spanish) == 3

@O.k
def DefaultDictionaries_Testing():
    from collections import defaultdict
    word = 'mississippi'
    d = defaultdict(int)
    for k in word:
        d[k] += 1
    diffChar = len(d.keys())
    assert diffChar == 4

@O.k
def Counters_Testing():
    listcounter = Counter(["Hello", "NewYork", "Its", "New", "Year","New","beginnings"]).most_common(1)
    assert listcounter == [("New", 2)]

@O.k
def Set_Testing():
    random_list = [0,1,2,1,2,4,5,6,3,2]
    random_set = set(random_list)

    assert len(random_set) == 7
    assert len(random_list) == 10

@O.k
def ControlFlow_Testing():
    if 1 > 2:
        assert 1 > 2
    else:
        assert 1 <= 2

@O.k
def Truthiness_Testing():
    assert all([True, 0.1, { 2,4,5 }])
    assert any([False, 7.8, {}])

@O.k
def Sorting_Testing():
    x = sorted([-4,1,-2,3], reverse=True)
    assert x[0]==3

@O.k
def ListComprehension_Testing():
    one = [1, 2, 3]
    two = {x * 1 for x in one}
    assert len(one) == len(two)

@O.k
def GeneratorsIterators_Testing():
    x = range(1,100)
    for a in x:b = a
    assert b == 99
    
@O.k
def Randomness_Testing():
    from random import randrange
    assert randrange(5, 8) in [5, 6, 7, 8]

@O.k
def RegularExpressions_Testing():
    assert 'FSSCOURSE'.isupper()
    assert 'FSS Fun'.split() == ['FSS','Fun']

@O.k
def ObjectOriented_Testing():
    cal = Calculator(5, 6)
    assert cal.add() == 11

@O.k
def FunctionalTools_Testing():
    def triple(x):
        return 3 * x

    values = [1, 2, 3, 4]
    tripled = [triple(x) for x in values]
    assert tripled == [3,6,9,12]

@O.k
def Enumerate_Testing():

    my_list = ["apple", "banana", "grapes", "pear"]
    counter_list = list(enumerate(my_list, 1))

    for i, document in enumerate(counter_list):
        if i > 2:
            assert document == counter_list[3]

@O.k
def ZipArgumentUnpacking_Testing():
    ids = ['200202503', '200202504', '200202504']
    courses = ['FSS', 'Software Securtiy', 'Computer Networks']
    combined = list(zip(ids, courses))
    assert combined[0] == ('200202503','FSS')

def multipleAddition(n,*argv):
    for arg in argv:
        n = n + arg
    return n

@O.k
def Args_Testing():
    assert multipleAddition(1, 2, 3, 4) == 10


def getName(first, last, **kwargs):
    return first + kwargs['middle'] + last

@O.k
def Kargs_Testing():
    assert getName('a', 'c', middle='b') == 'abc'


if __name__== "__main__":
  O.report()
