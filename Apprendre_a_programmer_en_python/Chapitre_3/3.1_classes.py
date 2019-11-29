#                       SOMMAIRE   : Les classes          #
#   1.  Nos premiers attributs
    #   1.1Quand on crée notre objet…
    
#   2.  Les méthodes , la recette
    #   2.1 Paramètre self
    #   2.2 Methodes de classe / Méthodes statiques

#   3.  Un peu d'intospection
    #   3.1 fonction dir
    #   3.2 attribut special __dict__
#---------------------------------------------------------#

class Personne: # Définition de notre classe Personne (1.)
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son âge
    - son lieu de résidence"""

    
    def __init__(self): # Notre méthode constructeur (1.)
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.nom = "Dupont"

        self.prenom = "Jean" # Quelle originalité
        self.age = 33 # Cela n'engage à rien
        self.lieu_residence = "Paris"
        
# Test sur notre attributs

jean = Personne()
print("\n-- Test avec un attribut --")
print("Etudions la classe Personne : \n {} ".format(jean))
print("Mon nom est  : \n {} ".format(jean.nom))
print("\n-- Test avec plusieurs attributs (prenom, age, lieu de residence)--")
print("Mon prenom est  : \n {} ".format(jean.prenom))
print("Mon age est de : \n  {} ans ".format(jean.age))
print("J'habite actuelement à : \n {} ".format(jean.lieu_residence))
demenage = jean.lieu_de_residence = "Berlin"
print("Je démenage vers  : \n {} ".format(demenage))

print("-- Fin de test des attributs-- \n")
    #------------------------------#
class CompteurDObjet:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    
    objets_crees = 0 # Le compteur vaut 0 au départ
    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        CompteurDObjet.objets_crees += 1

comptage = CompteurDObjet.objets_crees
print(comptage)     # => 0

a = CompteurDObjet()
comptage_1 = CompteurDObjet.objets_crees
print(comptage_1)   # => 1

b = CompteurDObjet()

comptage_2 = CompteurDObjet.objets_crees
print(comptage_2)   # => 2
print("-- Fin de test des attributs de classe CompteurDObjet -- \n")
#---------------------------------------------------------#
#   2. Les méthodes
class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer, par jeu de méthodes. L'attribut modifié
    est 'surface'"""

    
    def __init__(self): # Present dans 2. 
        """Par défaut, notre surface est vide"""
        self.surface = ""
    def ecrire(self, message_a_ecrire): # Present dans 2.
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    # Ajout de la methode lire: present dans 2.1 " param self "
    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        la surface du tableau"""

        print(self.surface)

    # Ajout de la methode effacer : present dans 2.1 " param self "    
    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""

# Tests sur la classe TableauNoir

#   tab = TableauNoir()
#   tab.surface
#   tab.ecrire("Coooool ! Ce sont les vacances !")
#   tab.surface

    #   2.1 Paramètre self
# Tests sur la classe TableauNoir avec self
#   print("--Fin Test classe TableauNoir --"
#   tab.ecrire
#   TableauNoir.ecrire
#   help(TableauNoir.ecrire)
#   TableauNoir.ecrire(tab, "essai")
#   tab.surface

    #   2.2 Methodes de classe / Méthodes statiques
# Methode de classe 
class Compteur: 
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on crée un objet de ce type"""

    
    objets_crees = 0 # Le compteur vaut 0 au départ
    def __init__(self):
        """À chaque fois qu'on crée un objet, on incrémente le compteur"""
        Compteur.objets_crees += 1
    def combien(cls):
        """Méthode de classe affichant combien d'objets ont été créés"""
        print("Jusqu'à présent, {} objets ont été créés.".format(
                cls.objets_crees))
    combien = classmethod(combien)


class MethodeStatique: # Methode statique
    """Une classe de test tout simplement"""
    def afficher():
        """Fonction chargée d'afficher quelque chose"""
        print("On affiche la même chose.")
        print("peu importe les données de l'objet ou de la classe.")
    afficher = staticmethod(afficher)

#--------------------------------------------------------#

    #   3.1 'dir'
class Test:
    """Une classe de test tout simplement"""
    def __init__(self):
        """On définit dans le constructeur un unique attribut"""
        self.mon_attribut = "ok"
    
    def afficher_attribut(self):
        """Méthode affichant l'attribut 'mon_attribut'"""
        print("Mon attribut est {0}.".format(self.mon_attribut))

# Créons un objet de la classe Test
un_test = Test()    
# On appelle la methode 'afficher_attribut' de la classe Test
un_test.afficher_attribut()

# Pour afficher la liste d'attribut de la classe
# on doit la sauvegarder dans une variable puis l'afficher avec 'print()'
liste_attr =dir(un_test)    
print(liste_attr)

    #   3.2 '__dict__'
print("---------------------")
dico= un_test.__dict__
print(dico)

# On va modifier la valeur de l'attibut
print("----Changer la valeur de l'attribut-------")
dico["mon_attribut"] = "plus ok"
un_test.afficher_attribut()

