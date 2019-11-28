"""module multipli contenant la fonction table"""

import os
import sys

# Crees ses propres modules

    #   Mes modules à moi
def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb de
    1 * nb jusqu'à max * nb"""
    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1



    #   Faire un test de module dans le module-même

while True:
    if __name__ == "__main__":
        choix_table= input("\n saisir un table de multiplication: ")
        choix_table = int(choix_table)
        table(choix_table)
        continuer = input("voulez vous continuer O/N ? :")
        if continuer != "N" and continuer == "O":
            print(" Passons au choix de table suivante ...")
            
        else:
            continuer == "N"
            print(" A bientot")
            sys.exit()
    
        
        
        
            
            
    
        
        
