# 1.    la portée des variables ( variables locales)
    # 1.1   Dans nos fonctions, quelles variables sont accessibles ?

a = 5

def print_a():
    """Fonctionchargée d'afficher la variable a
    Cette variable an'est pas passé en paramètre de la fonction.
    On suppose qu'elle a été créée en dehors de la fonction,
    on veux voir si elle est accessible depuis le corps de la fonction."""

    print("La variabe a = {0}." .format(a))

# Exemple sur interpreteur
#   >>> a = 5
#   >>> print_a()
#   La variable a = 5.
#   >>> a = 8
#   >>> print_a()
#   La variable a = 8.

#---------------------------------------------------------------------------   
    # 1.2    Qu'advient-il des variables définies dans un corps de fonction ?

def set_var(nouvelle_valeur):
    """Fonction nous permettant de tester la portée des variables
    définies dans notre corps de fonction"""
    
    # On essaye d'afficher la variable var, si elle existe
    try:
        print("Avant l'affectation, notre variable var vaut {0}.".format(var))
    except NameError:
        print("La variable var n'existe pas encore.")
    var = nouvelle_valeur
    print("Après l'affectation, notre variable var vaut {0}.".format(var))

# Exemple sur interpreteur
#>>> set_var(5)
#La variable var n'existe pas encore.
#Après l'affectation, notre variable var vaut 5.
#>>> var
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'var' is not defined


#---------------------------------------------------------------------------
    # 1.3    Une fonction modifiant des objets

def ajouter(liste, valeur_a_ajouter):
    """Cette fonction insère à la fin de la liste la valeur que l'on veut ajouter"""

    liste.append(valeur_a_ajouter)

# Exemple sur interpreteur
    #   >>> ma_liste=['a', 'e', 'i']
    #   >>> ajouter(ma_liste, 'o')
    #   >>> ma_liste
    #   ['a', 'e', 'i', 'o']
#---------------------------------------------------------------------------
    # 1.4   Les Références
    
# Exemple 1 sur interpreteur :   2 listes qui reférence au meme endroits ?
    #   >>>ma_liste1 = [1, 2, 3]
    #   >>>ma_liste2 = ma_liste1
    #   >>>ma_liste2.append(4)
    #   >>>print(ma_liste2)
    #   [1, 2, 3, 4]
    #   >>>print(ma_liste1)
    #   [1, 2, 3, 4]

# Exemple 2 sur interpreteur :   modifier une liste sans toucher à l'autre

    #   >>> ma_liste1 = [1, 2, 3]
    #   >>> ma_liste2 = list(ma_liste1) # Cela revient à copier le contenu de ma_liste1
    #   >>> ma_liste2.append(4)
    #   >>> print(ma_liste2)
    #   [1, 2, 3, 4]
    #   >>> print(ma_liste1)
    #   [1, 2, 3]

# Exemple 3 sur interpreteur :   Comparaisons des références entre 2 listes

    #   >>> ma_liste1 = [1, 2]
    #   >>> ma_liste2 = [1, 2]
    #   >>> ma_liste1 == ma_liste2 # On compare le contenu des listes
    #   True
    #   >>> ma_liste1 is ma_liste2 # On compare leur référence
    #   False


#---------------------------------------------------------------------------
#Les variables Globales

i= 4
def inc_i():
    """ Fonction chargée d'incrementé i de 1. """
    global i # python recherche i en dehors de l'espace local de la fonction
    i += 1
     
