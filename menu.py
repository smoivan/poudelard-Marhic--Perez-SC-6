from utils.input_utils import demander_choix
from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
#from chapitres.chapitre_4 import lancer_chapitre_4
import sys

def afficher_menu_principal():

    print("MENU PRINCIPAL - POUDLARD")

    print("1. Lancer l'aventure (Chapitres 1 à 4)")
    print("2. Quitter le jeu")

def lancer_choix_menu():
    maisons = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }
    
    while True:
        afficher_menu_principal()
        choix = input("\nVotre choix : ").strip()
        
        if choix == "1":

            joueur = lancer_chapitre_1()
            

            lancer_chapitre_2(joueur)
            

            lancer_chapitre_3(joueur, maisons)
            

            #lancer_chapitre_4(joueur, maisons)
            
        elif choix == "2":
            print("Au revoir et à bientôt dans le monde magique !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
