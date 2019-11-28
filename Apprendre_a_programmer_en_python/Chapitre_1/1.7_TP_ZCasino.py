# -*-coding:Latin-1 -*


# importation necessaire
import os
from random import randrange
from math import ceil

# D�claration des variable de d�part
monnaie = -1
jouer_partie = True
 
while monnaie == -1:
    
    monnaie = input("Avec combien d'argent voulez vous commencer ? :" )
    try:
        monnaie = int(monnaie)
    except ValueError:
        print("Vous n'avez pas saisi combien vous voulez de $ pour jouer \n")
        monnaie = -1
        continue
    if monnaie <= 0:
            print("Vous avez entrer une mise n�gative ou nulle \n ") 
   


print("\n\nBienvenue au ZCasino! Il y a une place de libre � la roulette. Ca vous tente ?\n\n\n ")

while jouer_partie:
    numero = -1
    while numero < 0 or numero >49:
        numero = input("Veuillez indiquer le numero dont vous souhaitez miser (entre 0 et 49) :\n")

        #on converti la chaine en nombre
        try:
            numero = int(numero)
        except ValueError:
            print("Vous n'avez pas saisi de numero \n")
            numero = -1
            continue
        if numero < 0:
            print(" Le numero entr� est n�gatif \n")
        if numero > 49:
            print(" Le numero depasse la limite autoros� fix� a 49 \n")

# Selection de la somme a miser
    mise = 0
    while mise <= 0 or mise > monnaie:
        mise = input("\n\nVeuillez placer une mise sur le numero choisi :\n")

        # on converti la chaine en nombre
        try:
            mise =  int(mise)
        except ValueError:
            print("Vous n'avez pas miser \n ")
        if mise <= 0:
            print("Vous avez entrer une mise n�gative ou nulle \n ")
        if mise > monnaie:
            print ("Vous ne pouvez pas mis� plus que ce que vous avez", monnaie, "$ \n")
    
    print(" \n\nLe numero et sa mise ont �t� enregistrer par le croupier. Les jeux sont fais \n")
    numero_gagnant =randrange(50)
    print(" \n Que l'on fasse tourn�e la roue ...  elle s'arrete sur le num�ro", numero_gagnant)
    

# La grille des gains

    if numero_gagnant == numero:
        print("\n F�licitation : vous avez gagner", mise * 3, "$")
        monnaie += mise *3
    elif numero_gagnant %2 == numero % 2: # Si il sont en plus de la m�me couleur
        mise = ceil(mise * 0.5)
        print("Vous avez mis� la bonne couleur,. Vous obtener",mise,"$")
        monnaie += mise
    else:
        print("D�sol�, ce n'est pas votre jour de chance. Vous perdez votre mise.")
        monnaie -= mise

# Si le joueur n'as plus d'argent
    if monnaie <= 0:
        print("Vous �tes ruin� ! Veuillez quitter le ZCasino.")
        continuer_partie = False
    else:
        # Affiche l'argent du joueur
        print("Vous avez desormais",monnaie,"$")
        quitter = input("Soutaitez-vous partie du ZCasino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            continuer_partie = False
    
os.system("pause")
