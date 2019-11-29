# Sommaire

# 1.    Retour sur le processus d'instanciation
    #   1.1 la methode __new__
    
# 2.    Créer une classe dynammiquement
    #   2.1 Methodes connus
    #   2.2 Créer une classe dynamiquement
# 3.    Définition d'une métaclasse
    #   3.1 la methode __new__
    #   3.2 la methode __init__
    #   3.3 metaclasses en action

#--------------------------------------------
# 1.
class Personne:
    
    """Classe définissant une personne.
    
    Elle possède comme attributs :
    nom -- le nom de la personne
    prenom -- son prénom
    age -- son âge
    lieu_residence -- son lieu de résidence
    
    Le nom et le prénom doivent être passés au constructeur."""

    #   1.1
    def __new__(cls, nom, prenom):
        print("Appel de la méthode __new__ de la classe {}".format(cls))
        # On laisse le travail à object

        # cela marche pour une version anterieur a 3.4
       #return object.__new__(cls, nom, prenom) 
        return object.__new__(cls) # s'ecrit mtn comme ceci
    
    def __init__(self, nom, prenom):
        """Constructeur de notre personne."""
        print("Appel de la méthode __init__")
        self.nom = nom
        self.prenom = prenom
        self.age = 23
        self.lieu_residence = "Lyon"

personne = Personne("Doe", "John")

#--------------------------------------------------#
    # 2.1
class MaClasse:
    print("\n")
    print(type(5))
    print("une chaîne")
    print([1,2,3])
#   type(str)   # resultat: <class 'type'> 
#   type(int)   # resultat: <class 'type'>
#   type(list)  # resultat: <class 'type'>


    #2.2
print("----Classe a Créeer----\n")
Personne = type("Personne", (), {})
print(Personne)
print("----------------\n")
john = Personne()
print(john)
print("------dictionnaire des attributs -----\n")
print(dir(john))

print("\n")


def creer_personne(personne, nom, prenom):
    """La fonction qui jouera le rôle de constructeur pour notre classe Personne.
    
    Elle prend en paramètre, outre la personne :
    nom -- son nom
    prenom -- son prenom"""
    
    personne.nom = nom
    personne.prenom = prenom
    personne.age = 21
    personne.lieu_residence = "Lyon"

def presenter_personne(personne):
    """Fonction présentant la personne.
    
    Elle affiche son prénom et son nom"""
    
    print("{} {}".format(personne.prenom, personne.nom))

# Dictionnaire des méthodes
methodes = {
    "__init__": creer_personne,
    "presenter": presenter_personne,
}

# Création dynamique de la classe
Personne = type("Personne", (), methodes)

    #----------------------------------#

# Execution du programme pour presenter une personne
print("----------------")
jack = Personne("Ryan","Jack")
print("Mon nom est {} ".format(jack.nom))
print("Mon prenom est {}".format(jack.prenom))
print("Mon age est {}".format(jack.age))
jack.presenter()


#--------------------------------------------------

#   3.1  

class MaMetaClasse(type):
    
    """Exemple d'une métaclasse."""
    
    def __new__(metacls, nom, bases, dict):
        """Création de notre classe """
        print("----------------")
        print("On crée la classe {} grâce à une métaclasse.".format(nom))
        return type.__new__(metacls, nom, bases, dict)

    #----------------------------------#
#   3.2
    

class MaClasses(metaclass=MaMetaClasse):

    def __init__(self,nom,prenom):
        
        """Initialisation de notre classe """
        self.nom = nom
        self.prenom = prenom
        print("----------------")
        print("On initialise la classe avec son nom: {} et son prenom: {} grâce à sa métaclasse.".format(nom,prenom))

    #----------------------------------#
    # Objectif
#   {
#       "Widget": Widget,
#       "Bouton": Bouton,
#       "CaseACocher": CaseACocher,
#       "Menu": Menu,
#       "Cadre": Cadre,
#   }
        
trace_classes = {} # Notre dictionnaire vide

class MetaWidget(type):
    
    """Notre métaclasse pour nos Widgets.
    
    Elle hérite de type, puisque c'est une métaclasse.
    Elle va écrire dans le dictionnaire trace_classes à chaque fois
    qu'une classe sera créée, utilisant cette métaclasse naturellement."""
    
    def __init__(cls, nom, bases, dict):
        """Constructeur de notre métaclasse, appelé quand on crée une classe."""
        type.__init__(cls, nom, bases, dict)
        trace_classes[nom] = cls

class Widget(metaclass=MetaWidget):
    
    """Classe mère de tous nos widgets."""
    
    pass

class Bouton(Widget):
    
    """Une classe définissant le widget bouton."""
    
    pass

class CaseACocher(Widget):
    
    """Une classe définissant le widget case à cocher."""
    
    pass

class Menu(Widget):
    
    """Une classe définissant le widget menu."""
    
    pass

class Cadre(Widget):
    
    """Une classe définissant le widget cadre."""

    pass

print("Voici le dictionnaire de Widget: \n {} ".format(trace_classes))





