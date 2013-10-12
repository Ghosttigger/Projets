#!/usr/bin/env python3
#TODO: améliorer la boucle principale, améliorer la class Joueur(), corriger la class Salle(),
import sys

def sav(label, nom, desc, sortie="0"):
    """Créer un fichier de sauvegarde de salle avec un nom et une description, ex: sav("test", "exemple","Une description") """
    fichier = open("salle/"+label, "w")
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
    def update(self):
        """Créer un fichier avec le nom du joueur, et son emplacement"""
        fichier = open(self.nom, "r")
        self.nom = fichier.readline().rstrip('\n\r').split("[name]")
        self.nom = "".join(self.nom)
        self.position = fichier.readline().rstrip('\n\r').split("[position]")
        self.position = "".join(self.position)
        fichier.close()
    def deplacer(self, destination):
        """Remplace dans la sauvegarde du joueur, sa position par sa destination ex: Joueur.deplacer("Olaf","valhalla")"""
        self.position=self.position.replace(self.position, destination)
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n" ) #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position)
        fichier.close()
    def boussole(self):
        """Renvoie la position courante du Joueur grâce à son fichier de sauvegarde"""
        fichier=open(self.nom, "r")
        x = fichier.read().rstrip('\n\r').split("[name]"+self.nom + "\n")
        fichier.close()
        x = "".join(x)
        self.position = x.replace('[position]', '')
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
    def update(self):
        """Créer un fichier de sauvegarde de salle avec un nom et une description, ex: sav("test", "exemple","Une description") """
        fichier = open(self.label, "r")
        self.nom = fichier.readline().rstrip('\n\r').split("[name]")
        self.nom = "".join(self.nom)
        self.position = fichier.readline().rstrip('\n\r').split("[description]")
        self.description = "".join(self.description)
        self.sortie = fichier.readline().rstrip('\n\r').split("[sortie]")
        self.sortie = "".join(self.sortie)
        self.sortie = self.sortie.split(' ')
        fichier.close()
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
    print("===="+nom+"====\n")
    print(description+"\n")
    print("sorties:")
    print(sortie)

#Création de la salle courante
Room=Salle()
#Création du joueur 1
j1=Joueur()
j1.update()

continuer=1
while continuer:
    Room.label = j1.boussole()
    Room.update()
    lire(j1.boussole())
    go = input("> ")
    x = Room.sortie.count(go)
    if go == "exit":
        sys.exit()
    compteur = -1
    for i in Room.sortie:
        compteur += 1
        i = "".join(i)
        if go == i:
            j1.deplacer(go)
        elif x == 0:
            print("Cette destination n'existe pas")
