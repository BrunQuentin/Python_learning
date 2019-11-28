# -*-coding:Latin-1 -*

# Avancer pas à pas vers la modularité 1/2
## Les Fonctions

#-----------------------------------------#
    # Fonciton pour la une table

def table_de_7():
       nb = 7
       cpt = 0
        
       while cpt <10:
           print(cpt +1, "*", nb, "=", (cpt +1)* nb)
           cpt += 1

#-----------------------------------------#     
    # Fonction pour n'importe que table en passant la table en argument

def table_0(nb):
    """ Fonction affichant la table de multiplication par nb
    de 1*nb à 10*nb"""
    cpt = 0
    while cpt <10:
           print(cpt +1, "*", nb, "=", (cpt +1)* nb)
           cpt += 1
#-----------------------------------------#
    # Fonction pour faire varier le choix de la table et sa taille maximale
    # 2 arguments utilisé
    

def table_1(nb1,max):
    """ Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    (max >= 0)"""
    cpt1 = 0
    
    while cpt1 <max:
           print(cpt1 +1, "*", nb1, "=", (cpt1 +1)* nb1)
           cpt1 += 1
#-----------------------------------------#
    # Valeurs par defaut des parametres

def table(nb, max=10):
    """ Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb où max est par régler par defaut à 10
    (max >= 0)"""
    
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1

def fonc(a=1, b=2 ,c=3 ,d=4 ,e=5):
    print("a= ",a, "b =",b ,"c =",c ,"d =",d ,"e =",e)

#-----------------------------------------#
    # Signature d'une fonction

def exemple_1():
     while 1:
        print("Un exemple d'une fonction sans paramètre ")
        exemple_1()

def exemple_2():
    while 1:
        print("Un AUTRE exemple de fonction sans paramètre ")
        exemple_2()
        
    
#-----------------------------------------#
    # instruction return

def carre(valeur):
       
       return valeur * valeur

#-----------------------------------------#

## Les Fonctions lambda

f = lambda x: x*x

g = lambda x, y : x + y


#-----------------------------------------#

## A la découverte des modules

import math

math.sqrt(16)
# resutlat attendu 4 

import math as mathematiques
mathematiques.sqrt(25)

from math import fabs # importe uniquement le module fonction absolu (fabs)

from math import *   # importe tout ce qui ce trouve dans le module
