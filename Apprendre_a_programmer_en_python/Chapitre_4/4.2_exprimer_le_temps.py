
#   1.  Le module time
import time
#   2.  Le module datetime
import datetime

    #   2.1 une date
    #   2.2 une heure
    #   2.3 date & heures
#-------------------------------------------------#
#   1.1 date & heure dans un nombre unique

tps_en_nbr = time.time()
print(tps_en_nbr)
print("-----Temps en nombre----")

# Exemple fait sur console
debut = time.time()
print("On attend quelques secondes avant de taper la commande suivante".format(debut))
t = 3 
time.sleep(t) # permet de mettre en pause de "x" sec dans le programme (1.4)

fin = time.time()
print(" debut du chrono {0} \n fin du chrono {1}".format(debut, fin))
#1297642195.45 1297642202.27
debut < fin
#True
diff = fin - debut # Combien de secondes entre debut et fin ?
print(" Il s'est ecoulé {} entre le début et la fin \n ".format(diff))
print("-------------------------------")
#-------------------------------------------------#
#   1.2 date & heure de facçon plus présentable
local =time.localtime()
print(local)
print("-- Local time ---")
tps_1 = time.localtime(debut)
print(tps_1)
print("-- Temps précis 1 ---")
tps_2 = time.localtime(fin)
print(tps_2)
print("-- Temps précis 2 ---")

#   1.3 Recupérer un timestamp depuis une date
print(debut)
tps_01 = time.localtime(debut)
print(tps_01)
ts_debut = time.mktime(tps_01)
print("Voici un timestamp récupérer depuis une date \n {} \n--------------".format(ts_debut))

#   1.5 Formater un temps
temps_fr = time.strftime("%A %d %B %Y %H:%M:%S")
print("voici comment est afficher la date en france : \n {} \n ------------".format(temps_fr))

#-------------------------------------------------#
#   2.1
date = datetime.date(2010, 12, 25)
print("Voici une date a ne pas oublier, le : {} \n ".format(date))
print("-- Date d'aujourd'hui --")
ajd = datetime.date.today()
print("Aujourd'hui nous sommes le : {} \n ".format(ajd))
#-------------------------------------------------#
#   2.2
# représenter par 5 paramètre (classe time du module datetime est utilisé ici

#hour(0 par défaut) : les heures, valeur comprise entre 0 et 23 ;

#minute(0 par défaut) : les minutes, valeur comprise entre 0 et 59 ;

#second(0 par défaut) : les secondes, valeur comprise entre 0 et 59 ;

#microsecond(0 par défaut) : la précision de l'heure en micro-secondes,
#entre 0 et 1.000.000 ;

#tzinfo(None par défaut) : l'information de fuseau horaire

#-------------------------------------------------#
#   2.3
mtn = datetime.datetime.now()
print(mtn)
