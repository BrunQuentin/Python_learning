#                   SOMMAIRE   : Les proprietes             
#   1.  Qu'est ce que l'encapsulation (théorique)
    
#   2.  Les propriétés à la casserole (théorique)

#   3.  Les propriétés en action ( pratique)
#-----------------------------------------------------------#

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom ;
    - son prénom ;
    - son âge ;
    - son lieu de résidence"""

    
    def __init__(self, nom, prenom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self._lieu_residence = "Paris" # Notez le souligné _ devant le nom
    def _get_lieu_residence(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lectur
        à l'attribut 'lieu_residence'"""
        
        
        print("On accède à l'attribut lieu_residence !")
        return self._lieu_residence
    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format( \
                self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)


# Test sur les propriétés
jack = Personne("Ryan","Jack")
print("Mon nom est  : \n {} ".format(jack.nom))
print("Mon prenom est  : \n {} ".format(jack.prenom))
print("Mon age est de : \n  {} ans ".format(jack.age))
print("J'habite actuelement à : \n {} ".format(jack.lieu_residence))
demenage = jack.lieu_de_residence = " Ecosse"
print("Je démenage ici en  : \n {} ".format(demenage))

#---------------------------------------------------------------------------------#
# En resumé

#   >   Les propriétés permettent de contrôler
#       l'accès à certains attributs d'une instance.

#   >   Elles se définissent dans le corps de la classe en suivant cette syntaxe :
#       nom_propriete =property(\
#       methode_accesseur, methode_mutateur,methode_suppression, methode_aide).


#   >   On y fait appel ensuite en écrivant
#       objet.nom_propriete comme pour n'importe quel attribut.

#   >   Si on veux lire l'attribut => methode_accesseur est appelée
#   >   Si on veux modifier l'attribut => methode_mutateur est appelée
#   >   Chacun des paramètres à passer àpropertyest optionnel.
#---------------------------------------------------------------------------------#

