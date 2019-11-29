
# L"héritage simple

class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
        
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
      # self.nom = nom
        # pose une erreur si on veut recupérer le prenom car non importé dans AgentSpecial
        Personne__init__(self.nom)
        self.matricule = matricule
        
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

agent = AgentSpecial("Fisher", "18327-121")
print(agent.nom)

print(agent)
Agent Fisher, matricule 18327-121
print(agent.prenom)

    # Petite précision

def __setattr__(self, nom_attribut, valeur_attribut):
        """Méthode appelée quand on fait objet.attribut = valeur"""
        print("Attention, on modifie l'attribut {0} de l'objet !".format(nom_attribut))
        object.__setattr__(self, nom_attribut, valeur_attribut)

    # 2 fonction pratiques

        # issubclass
        # isinstance

issubclass(AgentSpecial, Personne) # AgentSpecial herite de Personne
issubclass(AgentSpecial, object)
issubclass(Personne, object)
issubclass(Personne, AgentSpecial) # Ici cela voudrais dire que Personne herite AgentSpecial


#--------------------------------------------------#
# Heritage Mutliple
    #   
class MaClasseHeritee(MaClasseMere1, MaClasseMere2):

    # Recherche des méthodes
#--------------------------------------------------#
# Retour sur les exceptions
    #   Création d'exceptions personnalisées
        
        # Se positionner dans la hiérarchie
class MonException(Exception):
    """Exception levée dans un certain contexte… qui reste à définir"""
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message
    def __str__(self):
        """On renvoie le message"""
        return self.message

    # visible sur interpréteur
raise MonException("OUPS... j'ai tout cassé")

    #--------------------------------------------------#
class ErreurAnalyseFichier(Exception):
    """Cette exception est levée quand un fichier (de configuration)
    n'a pas pu être analysé.
    
    Attributs :
        fichier -- le nom du fichier posant problème
        ligne -- le numéro de la ligne posant problème
        message -- le problème proprement dit"""
    
    def __init__(self, fichier, ligne, message):
        """Constructeur de notre exception"""
        self.fichier = fichier
        self.ligne = ligne
        self.message = message
    def __str__(self):
        """Affichage de l'exception"""
        return "[{}:{}]: {}".format(self.fichier, self.ligne, \
                self.message)
