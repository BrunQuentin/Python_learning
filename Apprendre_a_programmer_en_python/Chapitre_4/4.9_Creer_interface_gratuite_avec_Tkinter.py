#   1.  Présentation de Tkinter
#   2.  Première interface graphique
#   3.  De nombreux widgets
#   4.  Les commandes
############################################

#   2.
"""Premier exemple avec Tkinter.

On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

"""

# On importe Tkinter
from tkinter import *

    # On crée une fenêtre, racine de notre interface
#fenetre = Tk()

    # On crée un label (ligne de texte) souhaitant la bienvenue
    # Note : le premier paramètre passé au constructeur de Label est notre
    # interface racine
#champ_label = Label(fenetre, text="Salut les Zér0s !")

    # On affiche le label dans la fenêtre
#champ_label.pack()

#champ_label["text"]
#print(champ_label["text"])
#champ_label["text"]= "Maintenant au revoir !"
#print(champ_label["text"])

    # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
#fenetre.mainloop()


#------------------------------------------#

#   3.  Les Widgets
    #   Labels,
fenetre = Tk()
champ_label_2 = Label(fenetre, text="contenu de notre champ label")
champ_label_2.pack()

    #   Boutons
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack()

    # Ligne de saisi de texte
var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()

    # case à cocher
var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()
var_case.get() # vaut 1 si non coché sinon 0

    # Boutons radios
var_choix = StringVar()

choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

var_choix.get()

    # Listes déroulantes
liste = Listbox(fenetre)
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")
liste.pack()

    # organiser ses widgets dans la fenetres
cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X)


#
fenetre.mainloop()

#------------------------------------------#

#   4. Les commandes

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.nb_clic = 0
        
        # Création de nos widgets
        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")
        self.message.pack()
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",
                command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
    
    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        
        On change la valeur du label message."""
        
        self.nb_clic += 1
        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)

    #------------------------------------------#
#   Creation interface:
fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()

