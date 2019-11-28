# -*-coding:Latin-1 -*

import os, sys

# tulpes partie 2
# sommaire

# 1.    Entre chaines & listes
    #   1.1 Des chaines aux listes

ma_chaine = "Bonjour � tous"
print(ma_chaine)
print("\n--- chaines => Listes ---\n")
print(ma_chaine.split(" "))
print("-------------------------")
    #   1.2 Des listes aux chaines
ma_liste = ['Bonjour', '�','tous']
print(ma_liste)
print("\n--- Listes => chaines  ---\n")
print(" ".join(ma_liste))
print("-------------------------")
    #   1.3 Une application pratique

def afficher_flottant(flottant):
    """Fonction prenant enparam�tre un flottant et renvoyant une chaine de
    caract�re repr�sentant la troncature de ce nombre. La partie flottante doit
    avoir un longueur maximum de 3 caract�res."""

    if type(flottant) is not float:
        raise TypeError("Le param�tre doit �tre un flottant")

    flottant = str(flottant)
    partie_entiere , partie_flottant = flottant.split(".")

    return ",".join([partie_entiere, partie_flottant[:3]])

# Exemple sur interpreteur:
#   afficher_flottant(3.999999999)
#   repr(afficher_flottant)
#   afficher_flottant(1.5)
#   repr(afficher_flottant)

#---------------------------------------------------

#   2.  Les listes et param�tres de fonctions

def fonction_inconnue(*parametres):
    """Test d'une fonction pouvant �tre appel�e avec uun nombre de variable de
    param�tres """

    print("j'ai rec�u : {}." .format(parametres))

# Exemple sur interpreteur:
#   >>> fonction_inconnue() # On appelle la fonction sans param�tre
#   J'ai re�u : ().
#   >>> fonction_inconnue(33)
#   J'ai re�u : (33,).
#   >>> fonction_inconnue('a', 'e', 'f')
#   J'ai re�u : ('a', 'e', 'f').
#   >>> var = 3.5
#   >>> fonction_inconnue(var, [4], "...")
#   J'ai re�u : (3.5, [4], '...').

def fonction_inconnue(nom, prenom, *commentaires):
    pass

#   <=> print(value, ..., sep=' ', end='\n', file=sys.stdout)
def print(*values, sep=' ', end='\n', file=sys.stdout):
    pass

#---------------------------------------------------

def afficher(*parametres, sep='', fin='\n'):
    """Fonction charg�e de reproduire le comportement de print.

    ELle doit finir par faire appel � print pour afficher le r�sultat.
    Mais les param�tres devront deja avoir �t� format�s.
    On doit passer � print une unique cha�ne, en lui sp�cifiant de ne
    rien mettre � la fin :

    print(chaine, end='')"""

    # parametres est un tuple donc impossible � modifier
    # en l'�tat actuel des choses.


    parametres = list(parametres)

    # maintenant parametres est une liste (qui est modifiable)
    # On va convertir toutes les valeurs en chaine sinon probleme
    # lors du join.

    for i, parametres in enumerate(parametres):
        parametres[i] = str(parametres)

    # Passons a la chaine finale

    chaine = sep.join(parametres)

    chaine += fin

    print(chaine, end='')
    print("-------------------------")

#---------------------------------------------------

    #   Transformer une liste en param�tres de fonction

#   liste_des_parametres = [1, 4, 9, 16, 25, 36]
#   print(*liste_des_parametres)
#   print("-------------------------")
# r�sultat attendu:   1 4 9 16 25 36
#---------------------------------------------------
#   3.  Les Comprehensions des liste
    #   1.  Parcours simple
#   liste_origine = [0, 1, 2, 3, 4, 5]
#   [nb * nb for nb in liste_origine]

# r�sultat attendu: [0, 1, 4, 9, 16, 25]
#   print("-------------------------")

    #   2.  Filtrage avec une branche conditionnel
#   liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   [nb for nb in liste_origine if nb % 2 == 0]

#   r�sultat attendu: [2, 4, 6, 8, 10]
#   print("-------------------------")

    #   3.Nouvelle application concr�te:  trier dans l'ordre decroissant
    
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
