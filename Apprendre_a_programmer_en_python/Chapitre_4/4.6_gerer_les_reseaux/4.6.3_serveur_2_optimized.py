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
print("coté serveur \n")
# Etapes coté serveur a faire sur console:
#   -A1 Constuire le socket
#connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   -B1 Connecter notre socket
#connexion_principale.bind(('', 12800))  

#   -C1 Faire écouter notre socket
#connexion_principale.listen(5)

#   -D1 Accepter une connexion venant du client
#connexion_avec_client, infos_connexion = connexion_principale.accept()
#print(infos_connexion)

#   -E3    Faire communiquer nos socket
# connexion_avec_client.send(b"Je viens d'accepter la connexion")

#   F4- Fermer la connexion
#   connexion_avec_client.close()

#----------------------------------------------------------------#
#   3.  Le serveur
import socket
import select

hote = ''
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

serveur_lance = True
clients_connectes = []
while serveur_lance:
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la connexion_principale en lecture
    # On attend maximum 50ms
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
        [], [], 0.05)
    
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        clients_connectes.append(connexion_avec_client)
    
    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_a_lire:
            # Client est de type socket
            msg_recu = client.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_recu = msg_recu.decode()
            print("Reçu: {}".format(msg_recu))
            client.send(b"5 / 5")
            if msg_recu == "fin":
                serveur_lance = False

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()
#----------------------------------------------------------------#
#   4.  Le client
#----------------------------------------------------------------#
#   5.  Un client plus élaboré
#----------------------------------------------------------------#
