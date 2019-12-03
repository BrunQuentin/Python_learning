import socket

#   2. Sockets

#   A2-  Création du client
print("coté client \n")
#   connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   B2-  Connecter le client
#   connexion_avec_serveur.connect(('localhost', 12800))

#   C3-  Faire communiquer nos socket
#   msg_recu = connexion_avec_server.recv(1024)
#   msg_recu

#   D4- Fermer la connexion
#   connexion_avec_serveur.close()

#--------------------------------------------------------------
import socket

hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_a_envoyer = b""
while msg_a_envoyer != b"fin":
    msg_a_envoyer = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    msg_a_envoyer = msg_a_envoyer.encode()
    # On envoie le message
    connexion_avec_serveur.send(msg_a_envoyer)
    msg_recu = connexion_avec_serveur.recv(1024)
    print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connexion_avec_serveur.close()
