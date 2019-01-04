#--------------------------------------------------------------------------------------------------------------------------------------------
#   groupe9.py
#
#   Dec 04 2019 Initial (brought to me by Charlie)
#--------------------------------------------------------------------------------------------------------------------------------------------
import sys

#--------------------------------------------------------------------------------------------------------------------------------------------
def fabriquepaquet():
  paquet=[]
  lenvaleur = len(valeur)
  for i in range (lenenseigne) :
    for j in range (lenvaleur) :
      paquet.append((valeur[j],enseigne[i]))
  return paquet

#--------------------------------------------------------------------------------------------------------------------------------------------
def fisherYatesMelange(paquet):
  lenpaquet = len(paquet)
  import random
  for i in range (lenpaquet) :
    j = random.randint (0,i)
    (paquet[i],paquet[j])=(paquet[j],paquet[i])
  return paquet

#--------------------------------------------------------------------------------------------------------------------------------------------
def distribuer(N,J,paquet):
  joueurs =[]
  paquetmelange = paquet[:]
  paquetrestant = []
  taillepaquetmelange = len(paquetmelange)
  compt=0

  for i in range(J):
    joueurs.append([]) #initialise le nombre de joueurs
            
  for j in range (J) :
    for n in range (N) : #rempli les mains des joueurs
      joueurs[j].append(paquetmelange[compt])
      compt+=1
      for k in range (compt,taillepaquetmelange):
        paquetrestant.append(paquetmelange[k])
    return joueurs , paquetrestant

#--------------------------------------------------------------------------------------------------------------------------------------------
def InitialisePartie (N,J) :
  paquet = fabriquepaquet()
  paquetmelange = fisherYatesMelange(paquet)
  return distribuer(N,J,paquetmelange)


#--------------------------------------------------------------------------------------------------------------------------------------------
def bataille (indice,plateau,main) :
 
    cartesbataille = []
    for i in indice :
        if len(main[i])<=2 :
            plateau+=main[i]
            PositionDansIndice=indice.index(i)
            del indice[PositionDansIndice]
            del main[i]
            
    nbJtotal = len(main)
    nbJbataille = len(indice)
    
    for i in indice :
        plateau.append (main[i][0])
        del main[i][0]

    for i in range(nbJtotal):
        cartesbataille.append((0,0))
        
    for j in range (nbJtotal):
        for k in range (nbJbataille):
            if j == indice[k]:
              cartesbataille[j]=main[j][0]
              del main[j][0]

    cartegagnante = meilleurCarte(cartesbataille)
    gagnant = cartesbataille.index(cartegagnante)
    main[gagnant]+=plateau
      
    print("cartes batailles :", cartesbataille)
    return main

#--------------------------------------------------------------------------------------------------------------------------------------------
def jouerBataille(N,J):
       main,paquetRestant = InitialisePartie (N,J)



#-----------------------------------------------------------------------------------------------------------
# Just to be able to control the game flow interactively...
#-----------------------------------------------------------------------------------------------------------
def getString(prompt = "Enter a string please : ", mandatory = False) :
    while True:
        sys.stdout.write(prompt)
        line = sys.stdin.readline()
        if mandatory == True and len(line)==1 :
            print "Enter something please..."
        else : 
            break
    
    return line[:-1]
#--------------------------------------------------------------------------------------------------------------------------------------------
# Get the 1st card of each player on its stack (in the main array) and return it in the plateau
#--------------------------------------------------------------------------------------------------------------------------------------------
def tourdejeu (main) :

  plateau = []

  nbdejoueurs = len(main)    
  for i in range (nbdejoueurs):
    plateau.append (main[i][0])
    del main[i][0]

  print('plateau   : ', plateau)
  print('La main   : ', main)    
  return plateau,main
#--------------------------------------------------------------------------------------------------------------------------------------------
# Determines whon wins the tour
#--------------------------------------------------------------------------------------------------------------------------------------------
def meilleurCarte (liste) :
    taille = len(liste)
    position = [] #liste qui va contenir les rangs des valeurs des cartes
    for i in range (taille) : 
      for elmt in valeur :               
          if liste[i][0] == elmt :
            position.append(valeur.index(elmt))
            break   # Charlie, I added the break, no need to scan the full array once the card is identified

    indexmax = position.index(max(position))
    meilleurcarte = liste[indexmax]
    return meilleurcarte
#--------------------------------------------------------------------------------------------------------------------------------------------
# Play one tour
#--------------------------------------------------------------------------------------------------------------------------------------------
def testbataille(plateau,main) :
    indice = []
    nbdecarte = len(plateau)
    meilleurecarte = meilleurCarte(plateau)
    
    for i in range (nbdecarte) :
        if valeur.index(plateau[i][0]) == valeur.index(meilleurecarte[0]):
            indice.append(i)
            
    if len(indice) == 1 :
        main[indice[0]]+=plateau
    else :
        print("bataille : ")
        main = bataille(indice,plateau,main)
        
    return main
#--------------------------------------------------------------------------------------------------------------------------------------------
# Start here ;-)
#--------------------------------------------------------------------------------------------------------------------------------------------
Version = 'groupe9: Dec 04 2019, 1.08'

# Players
NomJoueur = ['Yves', 'Charles','Antoine','Margo']
# Players hands
main = [
    [('2','pique'),('3', 'carreau')],
    [('V', 'coeur'),('5', 'pique')],
    [('D', 'pique'),('7', 'coeur')],
    [('8', 'carreau'),('as', 'carreau')]
]

Final =[]
enseigne = ['pique','trefle','coeur','carreau']
valeur = ['2','3','4','5','6','7','8','9','10','V','D','R','as']

print Version
print 'Hello players, welcome'
for p in NomJoueur:
  print 'Player : ', p

while len(main[0])>1 :
    plateau, main = tourdejeu(main)
    print 'Still ', len(main), ' players in the game'
    plateau,main = testbataille(plateau,main)
    getString('<CR> for next tour please ', False)

#    Plateau,main = tourdejeu(main)
#    Plateau,main = testbataille(Plateau,main)
        