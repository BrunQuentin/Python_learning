import time,sys, random
from threading import Thread, RLock

#   1.  Creation de threads
#   2.  La synchronisation des threads
#-----------------------------------------#

#   1.
print("Avant le sleep")
time.sleep(1)
print("Après le sleep")


# Exemple 1: Répète 20 fois
i = 0
while i < 20:
    sys.stdout.write("1")
    sys.stdout.flush()
    attente = 0.2
    attente += random.randint(1, 60) / 100
    # attente est à présent entre 0.2 et 0.8
    time.sleep(attente)
    i += 1
print("\n--- fin exemple 1 ---")

# Exemple 2: Approche parallèle 
class Afficheur(Thread):

    """Thread chargé simplement d'afficher une lettre dans la console."""

    def __init__(self, lettre):
        Thread.__init__(self)
        self.lettre = lettre

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 20:
            sys.stdout.write(self.lettre)
            sys.stdout.flush()
            attente = 0.2
            attente += random.randint(1, 60) / 100
            time.sleep(attente)
            i += 1


# Création des threads
thread_1 = Afficheur("1")
thread_2 = Afficheur("2")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

print("\n--- fin exemple 2: 2 threads en // ---")
#------------------------------------------------------------------#
#   2.
class AfficheurSimultane(Thread):

    """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 5:
            for lettre in self.mot:
                sys.stdout.write(lettre)
                sys.stdout.flush()
                attente = 0.2
                attente += random.randint(1, 60) / 100
                time.sleep(attente)
            i += 1

# Création des threads
thread_1 = AfficheurSimultane("canard")
thread_2 = AfficheurSimultane("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()

#------------------------------------------------------------------#

verrou = RLock()

class AfficheurSecuriser(Thread):

    """Thread chargé simplement d'afficher un mot dans la console."""

    def __init__(self, mot):
        Thread.__init__(self)
        self.mot = mot

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while i < 5:
            with verrou:
                for lettre in self.mot:
                    sys.stdout.write(lettre)
                    sys.stdout.flush()
                    attente = 0.2
                    attente += random.randint(1, 60) / 100
                    time.sleep(attente)
            i += 1

# Création des threads
thread_1 = AfficheurSecuriser("canard")
thread_2 = AfficheurSecuriser("TORTUE")

# Lancement des threads
thread_1.start()
thread_2.start()

# Attend que les threads se terminent
thread_1.join()
thread_2.join()
