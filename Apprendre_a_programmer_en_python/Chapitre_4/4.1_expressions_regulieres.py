#       SOMMAIRE   : Les expression regulières            #

#   1.  Que sont les expressions regulières 're' ? (Theorique)
    #   1.1 syntaxes pour 're'
    #   1.2 Comment cela se presente-il ?
    #   1.3 Des Caractères ordinaires
    #   1.4 Rechercher au début ou à la fin de la chaîne
    #   1.5 Contrôler le nombre d'occurrences    
    #   1.6 Les Classes de caractères
    #   1.7 Les groupes
    
#   2.  Le module re (Pratique)
    #   2.1 Chercher dans une chaîne
    #   2.2 Remplacer une expression
        # 2.2.1 Des groupes numérotés
        # 2.2.2 Donner des noms à nos groupes
    #   2.3 Des expressions compilés




#---------------------------------------------------------#

    # Pratique

    # 2.1

import re

r"\n"

res1= re.search(r"abc", "abcdef")
print("Recherche n°1 'abc' dans la chaine suivante : {} \n".format(res1))

res2= re.search(r"abc", "abacadaeaf")
print("Recherche n°2 'abc' dans la chaine suivante.Si resultat = None aucune chaine trouvé : {} \n ".format(res2))

res3= re.search(r"abc*", "abccc")
print("Recherche n°3 'abc' dans la chaine suivante :  {} \n".format(res3))

res4= re.search(r"chat*", "chateau")
print("Recherche n°4 'chat' dans la chaine suivante :  {} \n".format(res4))

print("-----------------------------\n")
chaine = ""
expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
while re.search(expression, chaine) is None:
    chaine = input("Saisissez un numéro de téléphone (valide) :")

#-----------------------------------------------
    # 2.2   Remplacer une expression

        # 2.2.1 Des groupes numérotés

# exemple 1:

#   (a)b(cd)
#   il y a 2 groupe (a) et (cd)

# exemple 2:
print("\n")
re_gp_num = re.sub(r"(ab)", r"\1 ", "abcdef") # ici " abcdef est la chaine a parcourir
print("Séperatiion en deux groupe grace au groupe (ab) lu en 'ab ' : \n {} ".format(re_gp_num))

        # 2.2.2 Donner des noms a des groupes

texte = """
nom ='Task1' id=8
nom ='Task2' id=31
nom ='Task3' id=17 """

print(re.sub(r"id=(?P<id>[0-9]+)", r"id[\g<id>]", texte))
print("\n")
    # 2.3   Des expressions compilés


chn_mdp = r"^[A-Za-z0-9]{6,}$"
exp_mdp = re.compile(chn_mdp)
mot_de_passe = ""
while exp_mdp.search(mot_de_passe) is None:
    mot_de_passe = input("Tapez votre mot de passe : ")
