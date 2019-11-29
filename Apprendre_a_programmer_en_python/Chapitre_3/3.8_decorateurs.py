# 1. En Theorie
    #   1.1 Format le plus simple
    #   1.2 Modifier le comportement de notre fonction
    #   1.3 Un décorateur avec des paramètres
    #   1.4 Tenir compte des paramètres de notre fonction
    #   1.5 Des décorateurs s'appliquant aux définitions de classes
    #   1.6 Chaîner nos décorateurs
    
# 2. Exemples d'application
    #   2.1 Les classes singleton
    #   2.2 Controler les types passés à notre fonction
#----------------------------------------------------------------#
    
    #   1.1
def mon_decorateur(fonction):
    """Premier exemple de décorateur"""
    print(" Notre décorateur est appelé avec en paramètre la fonction {0}".format(fonction))
    return fonction

@mon_decorateur
def salut():
    """Fonction modifiée par notre décorateur"""
    print("Salut !")

#Autre methode:
# def fonction():
#    pass
# salut = decorateur(salut)



    #--------------------------------------#
    #   1.2
def mon_decorateur(fonction):
    """Notre décorateur : il va afficher un message avant l'appel de la
    fonction définie"""
    
    def fonction_modifiee():
        """Fonction que l'on va renvoyer. Il s'agit en fait d'une version
        un peu modifiée de notre fonction originellement définie. On se
        contente d'afficher un avertissement avant d'exécuter notre fonction
        originellement définie"""
        
        print("Attention ! On appelle {0}".format(fonction))
        return fonction()
    return fonction_modifiee

@mon_decorateur
def salut():
    print("Salut !")

def obsolete(fonction_origine):
    """Décorateur levant une exception pour noter que la fonction_origine
    est obsolète"""
    
    def fonction_modifiee():
        raise RuntimeError("la fonction {0} est obsolète !".format(fonction_origine))
    return fonction_modifiee

# Sur l'interpreteur
# salut()
# salut
    
    #--------------------------------------#
    #   1.3
"""Pour gérer le temps, on importe le module time
On va utiliser surtout la fonction time() de ce module qui renvoie le nombre
de secondes écoulées depuis le premier janvier 1970 (habituellement).
On va s'en servir pour calculer le temps mis par notre fonction pour
s'exécuter"""

import time

def controler_temps(nb_secs):
    """Contrôle le temps mis par une fonction pour s'exécuter.
    Si le temps d'exécution est supérieur à nb_secs, on affiche une alerte"""
    
    def decorateur(fonction_a_executer):
        """Notre décorateur. C'est lui qui est appelé directement LORS
        DE LA DEFINITION de notre fonction (fonction_a_executer)"""
        
        def fonction_modifiee():
            """Fonction renvoyée par notre décorateur. Elle se charge
            de calculer le temps mis par la fonction à s'exécuter"""
            
            tps_avant = time.time() # Avant d'exécuter la fonction
            valeur_renvoyee = fonction_a_executer() # On exécute la fonction
            tps_apres = time.time()
            tps_execution = tps_apres - tps_avant
            if tps_execution >= nb_secs:
                print("La fonction {0} a mis {1} pour s'exécuter".format( \
                        fonction_a_executer, tps_execution))
            return valeur_renvoyee
        return fonction_modifiee
    return decorateur

@controler_temps(4) # @decorateur(parametre)
def attendre():
    input("Appuyer sur Entrée... ")

#Autre methode:
def attendre2():
    print("-----------------")
    input("Appuyer sur Entrée Vite ... !!!! ")
attendre2 = controler_temps(3)(attendre2)
    
    #--------------------------------------#
    #   1.4
def fonction_modifiee(*parametres_non_nommes, **parametres_nommes):
    """Fonction renvoyée par notre décorateur. Elle se charge
    de calculer le temps mis par la fonction à s'exécuter"""
    
    tps_avant = time.time() # avant d'exécuter la fonction
    ret = fonction_a_executer(*parametres_non_nommes, **parametres_nommes)
    tps_apres = time.time()
    tps_execution = tps_apres - tps_avant
    if tps_execution >= nb_secs:
        print("La fonction {0} a mis {1} pour s'exécuter".format( \
            fonction_a_executer, tps_execution))
    return ret
    
    
    #--------------------------------------#
    #   1.5
def decorateur1(classe):
    print("Définition de la classe {0}".format(classe))
    return classe

def decorateur2(dict):
    print("Définition du dictionnaire de la classe {0}".format(dict))
    return dict

@decorateur1
class Test:
    pass
    #--------------------------------------#
    #   1.6
print("----------")
@decorateur1
@decorateur2
def fonction():
    pass

#----------------------------------------------------------------#
    #   2.1
    
def singleton(classe_definie):
    instances = {} # Dictionnaire de nos instances singletons
    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance

@singleton
class Test_S:
    pass

    #--------------------------------------#
    #   2.2

def controler_types(*a_args, **a_kwargs):
    """On attend en paramètres du décorateur les types souhaités. On accepte
    une liste de paramètres indéterminés, étant donné que notre fonction
    définie pourra être appelée avec un nombre variable de paramètres et que
    chacun doit être contrôlé"""
    
    def decorateur(fonction_a_executer):
        """Notre décorateur. Il doit renvoyer fonction_modifiee"""
        def fonction_modifiee(*args, **kwargs):
            """Notre fonction modifiée. Elle se charge de contrôler
            les types qu'on lui passe en paramètres"""
            
            # La liste des paramètres attendus (a_args) doit être de même
            # Longueur que celle reçue (args)
            if len(a_args) != len(args):
                raise TypeError("le nombre d'arguments attendu n'est pas égal " \
                        "au nombre reçu")
            # On parcourt la liste des arguments reçus et non nommés
            for i, arg in enumerate(args):
                if a_args[i] is not type(args[i]):
                    raise TypeError("l'argument {0} n'est pas du type " \
                            "{1}".format(i, a_args[i]))
            
            # On parcourt à présent la liste des paramètres reçus et nommés
            for cle in kwargs:
                if cle not in a_kwargs:
                    raise TypeError("l'argument {0} n'a aucun type " \
                            "précisé".format(repr(cle)))
                if a_kwargs[cle] is not type(kwargs[cle]):
                    raise TypeError("l'argument {0} n'est pas de type" \
                            "{1}".format(repr(cle), a_kwargs[cle]))
            return fonction_a_executer(*args, **kwargs)
        return fonction_modifiee
    return decorateur

@controler_types(int, int)
# Decorateur défini ci dessus appliquer
# à la methode intervalle

def intervalle(base_inf, base_sup):
    print("Intervalle de {} à {}".format(base_inf, base_sup))
    
