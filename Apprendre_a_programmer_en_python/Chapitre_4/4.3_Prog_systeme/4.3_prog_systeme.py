#   1.  Les flux standard
    #   Accéder au flux
    #   Modifier les flux standard
#   2.  Les signaux
#   3.  Interpéter les argumemnts de la ligne de commande
#   4.  Executer une commande système depuis Python
#---------------------------------------------------------
import sys
import signal 

#   1.1
input_1 = sys.stdin   # L'entrée standard     (read part)
output_1 = sys.stdout  # La sortie standard    (write part)
output_2 =sys.stderr  # L'erreur standard     (write part)

print(" entrée standard: {0} \n sortie standard: {1} \n sortie d'erreur: {2} \n".format(input_1, output_1, output_2))

sys.stdout.write("un test")
print("\n")
sys.stdout.write("un test\n")
print("-----Fin acces flux standard (1.1)-----")
#   1.2
#with open('4.3_sortie.txt', 'w') as fichier:
#   sys.stdout = fichier
#   print("Quelque chose...".format(fichier))
#   fichier.close()

#----------------------------------------------------------#
#   2.

def fermer_programme(signal, frame):
    """Fonction appelée quand vient l'heure de fermer notre programme"""
    print("C'est l'heure de la fermeture !")
    sys.exit(0)

# Connexion du signal à notre fonction
signal.signal(signal.SIGINT, fermer_programme)

# Notre programme...
print("Le programme va boucler...")
while True:
    continue



