# -*-coding:Latin-1 -*

# Fin  tulpes partie 2


#---------------------------------------------------

    # trier dans l'ordre decroissant
    
inventaire = [
     ("pommes", 22),
     ("melons", 4),
     ("poires", 18),
     ("fraises", 76),
     ("prunes", 51),
    ]

inventaire_decrois =  [ (qtt,fruits) for fruits,qtt in inventaire]

inventaire = [(fruits, qtt) for qtt,fruits in sorted(inventaire_decrois,\
                                                     reverse = True)]
print("\n",inventaire,"\n")

#----------------------------

inventaire_1 = [
     ("pommes", 22),
     ("melons", 4),
     ("poires", 18),
     ("fraises", 76),
     ("prunes", 51),
    ]

inventaire_inv = [ (qtt,fruits) for fruits,qtt in inventaire_1]

inventaire_inv.sort(reverse = True)

inventaire_1 = [(fruits, qtt)for qtt,fruits in inventaire_inv]

inventaire_1 = list(inventaire_1)
print(inventaire_1)
