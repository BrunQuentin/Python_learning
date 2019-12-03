import socket

#   2. Sockets

#   A-  Création du client
print("coté client")
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   B-  Connecter le client
connexion_avec_serveur.connect(('localhost', 12800))

#   C-  Faire communiquer nos socket
#   msg_recu = connexion_avec_server.recv(1024)
#   msg_recu

#   D- Fermer la connexion
#   connexion_avec_serveur.close()
