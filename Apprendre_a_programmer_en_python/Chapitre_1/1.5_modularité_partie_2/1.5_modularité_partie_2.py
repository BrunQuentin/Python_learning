# -*-coding:Latin-1 -*
# Fonction pour voir si une ann�e est bissextile ou non (optimis�)

import os

annee =  input("Saisissez une ann�e : ")
annee = int(annee) # on caste la variable annee en int

if annee %400 == 0 or (annee %4 == 0 and annee % 100 !=0):
    	print("l'ann�e saisi est bissextile.")
else:
	print("l'ann�e saisi n'est pas bissextile.")

os.system("pause")

