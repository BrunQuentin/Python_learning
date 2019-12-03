#   1 Presentation du réseau
    #   1.1 Protocole TCP
    #   1.2 Clients & serveur
    #   1.3 Les différentes étapes
    #   1.4 Etablir une connexion
#   2.  Sockets
#   3.  Le serveur
#   4.  Le client
#   5.  Un client plus élaboré

#----------------------------------------------------------------#
#   1.1 TCP /UDP

#   -TCP    (Transmission Control Protocol)
#           =>  Orienté connexion. 
#           =>  Aucun pb de reception de message
#           =>  Si connexion perdu, la rétablir
#       avantages:
#       - capacité de transfert en grande quantité avec un % de perte d'info  
#       - connexion sécurisé
#       inconvénients;
#       - plus lent que UDP

#----------------------------------------------------------------#
#   1.2

#   Serveur :   Ecoute/Sniffe le réseau en attendant des connexion
#   Client:     Se connecte aux serveur
#----------------------------------------------------------------#
#   1.3 Les différentes étapes:

    #   Le serveur :
    #   1-  attend une connexion de la part du client ;
    #   2-  accepte la connexion quand le client se connecte ;
    #   3-  échange des informations avec le client ;
    #   4-  ferme la connexion.
    #   Le client :
    #   1-  se connecte au serveur ;
    #   2-  échange des informations avec le serveur ;
    #   3-  ferme la connexion.
#----------------------------------------------------------------#

#   1.4 Etablir une connexion

#   Pour que le client se connecte au serveur il faut:
#   -   Le nom d'hote (host)
#   -   Le numéro de port ( connexion web standard
#       (http 80 / connexion web privée (https): 443

#----------------------------------------------------------------#
#   2.  Sockets
import socket
print("coté serveur")
# Etapes coté serveur a faire sur console:
#   -A Constuire le socket
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   -B Connecter notre socket
connexion_principale.bind(('', 12800))  

#   -C Faire écouter notre socket
connexion_principale.listen(5)

#   -D Accepter une connexion venant du client
connexion_avec_client, infos_connexion = connexion_principale.accept()
print(infos_connexion)

#   -E    Faire communiquer nos socket
# connexion_avec_client.send(b"Je viens d'accepter la connexion")

#   F- Fermer la connexion
#   connexion_avec_client.close()

#----------------------------------------------------------------#
#   3.  Le serveur
#----------------------------------------------------------------#
#   4.  Le client
#----------------------------------------------------------------#
#   5.  Un client plus élaboré
#----------------------------------------------------------------#
