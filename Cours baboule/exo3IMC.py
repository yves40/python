#!/usr/bin/python
# -*- coding: iso-8859-15 -*-#
#
#   EXERCICE 3
#   ================================================
#   Calcul d'IMC
#
import sys

print '-----------------------------------------------'
print 'Rappel des seuils IMC'
print ' Extra   si : POIDS < 18.5'
print ' Normal  si : 18.5 < POIDS < 25'
print ' Mauvais si : POIDS > 18.5'
print '-----------------------------------------------'
sys.stdout.write('Entrez votre taille (m) : ')
TAILLE = sys.stdin.readline()
sys.stdout.write('Entrez votre poids (kg ): ')
POIDS = sys.stdin.readline()
TAILLE = float(TAILLE)
IMC = int(POIDS) / (TAILLE*TAILLE)

print 'Votre IMC est de : ', IMC, ' ********************'
print

if IMC < 18.5 :
  print 'Pleine forme'
elif IMC <= 25 :
  print 'Normal'
else:
  print 'Il va falloir faire un peu attention !!!'
    