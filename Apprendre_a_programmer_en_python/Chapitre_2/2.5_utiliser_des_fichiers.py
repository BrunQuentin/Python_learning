# -*-coding:Latin-1 -*

import os

os.chdir("E:\\Quentin_BRUN\\python\\python_save work\\Apprendre a programmer en python\\Chapitre_2\\2.4_utiliser_des_fichiers")
#   I.  Lecture et écriture dans un fichier

    # 1.    Ouvrir un fichier
    #--------------------------------------------------
    # 2.    Fermer un fichier
    #--------------------------------------------------
    # 3.    Lire l'intégralité du fichier
    #--------------------------------------------------
    # 4.    Ecrire dans un fichier
    #--------------------------------------------------
        # 4.1 Ecrire une chaîne
    #--------------------------------------------------
    # 5.    Ecrire d'autres types de données ( avec la méthode "write")
    #--------------------------------------------------
    # 6.    Le mot clé "with"


mon_fichier = open("fichier.txt", "r")  #   1.
print("--- info sur fichier.txt --- \n")
print(mon_fichier)                      #   1.

print("--- Le type de fichier.txt ---\n")
print(type(mon_fichier))                #   1.


contenu = mon_fichier.read()            #   3.
print("--- son contenu ---\n")
print(contenu)                          #   3.
mon_fichier.close()                     #   2.

mon_fichier_3 = open("fichier_write.txt","w")
mon_fichier_3.write("Premier test d'écriture dans un fichier via Python")   #   4.            
mon_fichier_3.close()

    #6
with open('fichier_write.txt', 'r') as mon_fic:
    texte = mon_fic.read()
    print("--- Fichier réecrit ---\n")
    print(texte)
    

#--------------------------------------------------

#   II. Enregister des objets dans les fichiers
    # 1.    Enregistrer

import pickle

# On creer un set(un ensemble) de données pour notre fichier donnees
score = {
    "joueur 1":    5,
    "joueur 2":   35,
    "joueur 3":   20,
    "joueur 4":    2
    }

with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    # enregistrement des données sur le code python
    # dans le fichier "donnees" sous forme binaire avec b
    mon_pickler.dump(score)


    #--------------------------------------------------
    # 2.    Recupérer nos objets enregistrés
with open('donnees', 'rb') as fichier:
     mon_depickler = pickle.Unpickler(fichier)
     # Lecture des objets contenus dans le fichier...
     score_recupere = mon_depickler.load()
     print("--- score recupéré du fichier 'donnees' ---\n")
     print(score_recupere)



    
