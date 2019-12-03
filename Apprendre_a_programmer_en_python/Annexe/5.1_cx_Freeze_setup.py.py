# -*-coding:Latin-1 -* # encodage du fichier

"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "salut",
    version = "0.1",
    description = "Ce programme vous dit bonjour",
    executables = [Executable("salut.py")],
)


#   name: le nom de notre futur programme.
#   version: sa version.
#   description: sa description.
#   executables: une liste contenant des objets de typeExecutable,
#       type que vous importez decx_Freeze. Pour se construire,
#       celui-ci prend en paramètre le chemin du fichier.py
#       (ici, c'est notre fichiersalut.py).


#   etape 1:    aller dans le repertoire ou se trouve Python38-32 (pour moi)
#   etape 2:    creer un executable avec la commande suivante
#                   C:\...\python38-32\python.exe setup.py build
