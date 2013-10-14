#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import pygame
from pygame.locals import *
pygame.init()

class Joueur():
    """Gère tout ce qui est relatif au joueur"""
    def __init__(self, nom="Olaf", position="depart", inventaire="", quetes=""):
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
        self.quetes = fichier.readline().rstrip('\n\r').split("[quetes]")
        self.quetes = "".join(self.quetes)
        self.quetes = self.quetes.split(',')
        fichier.close()
    def deplacer(self, destination):
        """Remplace dans la sauvegarde du joueur, sa position par sa destination ex: Joueur.deplacer("Olaf","valhalla")"""
        self.position=self.position.replace(self.position, destination)
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n") #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position + "\n")
        fichier.write("[inventaire]"+ ",".join(self.inventaire) + "\n")
        fichier.write("[quetes]"+ ",".join(self.quetes))
        fichier.close()
    def boussole(self):
        """Renvoie la position courante du Joueur grâce à son fichier de sauvegarde"""
        fichier=open(self.nom, "r")
        x = fichier.read().rstrip('\n\r').split("[name]"+self.nom + "\n")
        fichier.close()
        x = "".join(x)
        return self.position
    def ajouter_objet(self, objet):
        """Ajoute un objet à l'inventaire, et l'enregistre dans le fichier du joueur"""
        self.inventaire.append(objet)
        self.inventaire.sort()
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n") #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position + "\n")
        fichier.write("[inventaire]"+ ",".join(self.inventaire) + "\n")
        fichier.write("[quetes]"+ ",".join(self.quetes))
        fichier.close()
    def enlever_objet(self, objet):
        """Enlève un objet à l'inventaire, et enregistre les modifications dans le fichier du joueur"""
        self.inventaire.remove(objet)
        self.inventaire.sort()
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n") #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position + "\n")
        fichier.write("[inventaire]"+ ",".join(self.inventaire) + "\n")
        fichier.write("[quetes]"+ ",".join(self.quetes))
        fichier.close()
    def ajouter_quete(self, quete):
        """Ajoute un objet à l'inventaire, et l'enregistre dans le fichier du joueur"""
        self.quetes.append(quete)
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n") #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position + "\n")
        fichier.write("[inventaire]"+ ",".join(self.inventaire) + "\n")
        fichier.write("[quetes]"+ ",".join(self.quetes))
        fichier.close()
    def enlever_quete(self, quete):
        """Enlève un objet à l'inventaire, et enregistre les modifications dans le fichier du joueur"""
        self.quetes.remove(quete)
        fichier=open(self.nom, "w")
        fichier.write("[name]"+ self.nom + "\n") #à cause de l'option "w", obligé de réécrire le fichier
        fichier.write("[position]"+self.position + "\n")
        fichier.write("[inventaire]"+ ",".join(self.inventaire) + "\n")
        fichier.write("[quetes]"+ ",".join(self.quetes))
        fichier.close()

class Salle():
    """Gère le nom, la description et la sortie des salles, grâce à leurs fichiers de sauvegarde"""
    def __init__(self,label="RAF", nom="", description="", sortie="0", image=""):
        self.nom=nom
        self.description=description
        self.sortie=sortie
        self.label=label
        self.image=image
    def __getattr__(self):
        print("attribut non trouvé")
    def __setattr__(self,avant,apres):
        object.__setattr__(self, avant, apres)
    def update(self):
        """Met à jour les attributs de la salle grâce à son fichier"""
        fichier = open(self.label, "r")
        self.nom = fichier.readline().rstrip('\n\r').split("[name]")
        self.nom = "".join(self.nom)
        self.position = fichier.readline().rstrip('\n\r').split("[description]")
        self.description = "".join(self.description)
        self.sortie = fichier.readline().rstrip('\n\r').split("[sortie]")
        self.sortie = "".join(self.sortie)
        self.sortie = self.sortie.split(',')
        self.image = fichier.readline().rstrip('\n\r').split("[image]")
        self.image = "".join(self.image)
        fichier.close()

def lire(file):
    """Lit un fichier de salle et affiche son nom et sa description"""
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
