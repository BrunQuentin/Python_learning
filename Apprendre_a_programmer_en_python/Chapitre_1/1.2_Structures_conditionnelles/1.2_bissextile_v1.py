# -*-coding:Latin-1 -*
# Fonction pour voir si une ann�e est bissextile ou non

annee =  input("Saisissez une ann�e : ")
annee = int(annee) # on caste la variable annee en int
bissextile = False

if annee %400 == 0:
	bissextile = True
elif annee %100 == 0:
	bissextile = False
elif annee %4== 0:
	bissextile = True
else:
	bissextile = False

if bissextile:
	print("l'ann�e saisi est bissextile.")
else:
	print("l'ann�e saisi n'est pas bissextile.")
