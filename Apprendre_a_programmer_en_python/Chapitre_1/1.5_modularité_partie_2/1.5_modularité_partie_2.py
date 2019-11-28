# -*-coding:Latin-1 -*
# Fonction pour voir si une année est bissextile ou non (optimisé)

import os

annee =  input("Saisissez une année : ")
annee = int(annee) # on caste la variable annee en int

if annee %400 == 0 or (annee %4 == 0 and annee % 100 !=0):
    	print("l'année saisi est bissextile.")
else:
	print("l'année saisi n'est pas bissextile.")

os.system("pause")

