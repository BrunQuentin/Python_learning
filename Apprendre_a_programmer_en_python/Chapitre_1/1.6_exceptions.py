


# 1. Forme minimale du bloc try
annee = input("Veuillez saisir une année: ")

try:
    # Bloc a essayer
    annee = int(annee)
except:
    # Bloc qui sera executer en cas d'erreur
    print("Erreur lors de la conversion de l'année. ")
    
#------------------------------------------#
# 2. Forme plus complète

    # 2.1   Exécuter le bloc except pour un type d'exception précis



try:
    numerateur = input("Veuillez saisir un numerateur:")
    numerateur = int(numerateur)
    denominateur =input("Veuillez saisir un denominateur:")
    denominateur = int(denominateur)
    resultat = numerateur / denominateur
except NameError:
    print("Une erreur est survenue... laquelle ?")
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
#------------------------------------------
#   try:
        # Bloc de test
#   except type_de_l_exception as exception_retournee:
#       print("Voici l'erreur :", exception_retournee)
#------------------------------------------
    # 2.2   Les mots clés "else" et "finally

        # "else"

try:
    numerateur_2 = input("Veuillez saisir un numerateur (métode else) :")
    numerateur_2 = int(numerateur_2)
    denominateur_2 =input("Veuillez saisir un denominateur (métode else) :")
    denominateur_2= int(denominateur_2)
    resultat_2 = numerateur_2 / denominateur_2
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)

        #------------------------------------------
        # "finally"
        
#   try:
        # Test d'instruction(s)
#   except type_de_l_exception:
        # Traitement en cas d'erreur
#   finally:
        # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non
    
        #------------------------------------------
        # Un petit bonus : le mot clé "pass"
try:
    1/0
except ZeroDivisionError: 
    pass 
#------------------------------------------
# 3. Les asserions

annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
#------------------------------------------
# 4. Lzver une exception

annee = input("Saisissez une année: ") # L'utilisateur saisit l'année
try:
    annee = int(annee) # On tente de convertir l'année
    if annee<=0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative).")
