#   1.    Pourquoi tester
#   2.  Exemples de test unitaires
    #   2.1 Tester une fonctionnalité existante
#   3.  Decouverte automatiques des tests

#------------------------------------------------------------#

import random
import unittest

#   2.1

#   random.choice
liste = ["chat", "chien", "renard", "serpent", "cheval", "parapluie"]
print(" On a notre liste d'éléments présenter ci-dessous:\
            \n {} \n".format(liste))
choix_liste= random.choice(liste)
print(" On a mélanger la liste et on obtient... :\n {} ".format(choix_liste))

# random.shuffle
liste_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(" On a notre liste de 1 à 9 présenter ci-dessous:\
        \n {} \n".format(liste_2))
random.shuffle(liste_2)
print(" On a mélanger la liste complète\
            ,et on obtient... :\n {} ".format(liste_2))

# random.sample
liste_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(" On a notre liste d'éléments présenter ci-dessous:\
            \n {} \n".format(liste_3))
random.sample(liste_3, 5)
print(" On a notre liste de caractères mélangé :\
            \n {} \n".format(liste_3))

    # Ou peut-être que cet exemple sera plus clair
liste_4= random.sample(range(1000), 10)
print(" On a notre liste de nombres mélangé:\
            \n {} \n --------------------".format(liste_4))

#------------ test de la fonction random.choice -------------#
class RandomTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module 'random'."""

    def setUp(self):
        """Initialisation des tests."""
        self.liste = list(range(10))    
    
    def test_choice(self):
        """Test le fonctionnement de la fonction 'random.choice'."""
        liste = list(range(10))
        elt = random.choice(liste)
        # Vérifie que 'elt' est dans 'liste'
        self.assertIn(elt, liste)

     
    def test_shuffle(self):
        """Test le fonctionnement de la fonction 'random.shuffle'."""
        liste = list(range(10))
        random.shuffle(liste)
        liste.sort()
        self.assertEqual(liste, list(range(10)))

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        liste = list(range(10))
        extrait = random.sample(liste, 5)
        for element in extrait:
            self.assertIn(element, liste)

    def test_sample(self):
        """Test le fonctionnement de la fonction 'random.sample'."""
        liste = list(range(10))
        extrait = random.sample(liste, 5)
        for element in extrait:
            self.assertIn(element, liste)

        self.assertRaises(ValueError, random.sample, liste, 20)

unittest.main()#   Pour afficher nos test sur console

#------------ test echoué de la fonction random.choice  -------------#
#class RandomTest(unittest.TestCase):

#   """Test case utilisé pour tester les fonctions du module 'random'."""

#   def test_choice_2(self):
#       """Test le fonctionnement de la fonction 'random.choice'."""
#       liste_2 = list(range(10))
#       elt_2 = random.choice(liste_2)
#        self.assertIn(elt_2, ('a', 'b', 'c'))
#
#unittest.main()

#   Les principales méthode d'assertion


methode = [
    "assertEqual(a, b)",
    "assertNotEqual(a, b)",
    "assertTrue(x)",
    "assertFalse(x)",
    "assertIs(a, b)",
    "assertIsNot(a, b)",
    "assertIsNone(x)",
    "assertIsNotNone(x)",
    "assertIn(a, b)",
    "assertNotIn(a, b)",
    "assertIsInstance(a, b)",
    "assertNotIsInstance(a, b)",
    "assertRaises(exception, fonction, *args, **kwargs) ",  
    ]

explications = [
    "a == b",
    "a != b",
    "x is True",
    "x is False",
    "a is b",
    "a is not b",
    "x is None",
    "x is not None",
    "a in b",
    "a not in b",
    "isinstance(a, b)",
    "not isinstance(a, b)",
    "Vérifie que la fonction lève l'exception attendue.",
    ]

print("Liste de Methode : {} \n \
        Explications correspondante: {}\n".format(methode, explications))
