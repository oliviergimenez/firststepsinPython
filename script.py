"""
Training Dec 11
"""

# Hello world
print("hello world!")
test = "hello world"
print(test)

# tuple
bla = (4, 5, "booh", True)
print(bla)
print(bla[0])
print(bla[-1]) # dernier element

print(len(bla))

# lists

bla = [4, 5, "booh", True]
print(bla)
bla.append()

# dictionnaires

# sets
setA = {4, 5, "hi", 42}
print(setA)
setA.add(44)
print(setA)
setB = {4, 5, 122, 826}
print(setA | setB)
print(setA - setB)

# conditions

if True:
  print("ok")
elif False:
  print("ttttt")
else:
  print("impossible")


if True:
  print("ok")
else:
  pass

5 == 6

5 != 6

5 in [5, 6, 7]

5 not in [5, 6, 7]

not 5 == 6

# loops
tList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tList)
for iIndex in range(len(tList)):
  tList[iIndex]+=1
print(tList)

tList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tList)
for iIndex in range(len(tList)):
  tList[iIndex] = tList[iIndex] + 1
print(tList)

# supprime chiffres pairs
tList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tList)
for iValue in tList:
  if iValue%2==0:
    tList.remove(iValue)
print(tList)

# use keyword continue to pass an iteration
# and keyword break to quit the block

# functions

# my first function
def Racine(iValue, iRacine):
  print(iValue**(1/iRacine))
Racine(4, 2)
Racine(8, 3)

# function with outputs
def Racine(iValue, iRacine):
  fReponse = iValue**(1/iRacine)
  return fReponse 
#  print(fReponse)

stockage = Racine(4, 2)
print(stockage)

# arguments by default
def Racine(iValue = 4, iRacine = 2):
  fReponse = iValue**(1/iRacine)
  return fReponse 
#  print(fReponse)

stockage = Racine()
print(stockage)

