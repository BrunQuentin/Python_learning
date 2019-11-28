# -*-coding:Latin-1 -*

import os

os.chdir("E:\\Quentin_BRUN\\python\\python_save work\\Apprendre a programmer en python\\Chapitre_2\\2.4_utiliser_des_fichiers")
#   I.  Lecture et �criture dans un fichier

    # 1.    Ouvrir un fichier
    #--------------------------------------------------
    # 2.    Fermer un fichier
    #--------------------------------------------------
    # 3.    Lire l'int�gralit� du fichier
    #--------------------------------------------------
    # 4.    Ecrire dans un fichier
    #--------------------------------------------------
        # 4.1 Ecrire une cha�ne
    #--------------------------------------------------
    # 5.    Ecrire d'autres types de donn�es ( avec la m�thode "write")
    #--------------------------------------------------
    # 6.    Le mot cl� "with"


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
mon_fichier_3.write("Premier test d'�criture dans un fichier via Python")   #   4.            
mon_fichier_3.close()

    #6
with open('fichier_write.txt', 'r') as mon_fic:
    texte = mon_fic.read()
    print("--- Fichier r�ecrit ---\n")
    print(texte)
    

#--------------------------------------------------

#   II. Enregister des objets dans les fichiers
    # 1.    Enregistrer

import pickle

# On creer un set(un ensemble) de donn�es pour notre fichier donnees
score = {
    "joueur 1":    5,
    "joueur 2":   35,
    "joueur 3":   20,
    "joueur 4":    2
    }

with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    # enregistrement des donn�es sur le code python
    # dans le fichier "donnees" sous forme binaire avec b
    mon_pickler.dump(score)


    #--------------------------------------------------
    # 2.    Recup�rer nos objets enregistr�s
with open('donnees', 'rb') as fichier:
     mon_depickler = pickle.Unpickler(fichier)
     # Lecture des objets contenus dans le fichier...
     score_recupere = mon_depickler.load()
     print("--- score recup�r� du fichier 'donnees' ---\n")
     print(score_recupere)



    
