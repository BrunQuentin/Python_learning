#           SOMMAIRE   : Les methodes spéciales                         #

#   1.  Edition de l'objet et accès aux attributs
    #   1.1 Edition
    #   1.2 Représentation
    #   1.3 Acces aux attributs:
        #   __getattr__
        #   __setattr__
        #   __detattr__
        #   bonus
    
#   2.  Les méthodes de conteneurs
    #   2.1 Accès aux éléments d'un conteneur
    #   2.2 La méthode spéciale derrière le mot-clé in
    #   2.3 Connaître la taille d'un conteneur

#   3.  Les méthodes mathématiques
    #   3.1 Ce qui faut savoir
    #   3.2 Tout dépend du sens
    #   3.3 D'autres opérateurs
    
#   4.  Les méthodes de comparaison

#   5.  Des méthodes spéciales utile à pickle
#---------------------------------------------------------#
    # 1.1   Edition
class Exemple:
    """Un petit exemple de classe"""
    def __init__(self, nom):
        """Exemple de constructeur"""
        self.nom = nom
        self.autre_attribut = "une valeur"
        
    def __del__(self):
        """Méthode appelée quand l'objet est supprimé"""
        print("C'est la fin ! On me supprime !")

mon_objet = Exemple("un premier exemple")

    # 1.2   Representation
class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
    def __repr__(self):
        """Quand on entre notre objet dans l'interpréteur"""
        return "Personne: nom({}), prénom({}), âge({})".format(
                self.nom, self.prenom, self.age)
    def __str__(self):
        """Méthode permettant d'afficher plus joliment notre objet"""
        return "{} {}, âgé de {} ans".format(
                self.prenom, self.nom, self.age)


# Test sur la représentation des objets avec __repr__(object) ( sur console)
print("  Debut test sur __repr__\n")
p1 = Personne("Ryan", "Jack")
print(" Appel de __repr__ depuis la classe Personne : ")
print(p1)
print("\n Appel de __repr__ directement sur l'objet test 'p1' : ")
print(repr(p1))
print("  Fin   test sur __repr__\n")

# Test sur la représentation des objets avec __repr__(object) ( sur console)
print("  Debut test sur __str__\n")
print(p1)
chaine = str(p1)
print(chaine)
print("  Fin   test sur __str__\n")

    #---------------------------------------------------------#
    # 1.3   Acces aux attributs : __getattr__ , setattr__ , __delattr__

class Protege:
    """Classe possédant une méthode particulière d'accès à ses attributs :
    Si l'attribut n'est pas trouvé, on affiche une alerte et renvoie None"""

     
    def __init__(self):
        """On crée quelques attributs par défaut"""
        self.a = 1
        self.b = 2
        self.c = 3
        
    def __getattr__(self, nom):
        """Si Python ne trouve pas l'attribut nommé nom, il appelle
        cette méthode. On affiche une alerte"""

        print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

    def __setattr__(self, nom_attr, val_attr):
        """Méthode appelée quand on fait objet.nom_attr = val_attr.
        On se charge d'enregistrer l'objet"""
        
        
        object.__setattr__(self, nom_attr, val_attr)
        self.enregistrer()

    def __delattr__(self, nom_attr):
        """On ne peut supprimer d'attribut, on lève l'exception
        AttributeError"""
        
        raise AttributeError("Vous ne pouvez supprimer aucun attribut de cette classe")

#   objet = MaClasse() # On crée une instance de notre classe
#   getattr(objet, "nom") # Semblable à objet.nom
#   setattr(objet, "nom", val) # = objet.nom = val ou objet.__setattr__("nom", val)
#   delattr(objet, "nom") # = del objet.nom ou objet.__delattr__("nom")
#   hasattr(objet, "nom") # Renvoie True si l'attribut "nom" existe, False sinon
    
# Test sur l'acces aux attriburs de nos objets ( sur console)

#   pro = Protege()
#   print(pro.a)
#   print(pro.c)
#   print(pro.e) # annoncera une erreur
#   print(" Fin test __getattr__ ")

#---------------------------------------------------------#
#   2.    Les méthodes de conteneurs
    # 2.1
class ZDict:
    """Classe enveloppe d'un dictionnaire"""
    def __init__(self):
        """Notre classe n'accepte aucun paramètre"""
        self._dictionnaire = {}
    def __getitem__(self, index):
        """Cette méthode spéciale est appelée quand on fait objet[index]
        Elle redirige vers self._dictionnaire[index]"""
        
        return self._dictionnaire[index]
    def __setitem__(self, index, valeur):
        """Cette méthode est appelée quand on écrit objet[index] = valeur
        On redirige vers self._dictionnaire[index] = valeur"""
        
        self._dictionnaire[index] = valeur

    # 2.2 Test sur la méthode spéciale derrière 'in'
ma_liste = [1, 2, 3, 4, 5]
8 in ma_liste # Revient au même que ...
contient =ma_liste.__contains__(8)
print(contient)

    # 2.3 Connaitre la taille d'un conterneur

    #   La methode __len__ permet de donner la taille d'un objet conteneur
    #   syntaxe: len(objet) <=> objet.__len__()

