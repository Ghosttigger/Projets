Games
=====

Moteur de "livre dont vous êtes le héros"

Statut: en dévellopement

Les fichiers de sauvegarde doivent se présenter sous cette forme:

Salles:
=======

    [name]nom-de-la-salle
    [description]sa-description
    [sortie]sortie1,sortie2
    [image]image-de-la-salle.png


Personnages:
============

    [name]nom-du-personnage
    [position]sa-position-courante


Quêtes:
=======
Pour le fichier de correspondance quête/fichier:

Nom-de-la-quete::nom-du-fichier

exemple:

    la grosse pomme::001

------------------------------------------------------------------------------------------------------------------------

Pour les fichiers de quête:

exemple:

Le coffre au trésor :

    from fonctions import *
    if j1.position == "depart":
        try:
            j1.inventaire.index("clef")
        except:
            print("Quête - Le coffre au trésor : Vous ne possédez pas la clef !")
        else:
            print("Vous ouvrez un coffre: il contient 10 000 piastres !")
            j1.enlever_quete("Le coffre au trésor")
