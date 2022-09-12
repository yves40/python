#!/usr/bin/python
# -*- coding: iso-8859-15 -*-#
#
#   EXERCICE 2
#   ===================================================
#   Calcul du nombre choisi N en fonction du résultat R
#   N= R/6 – 4/6
#   
import sys

R = input('Entrez le resultat : ')
R = int(R)
print ('le resultat est :', R)
N = R/6
N = N - 4/6
print ('Et voila le nombre choisi : ', N)

