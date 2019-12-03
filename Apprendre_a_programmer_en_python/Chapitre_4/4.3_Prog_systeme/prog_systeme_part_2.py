import sys
import argparse

import os

#if len(sys.argv) < 2:
#    print("Précisez une action en paramètre")
#    sys.exit(1)

#action = sys.argv[1]

#if action == "start":
#    print("On démarre l'opération")
#elif action == "stop":
#    print("On arrête l'opération")
#elif action == "restart":
#    print("On redémarre l'opération")
#elif action == "status":
#    print("On affiche l'état (démarré ou arrêté ?) de l'opération")
#else:
#    print("Je ne connais pas cette action")




parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="le nombre à mettre au carré")
parser.add_argument("-v", "--verbose", action="store_true",
        help="augmente la verbosité")
args = parser.parse_args()
print("Vous avez précisé X =", args.x)

x = args.x
retour = x ** 2
if args.verbose:
    print("{} ^ 2 = {}".format(x, retour))
else:
    print(retour)



