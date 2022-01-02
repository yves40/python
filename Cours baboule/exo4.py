#!/usr/bin/python
# -*- coding: iso-8859-15 -*-#
#
#   EXERCICE 4
#   ================================================
#   Comparaison de trois nombres ENTIERS. 
#   Trouver celui du milieu.
#
import sys, math

sys.stdout.write('Entrez le nombre ENTIER A : ')
A = sys.stdin.readline()
A = math.floor(float(A))
print 'A = ', A
sys.stdout.write('Entrez le nombre ENTIER B : ')
B = sys.stdin.readline()
B = math.floor(float(B))
print 'B = ', B
sys.stdout.write('Entrez le nombre ENTIER C : ')
C = sys.stdin.readline()
C = math.floor(float(C))
print 'C = ', C

if A < B :
  if B < C :
    print 'B est au mileu: ', A, B, C
  else:
    print 'C est au mileu: ', A, C, B
else:
  if A < C :
    print 'A est au milieu: ', B, A, C
  else:
    print 'C est au milieu: ', A, C, B
        
