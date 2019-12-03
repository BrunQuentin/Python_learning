#   1.  Receptionner un mot de passe saisi par l'utilisateur
#   2.  Chiffrer un mot de passe

from getpass import getpass
import hashlib

#   1.
#   mot_de_passe =getpass("Tappez votre mot de passe: ")
#   print("mot de passe lisible: {} \n".format(mot_de_passe))
#--------------------------------#


#   2.
secu = hashlib.algorithms_guaranteed
print("liste d'algorigrithme de hachage:\n {}\n -----------".format(secu))

mdp = hashlib.sha1(b"Mot_de_Passe???")
print(mdp)
mdp.hexdigest()

#--------------------------------

chaine_mot_de_passe = b"azerty"
mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()

verrouille = True
while verrouille:
    entre = getpass("Tapez le mot de passe : ") # azerty
    # On encode la saisie pour avoir un type bytes
    entre = entre.encode()
    
    entre_chiffre = hashlib.sha1(entre).hexdigest()
    if entre_chiffre == mot_de_passe_chiffre:
        verrouille = False
    else:
        print("Mot de passe incorrect")

print("Mot de passe accepté...")
