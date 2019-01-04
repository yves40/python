#!/usr/bin/python

valeur = ['2', '3', '4', '5', 'As']

def meilleurCarte(liste):
    taille = len(liste)
    position = []
    for i in range(taille):
      for elmt in valeur:
        if liste[i] == elmt
          position.append(valeur.index(elmt))
    indexmax = position.index(max(position))
    meilleurcarte = liste[indexmax]

    return meilleurcarte


for x in valeur:
    print x, 'likes jelly beans.'

best = meilleurCarte(['3', 'As', '5'])
print(best)

