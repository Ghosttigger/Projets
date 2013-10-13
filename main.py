#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from fonctions import *
import sys

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
    fichier=open("quetes", "r")
    for ligne in fichier:
        for quete in j1.quetes:
            if quete in ligne:
                quete_verif = ligne
                quete_verif = quete_verif.rstrip('\n').split("::")
                quete_verif = "".join(quete_verif)
                quete_verif = quete_verif.split(quete)
                quete_verif = "".join(quete_verif)
                exec(open(quete_verif).read())
    fichier.close()
    go = input("> ")
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
    elif go == "quetes":
        for i in j1.quetes:
            i = "".join(i)
            print("Quête en cours : " + i)
    for i in Room.sortie:
        i = "".join(i)
        if go == i:
            j1.deplacer(go)
        elif go != "inventaire" and go != "quetes":
            print("Cette destination n'existe pas")
