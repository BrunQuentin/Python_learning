# -*-coding:Latin-1 -*


# 1. Cr�ation et �dition de dictionnaires

    #   1.1 Creer un dictionnaire
    
# Exemple 1 sur interpr�teur: Sur les dictionnaire vide

mon_dico = dict()
type(mon_dico)
# reponse de l'interpreteur:   <class 'dict'>
mon_dico
# reponse de l'interpreteur:   {}
# Du coup, vous devriez trouver la deuxi�me mani�re de cr�er un dictionnaire vide
mon_dico = {}
mon_dico
# reponse de l'interpreteur:   {}
#------------------------------------------------------------------------
# Exemple 2 sur interpr�teur: Sur les dictionnaire vide que l'on agrege
        ## ajouter des cl�s et valeurs dans notre dictionnaire vide
mon_dico_2 = {}
mon_dico_2["pseudo"] = "Prolixe"
mon_dico_2["mot de passe"] = "*"
mon_dico_2
# reponse de l'interpreteur:   {'mot de passe': '*', 'pseudo': 'Prolixe'}
#------------------------------------------------------------------------
# Exemple 3 sur interpr�teur: Sur le remplacement de valeurs dans les cl� dans les dico 
        ## remplacer ou creer un nouvelle objet du dico
mon_dico_3 = {}
mon_dico_3["pseudo"] = "Prolixe"
mon_dico_3["mot de passe"] = "*"
mon_dico_3["pseudo"] = "6pri1"
mon_dico_3
# reponse de l'interpreteur:   {'mot de passe': '*', 'pseudo': '6pri1'}

        ## Pour acc�der � la valeur d'une cl� pr�cise, c'est tr�s simple (voir ci-dessous)
mon_dico_3["mot de passe"]
# reponse de l'interpreteur: '*'
#------------------------------------------------------------------------
# Exemple 4 sur interpr�teur: Repr�sentation des dictionnaires
mon_dico_4 = {}
mon_dico_4[0] = "a"
mon_dico_4[1] = "e"
mon_dico_4[2] = "i"
mon_dico_4[3] = "o"
mon_dico_4[4] = "u"
mon_dico_4[5] = "y"
mon_dico_4
# reponse de l'interpreteur: {0: 'a', 1: 'e', 2: 'i', 3: 'o', 4: 'u', 5: 'y'}
#------------------------------------------------------------------------

    ## Exemple pratique sur un Echiquier
echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas � gauche de l'�chiquier
echiquier['b', 1] = "cavalier blanc" # � droite de la tour
echiquier['c', 1] = "fou blanc" # � droite du cavalier
echiquier['d', 1] = "reine blanche" # � droite du fou
# ... Premi�re ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, � droite du pion
# ... Seconde ligne des blancs
#------------------------------------------------------------------------
    ## On peut aussi cr�er des dictionnaires d�j� remplis 
def creer_dico_pre_rempli():
    placard = {"chemise":3, "pantalon":6, "tee-shirt":7}

    #------------------------------------------------------------------------
    # Supprimer des cl�s d'un dictionnaire
def supprimer_cle_dico():
    #Methode 1: avec del
    placard = {"chemise":3, "pantalon":6, "tee shirt":7}
    del placard["chemise"]    

    #M�thode 2: avec pop
    placard_2 = {"chemise":3, "pantalon":6, "tee shirt":7}
    placard_2.pop("chemise")
    # reponse de l'interpreteur: 3

    #------------------------------------------------------------------------
    # Un peu plus loin
def fete():
    print("c'est la f�te.")

def oiseau():
    print("Fais comme l'oiseau.")

# Notre dico 
fonctions = {}
fonctions["fete"] = fete
fonctions["oiseau"] = oiseau
#------------------------------------------------------------------------
# 2. Les m�thodes de parcours
    #   2.1 Parcours des cl�s
def parcours_cles():
    fruits = {"pommes":21, "melons":3, "poires":31}
    for cle in fruits:
        print(cle)
        
def parcours_cles_2():
    fruits = {"pommes":21, "melons":3, "poires":31}
    for cle in fruits.keys():
        print(cle)
        
    #   2.2 Parcours des valeurs
def parcours_valeurs():
    fruits = {"pommes":21, "melons":3, "poires":31}
    for cle in fruits.values():
        print(valeur)
    if 21 in fruits.values():
        print("Un des fruits se trouve dans la quantit� 21.")
        
    #   2.3 Parcours des cl�s et valeurs simulan�ment
def parcours_cles_valeurs():
    fruits = {"pommes":21, "melons":3, "poires":31}
    for cle, valeur in fruits.items():
         print("La cl� {} contient la valeur {}.".format(cle, valeur))
#------------------------------------------------------------------------
# 3. Les Dicos et parametres de fonction

    # 3.1 Recup�rer les params nomm�s dans un dico
    
def fct_inc(**parametres_nommes):
    """ Fonction permettant de voir comment r�cup�rer les param�tres nomm�s
    dans un dictionnaire."""

    print("J'ai re�u en param�tres nomm�s :{}.".format(parametres_nommes))

    # Exemple sur interpr�teur:
    #    >>> fonction_inconnue() # Aucun param�tre
    #    J'ai re�u en param�tres nomm�s : {}
    #    >>> fonction_inconnue(p=4, j=8)
    #   J'ai re�u en param�tres nomm�s : {'p': 4, 'j': 8}

def fct_inc_2(*en_liste, **en_dico):
    print("parametre x ou y")

    #------------------------------------------------------------------------

    # 3.2 Transformer un dictionnaire en param�tres nomm�s d'une fonction

    # Exemple 1 sur interpr�teur:
    #   >>> parametres = {"sep":" >> ", "end":" -\n"}
    #   >>> print("Voici", "un", "exemple", "d'appel", **parametres)
    #   Voici >> un >> exemple >> d'appel -

    # Exemple 2 sur interpr�teur:

    #   >>> print("Voici", "un", "exemple", "d'appel", sep=" >> ", end=" -\n")
    #   Voici >> un >> exemple >> d'appel -
