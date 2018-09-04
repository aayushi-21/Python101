import re,traceback

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

DATA1 ="""outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""


DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""

def lines(src):
    # Split data based on \n

    return src.split("\n")

def rows(src):
    res = []
    # Killing Bad Characters

    for x in src:
        a = x.split("#")
        b = a[0].strip()
        res.append(b)

    #Removing Blank spaces and combining the ,

    i = -1
    result = []
    flag = 0
    for x in res:
        if x.strip():
            if flag == 0:
                i = i + 1
                result.append(x)
            else:
                result[i] = result[i] + x
            if x.endswith(","):
                flag = 1
            else:
                flag = 0
    return result


# For getting the index of the column which has $ (integer)

def cols(src):
    int_columns = []
    the_list = []
    list = src[0].split(",") #Splitting words on the basis of ,
    for x in list:
        if not (x.find("$")):
            int_columns.append(list.index(x))
    the_list.append(src[0])
    for x in int_columns:
       for i in range(1,len(src)):
           list = src[i].split(",")
           list[x] = float(list[x])
           the_list.append(list)
    return the_list

#For getting the index of the column which has ? (needs to be removed)

def prep(src):
    remove_columns = []
    list = src[0].split(",")
    num = len(list)
    for x in list:
        if not (x.find("?")):
            remove_columns.append(list.index(x))
    for x in remove_columns:
       for i in range(1,len(src)):
           length = len(src[i])
           while length > num:
               src[i].pop(length-1)
               length = length -1
           src[i].pop(x)
    src.pop(0)

    return src


def ok0(s):
  for row in prep(cols(rows(lines(s)))):
    print(row)

@O.k
def ok1(): ok0(DATA1)

@O.k
def ok2(): ok0(DATA2)

if __name__ == "__main__":
    O.report()