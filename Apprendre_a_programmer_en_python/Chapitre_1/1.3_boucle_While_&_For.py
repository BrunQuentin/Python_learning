# -*-coding:Latin-1 -*

#Boucle while ( table de multiplication automatisé)

table_multi = input("quel table de multiplication voulez vous connaitre : ")
table_multi = int(table_multi)


nb = 0 # compteur de variable pour incrémenter dans la boucle

while nb <10: # tant que nb est strictement inferieur à 10
    print(nb +1, "*", table_multi, "=", (nb +1)* table_multi)
    nb += 1 # on incrémente nb à chaque ittération
print("\n")
        
#Boucle for // boucle infinie // break 

chaine = input("Saisissez votre message : ")
for lettre in chaine:
    #if lettre in "AEIOUYaeiouy": # lettre est une voyelle
        print(lettre)
    #else: # lettre est une consonne... ou plus exactement, lettre n'est pas une voyelle
     #   print("*")
print("\n")
#----------------


while 1:
    lettre = input("Tapez 'Q' pour  quitter : ")
    if lettre == 'Q':
        print("Fin de boucle")
        break
    
print("\n")
#-----------------

valeur = 1

while valeur <20:
    if valeur %3 == 0:  # si la valeur est multiple de 3
        valeur += 4     # on ajoute 4 à la valeur
        print("On incrémente de 4, la valeur est égale à :",valeur)
        continue # On retourne au while sans executer les autres lignes
    print("La variable valeur =",valeur)
    valeur += 1     # Dans le cas classique on ajoute 1 à valeur
