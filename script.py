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

# libraries

import time # time.time
import random # random.randint
import sys
import os # os.listdir
# docs.python.org/fr/3/library

# exercice jeu de bataille

""" 
On distribue les 52 cartes aux joueurs (peut se jouer à deux) qui les rassemblent en paquet devant eux. 
Chacun tire la carte du dessus de son paquet et la pose sur la table.
Celui qui a la carte la plus forte ramasse les autres cartes. 
L'as est la plus forte carte, puis roi, dame, valet, 10, etc.
Lorsque deux joueurs posent en même temps deux cartes de même valeur il y a "bataille". 
Lorsqu'il y a "bataille" les joueurs tirent la carte suivante et la posent, face cachée, sur la carte précédente. 
Puis ils tirent une deuxième carte qu'ils posent cette fois-ci face découverte et c'est cette dernière qui départagera les joueurs. 
Le gagnant est celui qui remporte toutes les cartes.
"""

"""
Créer un paquet de 52 cartes.
Le partager équitablement de façon aléatoire entre deux joueurs.
Faire s’affronter les deux joueurs.
A chaque tour, chaque joueur pioche sa première carte. Le vainqueur emporte
le pli et le place sous sa pioche. En cas d’égalité, une bataille a lieu (ajout
d’une carte face cachée puis d’une carte face visible) jusqu’à ce qu’un
vainqueur l’emporte.
Le premier joueur à ne pas pouvoir piocher de carte a perdu.
Le programme doit afficher :
Le nombre du tour en cours
Le nom des cartes jouées par chaque joueur (ou le fait qu’ils jouent une
carte face cachée)
Annoncer une bataille
Signaler qui emporte le pli
Donner le nom du vainqueur de la partie
"""

listeCartes = ["Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Valet", "Reine", "Roi", "As"]
listeCouleurs = ["de Pique", "de Trefle", "de Coeur", "de Carreau"]

for i in listeCartes:
  print(i)

for i in listeCartes:
  print(i)
  for j in listeCouleurs:
    print("\t..."+j)


for i in listeCartes:
  for j in listeCouleurs:
    print(i+" "+j)

# step 1
def CreateDeck(listeCartes, listeCouleurs):
  valeur = 0
  paquet = {}
  for i in listeCartes:
    valeur = valeur + 1
    for j in listeCouleurs:
      nom = i + " " + j
      paquet[nom] = valeur
  return paquet
#    print(i + " " + j + ":" + str(valeur))

listeCartes = ["Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Valet", "Reine", "Roi", "As"]
listeCouleurs = ["de Pique", "de Trefle", "de Coeur", "de Carreau"]

CreateDeck(listeCartes, listeCouleurs)

# step 2

def Shuffle(listeCartes, listeCouleurs):






deck = []
for i in listeCartes:
  for j in listeCouleurs:
    nom_carte = i + " " + j
    deck.append(nom_carte)
deck_shuffled = random.sample(deck, len(deck))




Shuffle(listeCartes, listeCouleurs)

jeu = []
for i in range(listeCartes):
  for j in listeCouleurs:
    jeu[i, j] = i + " " + j


def tire_carte(carte, couleur):
  listeCartes = ["Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Valet", "Reine", "Roi", "As"]
  listeCouleurs = ["de Pique", "de Trefle", "de Coeur", "de Carreau"]
  return "{} {}".format(listeCartes[carte], listeCouleurs[couleur])

set_card_name(0, 3)

def

