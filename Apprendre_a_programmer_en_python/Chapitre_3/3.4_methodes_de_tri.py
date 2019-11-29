#   Sommaire

#   1.  Première approche du tri
    #   1.1 Deux Méthodes
    #   1.2 Aperçu des critère de tri
#   2.  Trier avec des clés précises
    #   2.1 L'argument key
    #   2.2 Trier une listes d'objets
    #   2.3 Trier dans le sens inverse

#   3.  Tri + rapide + efficace
    #   3.1.  Les fonctions du module operator
        #   3.1.1   Trier une listes de tuples
        #   3.1.2   Trier une listes d'objets
        
    #   3.2.  Trier selon plusieurs critères
        # 3.2.1   Chaînage de tris

#---------------------------------------------------#

    # 1.1   Deux methodes

    # => liste.sort() => methode sort de la class list.
    #                   Tri la liste en ecrasant la liste actuel

    # sorted(liste) => fonction builtin disponible dans Python ;
    #               Tri la liste dans une autre liste et garde la liste d'origine intact.

#---------------------------------------------------#

    #   1.2

tri_1 =sorted([1, 8, -2, 15, 9])
print("Tri d'une liste d'entiers :  {} \n ".format(tri_1))
tri_2= sorted(["1", "8", "-2", "15", "9"])
print("Tri d'une chaine de characteres :  {} \n".format(tri_2))


    # Quand une liste comporte plusieurs type => Impossible à trier


#---------------------------------------------------#
#   2.
    
eleves = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]
tri_eleves = sorted(eleves)
print("---- Tri avec des clés precises ---- \n  {} \n ".format(tri_eleves))



    #   2.1 "key"
tri_eleves_2 =sorted(eleves, key=lambda colonnes: colonnes[2])
print("---- Tri avec argument 'key' ---- \n {}\n ".format(tri_eleves_2))
    #---------------------------------------------------#
    #   2.2

class Eleves:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={}) \n>".format(
                self.prenom, self.age, self.moyenne)

eleves = [
    Eleves("Clément", 14, 16),
    Eleves("Charles", 12, 15),
    Eleves("Oriane", 14, 18),
    Eleves("Thomas", 11, 12),
    Eleves("Damien", 12, 15),
]

print("---- Liste d'eléves initial ---- \n {} \n".format(eleves))
tri_eleves_listes = sorted(eleves, key=lambda eleve: eleve.moyenne)
print("---- Tri d'une liste d'eléves ---- \n {} \n ".format(tri_eleves_listes))

    # 2.3 Tri inversé

tri_eleves_listes_inv = sorted(eleves, key=lambda eleve: eleve.age, reverse=True)
print("---- Tri d'une liste sur l'age des eléves inversé (decroissant) ---- \n {} \n ".format(tri_eleves_listes_inv))


#---------------------------------------------------#
        #   3.1.1   Trier une listes de tuples
etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 13, 15),
]
print("-----Liste de départ ---")
print(etudiants)
print("-----Tri Moyenne (tuples)---")
etudiants_triee_tuples= sorted(etudiants, key=lambda etudiant: etudiant[1])
print(etudiants_triee_tuples)

# Autre methode qui fait le meme chose que "sorted" 
#   from operator import itemgetter
#   sorted(etudiants, key=itemgetter(2))
print("---------------------------\n")


#---------------------------------------------------#
        #   3.1.2   Trier une listes d'objets

class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})\n>".format(
                self.prenom, self.age, self.moyenne)
etudiants_v2 = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 13, 15),
]

print("-----Liste de départ ---")
print(etudiants_v2)
print("-----Tri Moyenne (listes)---")
from operator import attrgetter
etudiants_triee_listes = sorted(etudiants_v2, key=attrgetter("moyenne"))
print(etudiants_triee_listes)
print("---------------------------\n")

#---------------------------------------------------#
   #    3.2 Trier selon plusieurs critères
etudiants_sorted = sorted(etudiants_v2, key=attrgetter("age", "moyenne"))
print(etudiants_sorted)
print("---------------------------\n")
        #   3.2.1 Chainage de tri
        
class LigneInventaire:

    """Classe représentant une ligne d'un inventaire de vente.

    Attributs attendus par le constructeur :
        produit -- le nom du produit
        prix -- le prix unitaire du produit
        quantite -- la quantité vendue du produit.

    """

    def __init__(self, produit, prix, quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite

    def __repr__(self):
        return "<Ligne d'inventaire {} ({}X{}) \n>".format(
                self.produit, self.prix, self.quantite)

# Création de l'inventaire
inventaire = [
    LigneInventaire("pomme rouge", 1.2, 19),
    LigneInventaire("orange", 1.4, 24),
    LigneInventaire("banane", 0.9, 21),
    LigneInventaire("poire", 1.2, 24),
]

from operator import attrgetter
inventaire_trier= sorted(inventaire, key=attrgetter("prix", "quantite"))
print(inventaire_trier)
