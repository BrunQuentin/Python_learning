# -*-coding:Latin-1 -*

# liste et tuples partie 1

# I. Creation et Edition de nos listes
    # 1 creation de listes

    # exemple 1, liste vide :
    #           >>> ma_liste = list() <=> >>> ma_liste = [] 
    #           >>> type(ma_liste)
    #           <class 'list'>
    #           >>> ma_liste
    #           []

    # exemple 2,liste non vide:
    #       >>> ma_liste_1 = [1, 2, 3, 4, 5] # Une liste avec cinq objets
    #       >>> print(ma_liste_1)
    #       [1, 2, 3, 4, 5]

    # exemple 3,liste de ce qu'on veux:
    #       >>> ma_liste_2 = [1, 3.5, "une chaine", []]

    # Acces au element de la liste grace a leur indice (ici avec l'exemple 2)
    #       >>> ma_liste_1[0]
    #       1

    # Pour remplacer un élément faire :
    #       >>> ma_liste_1[2] = E
    #       >>> ma_liste_1
    #       [1, 2, E, 4, 5]
#---------------------------------------------
    # 2.Insérer des objets dans une liste

    ##  En fin de liste avec "append"
        
    #   >>> ma_liste_1 = [1, 2, 3, 4, 5]
    #   >>> ma_liste_1.append(48)
    #   >>> ma liste_1
    #   [1, 2, 3, 4, 5, 48]

    ## Insérer un éléments dans une liste
    
    #   >>> ma_liste = ['a', 'b', 'd', 'e']
    #   >>> ma_liste.insert(2, 'c') # On insère 'c' à l'indice 2
    #   >>> print(ma_liste)
    #   ['a', 'b', 'c', 'd', 'e']

    ## Concatenation de listes
    #   >>> ma_liste1 = [3, 4, 5]
    #   >>> ma_liste2 = [8, 9, 10]
    #   >>> ma_liste1.extend(ma_liste2) # On insère ma_liste2 à la fin de ma_liste1
    #   >>> print(ma_liste1)
    #   [3, 4, 5, 8, 9, 10]
    #   >>> ma_liste1 = [3, 4, 5]
    #   >>> ma_liste1 + ma_liste2
    #   [3, 4, 5, 8, 9, 10]
    #   >>> ma_liste1 += ma_liste2 # Identique à extend
    #   >>> print(ma_liste1)
    #   [3, 4, 5, 8, 9, 10]
#---------------------------------------------
    # 3.Suppression d'éléments d'une liste

        # On suprime avec "del" ou "remove"
        # del var_a_supprimer ou del liste[indice]
        # liste.remove(element)
#---------------------------------------------

# II. Le parcours de listes

ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0 # Notre indice pour la boucle while

while i < len(ma_liste):
    print(ma_liste[i])
    i += 1 # On incrémente i, ne pas oublier !

# <=>

for elt in ma_liste:
    # elt va prendre les valeurs successives des éléments de ma_liste
    print(elt)

    # 1. fonction enumerate

ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i, elt in enumerate(ma_liste):
    print("À l'indice {} se trouve {}.".format(i, elt))
    
#---------------------------------------------

# III. Un petit coup d'oeil aux tuples

tuple_vide = ()
tuple_non_vide = (1,) # est équivalent à ci dessous
tuple_non_vide = 1,
tuple_avec_plusieurs_valeurs = (1, 2, 5)

    # Affection multiple

a,b =3, 4 # où a= 3 et b= 4
(a,b)=(3,4) # est un equivalent en tuple

    # Une fonction renvoyant plusieurs valeurs
    
def decomposer(entier, divise_par):
    """Cette fonction retourne la partie entière et le reste de
    entier / divise_par"""

    p_e = entier // divise_par
    reste = entier % divise_par
    return p_e, reste

    #Compilation sur interpreteur

    #   >>> partie_entiere, reste = decomposer(20, 3)
    #   >>> partie_entiere
    #   6
    #   >>> reste
    #   2
    
#---------------------------------------------


    
        
    
    