#---------------------------------------------------------#
    # 3.    Méthode mathématiques
    
class Duree:
    """Classe contenant des durées sous la forme d'un nombre de minutes
    et de secondes"""
    
    def __init__(self, min=0, sec=0):
        """Constructeur de la classe"""
        self.min = min # Nombre de minutes
        self.sec = sec # Nombre de secondes
    
    def __str__(self):
        """Affichage un peu plus joli de nos objets"""
        return "{0:02}:{1:02}".format(self.min, self.sec)
    #----------------------------------------------------------------#
    def __add__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        nouvelle_duree = Duree()
        # On va copier self dans l'objet créé pour avoir la même durée
        nouvelle_duree.min = self.min
        nouvelle_duree.sec = self.sec
        # On ajoute la durée
        nouvelle_duree.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if nouvelle_duree.sec >= 60:
            nouvelle_duree.min += nouvelle_duree.sec // 60
            nouvelle_duree.sec = nouvelle_duree.sec % 60
        # On renvoie la nouvelle durée
        return nouvelle_duree
    #----------------------------------------------------------------#
    #   Tout dépends du sens du calcul 

    def __radd__(self, objet_a_ajouter): # exemple : d1 + d2 <=> d2 + d1
        """Cette méthode est appelée si on écrit 4 + objet et que
        le premier objet (4 dans cet exemple) ne sait pas comment ajouter
        le second. On se contente de rediriger sur __add__ puisque,
        ici, cela revient au même : l'opération doit avoir le même résultat,
        posée dans un sens ou dans l'autre"""
        
        return self + objet_a_ajouter
    #----------------------------------------------------------------#
    #   D'autres opérateurs
    
    def __iadd__(self, objet_a_ajouter):
        """L'objet à ajouter est un entier, le nombre de secondes"""
        # On travaille directement sur self cette fois
        # On ajoute la durée
        self.sec += objet_a_ajouter
        # Si le nombre de secondes >= 60
        if self.sec >= 60:
            self.min += self.sec // 60
            self.sec = self.sec % 60
        # On renvoie self
        return self
    #----------------------------------------------------------------#
# Test sur les methodes mathématiques
print("  Debut test sur les methodes mathématiques \n")
d1 = Duree(3,5)
print(d1)
d1_add = d1.__add__(4)
print(d1_add)
print("\n")

d2 = d1 + 120 # d1 + 54 secondes
print(d2)

d3 = Duree(8, 5)
d3 += 240
print(d3)
print("  Fin   test sur les methodes mathématiques \n")
#---------------------------------------------------------#
    # 3. Méthode de comparaison


dico_Opérateur = {"1": "==" ,"2": "!=" ,"3": ">" ,"4": ">=","5": "<","6": "<="}  


class MéthodesSpécialesComparaison: 
    def __eq__(self, obj_a_cmp):
        pass
#1      Opérateur d'égalité (equal). Renvoie True si self et obj_a_cmp sont égaux,False sinon.

        pass
    def __ne__(self, obj_a_cmp):
        pass
#2      Différent de (non equal). Renvoie True si self et obj_a_cmp sont différents,False sinon.
        
    def __gt__(self, obj_a_cmp):
        pass
#3      Teste si self est strictement supérieur (greater than) à obj_a_cmp.

    def __ge__(self, obj_a_cmp):
        pass
#4      Teste si self est supérieur ou égal (greater or equal) à obj_a_cmp.

    def __lt__(self, obj_a_cmp):
        pass
#5      Teste si self est strictement inférieur (lower than) à obj_a_cmp.

    def __le__(self, obj_a_cmp):
        pass
#6      Teste si self est inférieur ou égal (lower or equal) à obj_a_cmp.


# Exemple Pratique

def __eq__(self, autre_duree):
        """Test si self et autre_duree sont égales"""
        return self.sec == autre_duree.sec and self.min == autre_duree.min
def __gt__(self, autre_duree):
        """Test si self > autre_duree"""
        # On calcule le nombre de secondes de self et autre_duree
        nb_sec1 = self.sec + self.min * 60
        nb_sec2 = autre_duree.sec + autre_duree.min * 60
        return nb_sec1 > nb_sec2

#---------------------------------------------------------#

    # 4. Méthode utile pour pickle
    
        #   Methode __getstate__ & __setstate__
        
class Temp:
    """Classe contenant plusieurs attributs, dont un temporaire"""
    
    def __init__(self):
        """Constructeur de notre objet"""
        self.attribut_1 = "une valeur"
        self.attribut_2 = "une autre valeur"
        self.attribut_temporaire = 5
   
    def __getstate__(self):
        """Renvoie le dictionnaire d'attributs à sérialiser"""
        dict_attr = dict(self.__dict__)
        dict_attr["attribut_temporaire"] = 0
        return dict_attr

    def __setstate__(self, dict_attr):
        """Méthode appelée lors de la désérialisation de l'objet"""
        dict_attr["attribut_temporaire"] = 0
        self.__dict__ = dict_attr


    
