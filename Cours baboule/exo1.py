#!/usr/bin/python
# -*- coding: iso-8859-15 -*-#
#
#   EXERCICE 1
#   ===================================================
#   Calcul du résultat R en fonction du nombre choisi N
#   R = (3N+2)*2
#
import sys

N = input("Entrez un nombre : ")
N = int(N)
print ('le nombre choisi est :', N)

R = N*3
R = R+2
R = R*2

print ('Et voila le resultat : ', R)

