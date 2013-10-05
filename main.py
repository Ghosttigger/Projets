#!/usr/bin/env python3
#TODO: améliorer la boucle principale, améliorer la class Joueur(), corriger la class Salle()
def sav(label, nom, desc, sortie="0"):
    """Créer un fichier de sauvegarde de salle avec un nom et une description, ex: sav("test", "exemple","Une description") """
    fichier = open(label, "w")
    fichier.write("[name]"+nom+ "\n" )
    fichier.write("[description]"+desc+ "\n" )
    fichier.write("[sortie]"+sortie)
    fichier.close()
class Joueur():
    """Permet de créer, deplacer le joueur"""
    def __init__(self, nom="Olaf", position="depart"):
        self.nom=nom
        self.position=position
    def __getattr__(self):
        print("attribut non trouvé")
    def __setattr__(self,avant,apres):
        object.__setattr__(self, avant, apres)
    def save(self):
        """Créer un fichier avec le nom du joueur, et son emplacement"""
        fichier = open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n" )
        fichier.write("[position]"+ self.position )
        fichier.close()
    def deplacer(self, destination):
        """Remplace dans la sauvegarde du joueur, sa position par sa destination ex: Joueur.deplacer("Olaf","valhalla")"""
        fichier=open(self.nom, "r")
        position = fichier.readline().rstrip('\n\r').split("[position]")
        x=fichier.read()
        fichier.close()
        position="".join(position)
        x=x.replace(position, destination)
        fichier=open(self.nom, "w")
        fichier.write(x)
        fichier.close()
    def boussole(self):
        """Renvoie la position courante du Joueur grâce à son fichier de sauvegarde"""
        fichier=open(self.nom, "r")
        x = fichier.read().rstrip('\n').split("[name]"+self.nom)
        fichier.close()
        x = "".join(x)
        self.position = x.replace('\n[position]', '')
        return self.position

class Salle():
    """Gère le nom, la description et la sortie des salles, grâce à leurs fichiers de sauvegarde"""
    def __init__(self,label="RAF", nom="", description="", sortie="0"):
        self.nom=nom
        self.description=description
        self.sortie=sortie
        self.label=label
    def __getattr__(self):
        print("attribut non trouvé")
    def __setattr__(self,avant,apres):
        object.__setattr__(self, avant, apres)
    def creer(self, label, nom, desc, sortie="0"):
        """Créer un fichier de sauvegarde de salle avec un nom et une description, ex: sav("test", "exemple","Une description") """
        fichier = open(label, "w")
        fichier.write("[name]"+nom+ "\n" )
        fichier.write("[description]"+desc+ "\n" )
        fichier.write("[sortie]"+sortie)
        fichier.close()
    def nom(self):
        """renvoie le nom de la salle grâce à son fichier de sauvegarde"""
        fichier=open(self.label,"r")
        self.nom = fichier.readline().rstrip('\n\r').split("[name]")
        self.nom = "".join(self.nom)
        fichier.close()
        return self.nom
    def description(self):
        """renvoie la description d'une salle grâce à son fichier de sauvegarde"""
        fichier=open(self.label,"r")
        self.description = fichier.readline().rstrip('\n\r').split("[description]")
        self.description = "".join(description)
        fichier.close()
        return self.description
    def sortie(self):
        """renvoie la sortie d'une salle grâce à son fichier de sauvegarde"""
        fichier=open(self.label,"r")
        self.sortie = fichier.readline().rstrip('\n\r').split("[sortie]")
        self.sortie = "".join(self.sortie)
        fichier.close()
        print(self.sortie)
        return self.sortie

def lire(file):
    """Lit un fichier créé avec la fonction sav() et affiche son nom et sa description"""
    fichier=open(file,"r")
    nom = fichier.readline().rstrip('\n\r').split("[name]")
    description = fichier.readline().rstrip('\n\r').split("[description]")
    sortie = fichier.readline().rstrip('\n\r').split("[sortie]")
    fichier.close()
    nom = "".join(nom)
    description="".join(description)
    sortie="".join(sortie)
    print("===="+nom+"====")
    print(description+"\n")
    print("sorties:")
    print(sortie)


Test=Salle()
Test.creer("depart","exemple","Blablabla","deux")

#Création de la salle DEUX
Deux=Salle()
Deux.creer("deux","exempledeux","abracadabra !","test")

#Création du joueur Bouffblood
j1=Joueur()
j1.nom="Olaf"
j1.save()



continuer=1
while continuer:
    pos=j1.boussole()
    lire(pos)
    Test.sortie="deux"
    j1.deplacer("deux")
    go=input("> ")
    if go == Test.sortie:
        j1.deplacer(go)
    else:
        print("La destination n'existe pas.")
    




