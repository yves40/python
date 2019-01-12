#--------------------------------------------------------------------------------------------------------------------------------------------
#   groupe9.py
#
#   Dec 04 2019 Initial (brought to me by Charlie)
#   Dec 11 2019 Test number of players remaining and finish the game
#   Dec 12 2019 Fix bug when looser is in the last position of the list
#               Improve the core gaming algorithm, manage the 'bataille'
#--------------------------------------------------------------------------------------------------------------------------------------------
import sys
import random

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
# Determines whon wins the tour
#--------------------------------------------------------------------------------------------------------------------------------------------
def meilleurCarte (liste) :
    taille = len(liste)
    position = [] #liste qui va contenir les rangs des valeurs des cartes
    for i in range (taille) : 
      for elmt in _VALEURS :               
          if liste[i][0] == elmt :
            position.append(_VALEURS.index(elmt))
            break   # Charlie, I added the break, no need to scan the full array once the card is identified

    indexmax = position.index(max(position))
    meilleurcarte = liste[indexmax]
    return meilleurcarte
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
def shootloosers(playercards) :
    while True:
        found = False
        for i in range(len(playercards)):
            if not playercards[i]:
                del playercards[i]
                print _NOMJOUEURS[i], ' has lost'
                del _NOMJOUEURS[i]
                found = True
                break               # One looser found, recheck
        if not found:
            break

    return playercards


#--------------------------------------------------------------------------------------------------------------------------------------------
# Get a card set
#--------------------------------------------------------------------------------------------------------------------------------------------
def fabriquepaquet():
  paquet=[]
  lenvaleur = len(_VALEURS)
  for i in range(len(_COULEURS)) :
    for j in range (lenvaleur) :
      paquet.append((_VALEURS[j],_COULEURS[i]))
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
#   Should be DELETED
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
      
    return main

#--------------------------------------------------------------------------------------------------------------------------------------------
# Get the 1st card of each player on its stack (in the cards array) and return it in the plateau
#--------------------------------------------------------------------------------------------------------------------------------------------
def getPlateau(cards):
  plateau = []

  for i in range (len(cards)):
    plateau.append (cards[i][0])
    del cards[i][0]

  return plateau,cards
#--------------------------------------------------------------------------------------------------------------------------------------------
# Play one tour. Can be called in recursive manner if a bataille occurs
#--------------------------------------------------------------------------------------------------------------------------------------------
def playTour(cards):

    plateau, cards = getPlateau(cards)    
    plateauwinners = []
    sotckcard = []
    # Search for the winner index
    while len(plateauwinners) != 1:
        plateauwinners = []
        for p in range(len(plateau)):
            sotckcard.append(plateau[p])
        meilleurecarte = meilleurCarte(plateau)
        # Once the best card is known, check if there's only one
        for i in range (len(plateau)) :        
            if _VALEURS.index(plateau[i][0]) == _VALEURS.index(meilleurecarte[0]):
                plateauwinners.append(i)
        if len(plateauwinners) > 1: # bataille ? 
            # Skip one card for each competing player (turned back in real game)
            for w in range(len(plateauwinners)):
                sotckcard.append(cards[plateauwinners[w]][0])     
                del cards[plateauwinners[w]][0]     
            # Now get the playing card for each player
            plateau = []
            for w in range(len(plateauwinners)):
                plateau.append(cards[plateauwinners[w]][0])     
                del cards[plateauwinners[w]][0]  

            
    cards[plateauwinners[0]]+=sotckcard
    return cards        
#--------------------------------------------------------------------------------------------------------------------------------------------
#   Start here ;-)
#   Global variables are uppercase and prefixed with an '_'
#--------------------------------------------------------------------------------------------------------------------------------------------
Version = 'groupe9: Dec 12 2019, 1.64'

# Cards
_COULEURS = ['pique','trefle','coeur','carreau']
_VALEURS = ['2','3','4','5','6','7','8','9','10','V','D','R','AS']
_PAQUET = fabriquepaquet()
_PAQUETMELANGE = fisherYatesMelange(_PAQUET)
_PIOCHE = []

# Players
_NOMJOUEURS = ['Margote', 'Yves', 'Charles' ]
_NBCARDSFORPLAYERS = 3
_CARDSJOUEURS, _PIOCHE = distribuer(_NBCARDSFORPLAYERS, len(_NOMJOUEURS), _PAQUETMELANGE)

# Players hands
# Initializing this array is no longer necessary as we'll fill it 
# by calling InitialisePartie()
_CARDSJOUEURS = [
    [('V','pique'),('9', 'carreau'),('8', 'carreau')],
    [('V', 'coeur'),('5', 'pique'),('7', 'carreau')],
    [('9', 'pique'),('7', 'coeur'),('6', 'carreau')]
]

# Some welcome message before starting the fight !!!
print '\n\n', Version
lookatplayers(_NOMJOUEURS, _CARDSJOUEURS)     # Who plays, whith which cards
getString('\n\nStart game <CR>', False)
#--------------------------------------------------------------------------------------------------------------------------------------------
# Game loop 
#--------------------------------------------------------------------------------------------------------------------------------------------
while len(_CARDSJOUEURS[0])>=1 :
    _CARDSJOUEURS = playTour(_CARDSJOUEURS)         # Play
    _CARDSJOUEURS = shootloosers(_CARDSJOUEURS)     # Are there any looser ? Yes remove them from the game
    if len(_NOMJOUEURS) > 1:
        lookatplayers(_NOMJOUEURS, _CARDSJOUEURS)
        getString('Next tour <CR>', False)
    else:
        print _NOMJOUEURS[0], ' wins !!!!!!!!!'
        sys.exit()

        