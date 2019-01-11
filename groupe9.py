#--------------------------------------------------------------------------------------------------------------------------------------------
#   groupe9.py
#
#   Dec 04 2019 Initial (brought to me by Charlie)
#   Dec 11 2019 Test number of players remaining and finish the game
#--------------------------------------------------------------------------------------------------------------------------------------------
import sys
import random

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
    print meilleurecarte[0], ' ', meilleurecarte[1], ' Wins'

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
# Dump players and cards
#--------------------------------------------------------------------------------------------------------------------------------------------
def lookatplayers(players, cards):
    print '\n ========== P L A Y E R S ===============\n'
    for p in players:
        playerindex =  players.index(p)
        playercards = cards[playerindex]
        print 'Player : ',p, ' [', len(playercards), ']'
        for card in playercards:
            print '\t\t\t\t', card
    print
#--------------------------------------------------------------------------------------------------------------------------------------------
# Remove players with no more cards
#--------------------------------------------------------------------------------------------------------------------------------------------
def shootloosers(main) :
    while True:
        found = False
        for i in range(0, len(main)-1):
            if not main[i]:
                del main[i]
                print NomJoueurs[i], ' has lost'
                del NomJoueurs[i]
                found = True
        if not found:
            break

    return main


#--------------------------------------------------------------------------------------------------------------------------------------------
# Get a card set
#--------------------------------------------------------------------------------------------------------------------------------------------
def fabriquepaquet():
  paquet=[]
  lenvaleur = len(valeur)
  for i in range(len(couleurs)) :
    for j in range (lenvaleur) :
      paquet.append((valeur[j],couleurs[i]))
  return paquet

#--------------------------------------------------------------------------------------------------------------------------------------------
# Mix the card set 
#--------------------------------------------------------------------------------------------------------------------------------------------
def fisherYatesMelange(paquet):
  lenpaquet = len(paquet)
  for i in range (lenpaquet) :
    j = random.randint (0,i)
    (paquet[i],paquet[j])=(paquet[j],paquet[i])
  return paquet

#--------------------------------------------------------------------------------------------------------------------------------------------
# Distribute cards to N players
#--------------------------------------------------------------------------------------------------------------------------------------------
def distribuer(nbcartes,nbjoueurs,paquet):
    joueurs =[]
    paquetmelange = paquet[:]
    paquetrestant = []
    taillepaquetmelange = len(paquetmelange)

    for i in range(nbjoueurs):
        joueurs.append([]) # initialise le tableau recevant les cartes des joueurs
                
    for n in range (nbcartes) : # rempli les mains des joueurs
        for j in range (nbjoueurs) :
            joueurs[j].append(paquetmelange[0])
            del paquetmelange[0]

    return joueurs, paquetmelange

#--------------------------------------------------------------------------------------------------------------------------------------------
# Start here ;-)
#--------------------------------------------------------------------------------------------------------------------------------------------
Version = 'groupe9: Dec 11 2019, 1.45'

# Cards
couleurs = ['pique','trefle','coeur','carreau']
valeur = ['2','3','4','5','6','7','8','9','10','V','D','R','AS']
paquet = fabriquepaquet()
paquetmelange = fisherYatesMelange(paquet)
pioche = []

# Players
NomJoueurs = ['Margote', 'Yves', 'Charles' ]
NBCARDSFORPLAYERS = 3
cardsJoueurs, pioche = distribuer(NBCARDSFORPLAYERS, len(NomJoueurs), paquetmelange)

# Players hands
# Initializing this array is no longer necessary as we'll fill it 
# by calling InitialisePartie()
dummymain = [
    [('2','pique'),('3', 'carreau')],
    [('V', 'coeur'),('5', 'pique')],
    [('D', 'pique'),('7', 'coeur')]
]

# Some welcome message before starting the fight !!!
print '\n\n', Version

lookatplayers(NomJoueurs, cardsJoueurs)
getString('\n\nStart game <CR>', False)

# Now start serious things
while len(cardsJoueurs[0])>=1 :
    plateau, cardsJoueurs = tourdejeu(cardsJoueurs)                     # Put cards on the table
    print len(cardsJoueurs), ' players still in the game'   
    cardsJoueurs = testbataille(plateau,cardsJoueurs)                   # Play
    cardsJoueurs = shootloosers(cardsJoueurs)                           # Are there any looser ? Yes remove them from the game
    if len(NomJoueurs) > 1:
        lookatplayers(NomJoueurs, cardsJoueurs)
        getString('Next tour <CR>', False)
    else:
        print NomJoueurs[0], ' wins !!!!!!!!!'
        sys.exit(0)

        