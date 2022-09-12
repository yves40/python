#!/usr/bin/python
# -*- coding: iso-8859-15 -*-#
#
#   EXERCICE 4
#   ================================================
#   Comparaison de trois nombres ENTIERS. 
#   Trouver celui du milieu.
#
import sys, math

A = input('Entrez le nombre ENTIER A : ')
A = math.floor(float(A))
print ('A = ', A)
B = input('Entrez le nombre ENTIER B : ')
B = math.floor(float(B))
print ('B = ', B)
C = input('Entrez le nombre ENTIER C : ')
C = math.floor(float(C))
print ('C = ', C)
# Quel nombre est au milieu ? Solutions possibles :
#   A B C **
#   A C B **
#   C A B **
#   B A C **
#   B C A **
#   C B A **
if A < B :
  if B < C :
    print ('B est au milieu: ', A, B, C)
  elif A < C:
    print ('C est au milieu: ', A, C, B)
  else:
    print ('A est au milieu: ', C, A, B )   
else:
  if B > C :
    print ('B est au milieu: ', C, B, A)
  elif A > C:
    print ('C est au milieu: ', B, C, A)
  else:
    print ('A est au milieu: ', B, A, C)

        
