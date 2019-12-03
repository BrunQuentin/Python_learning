import math
from fractions import Fraction
import random

#   1.  Module math
    # 1.1   Fonction usuelles
    # 1.2   Trigonométrie
    # 1.3   Arrondir un nombre
#   2.  Fractions avec le module fractions

#   3.  Du pseudo-aleatoire avec random

#-----------------------------------------
#   1.1
carre = math.pow(5,2) # 5 au carré

carre_2 = 5 ** 2
print(" avec pow : {} \n avec ** : {} ".format(carre, carre_2))
rac = math.sqrt(25)     # racine carré de 25
expo = math.exp(5)      # exponentielle
v_abs = math.fabs(-3)   # valeur absolu
print(" sqrt(25): {} \n exponentielle(5) : {} \n valeurs absolu: {} \n --------- ".format(rac, expo, v_abs))

#   1.2 Trigo
#   math.degrees(angle_en_radians)
#   math.radians(angle_en_degres)

conv_deg = math.degrees(3)
conv_rad = math.radians(171.87)

print(conv_deg, conv_rad)
print("----- Fin Trigo -----")

#   1.3 Arrondir un nombre
arrondi_1 = math.ceil(2.3)  #   Renvoie le plus petit entier >= 2.3
arrondi_2 = math.floor(5.8) #   Renvoie le plus grand entier <= 5.8
arrondi_3 = math.trunc(9.5) #   Tronque 9.5
print(" ceil(2.3) = {} \n floor(5.8) = {} \n trunc(9.5) = {} \n ---Fin Arrondi --- "\
                                  .format(arrondi_1, arrondi_2, arrondi_3))
#-----------------------------------------
#       Créer/ manipuler des fraction

un_demi = Fraction(1, 2)
un_quart = Fraction('1/4')
autre_fraction = Fraction(-5, 30)



print(" 0.5 = {} \n 0.25 = {} \n autre fraction = {} \n -----------------"\
                              .format(un_demi, un_quart, autre_fraction))

frac_float =Fraction.from_float(0.5)
float(un_quart)

un_dixieme = Fraction(1, 10)
frac = un_dixieme + un_dixieme+ un_dixieme
frac_2 =  0.1 + 0.1 + 0.1
print(" fraction 1 = {} \n fraction 2 = {} \n fraction 2 a la main = {} \n -----------------"\
                              .format(un_dixieme, frac,frac_2))
frac_3 = un_dixieme * un_quart
frac_4 = un_dixieme + 5
frac_5 = un_demi / un_quart
frac_6 = un_quart / un_demi
print(" fraction 3 = {} \n fraction 4 = {} \n fraction 5 = {} \n fraction 6 = {} \n -----------------"\
                              .format(frac_3, frac_4,frac_5, frac_6))
print("---Fin fractions ---")
#-----------------------------------------
# 3.1   du pseudo-aleatoire

rand1 = random.randrange(5, 10, 2) #(debut_intervalle, fin_intervalle, pas)
# 3.2   fonction random
rand2 = random.random()
# 3.3   randrange & randint
rand3 = random.randint(1, 6)
print(" Choix random 1: {} \n Choix random 2: {} \n Choix random 3: {} \n ----------"\
          .format(rand1, rand2, rand3))

# 3.4   Opération sur les séquences
rand4 = random.choice(['a', 'b', 'k', 'p', 'i', 'w', 'z'])
liste = ['a', 'b', 'k', 'p', 'i', 'w', 'z']
print(" Choix random 4: {} \n liste d'origine: {} \n ----------".format(rand4, liste))
random.shuffle(liste)
print(" Liste melangé: {} \n  ----------".format(liste))
print("---Fin Pseudo-aleatoire ---")
