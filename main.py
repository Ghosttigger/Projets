#!/usr/bin/env python3

import sys

class Joueur():
    """Gère tout ce qui est relatif au joueur"""
    def __init__(self, nom="Olaf", position="depart", inventaire=""):
        self.nom=nom
        self.position=position
        self.inventaire=inventaire
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
        self.inventaire = fichier.readline().rstrip('\n\r').split("[inventaire]")
        self.inventaire = "".join(self.inventaire)
        self.inventaire = self.inventaire.split(',')
        fichier.close()
    def deplacer(self, destination):
        """Remplace dans la sauvegarde du joueur, sa position par sa destination ex: Joueur.deplacer("Olaf","valhalla")"""
        self.position=self.position.replace(self.position, destination)
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n") #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position + "\n")
        fichier.write("[inventaire]"+ ",".join(self.inventaire))
        fichier.close()
    def boussole(self):
        """Renvoie la position courante du Joueur grâce à son fichier de sauvegarde"""
        fichier=open(self.nom, "r")
        x = fichier.read().rstrip('\n\r').split("[name]"+self.nom + "\n")
        fichier.close()
        x = "".join(x)
        return self.position
    def ajouter(self, objet):
        """Ajoute un objet à l'inventaire, et l'enregistre dans le fichier du joueur"""
        self.inventaire.append(objet)
        self.inventaire.sort()
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n") #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position + "\n")
        fichier.write("[inventaire]"+ ",".join(self.inventaire))
        fichier.close()
    def enlever(self, objet):
        """Enlève un objet à l'inventaire, et enregistre les modifications dans le fichier du joueur"""
        self.inventaire.remove(objet)
        self.inventaire.sort()
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n") #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position + "\n")
        fichier.write("[inventaire]"+ ",".join(self.inventaire))
        fichier.close()        

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
        self.sortie = self.sortie.split(',')
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
    j1.update()
    Room.label = j1.boussole()
    Room.update()
    lire(j1.boussole())
    go = input("> ")
    x = Room.sortie.count(go)
    if go == "exit":
        sys.exit()
    elif go == "inventaire":
        i=0
        while i < len(j1.inventaire):
            if i < len(j1.inventaire) and j1.inventaire[i+1] != j1.inventaire[i]: #Si l'objet suivant n'est pas le même et que l'on est pas au bout de l'inventaire
                y = j1.inventaire.count(j1.inventaire[i])
                print("Vous avez %d %s dans votre sac" %(y, j1.inventaire[i]))
            else: #Sinon on compte le nombre de fois ou cet objet est présent et on met le compteur sur le prochain objet différent
                y = j1.inventaire.count(j1.inventaire[i])
                if i+y < len(j1.inventaire):
                    print("Vous avez %d %s dans votre sac" %(y, j1.inventaire[i]))
                    i += y
                    print("Vous avez %d %s dans votre sac" %(y, j1.inventaire[i]))
                else:
                    i = len(j1.inventaire)
                
            i += 1
    c = -1
    for i in Room.sortie:
        c += 1
        i = "".join(i)
        if go == i :
            j1.deplacer(go)
        elif x == 0 and go != "inventaire":
            print("Cette destination n'existe pas")



