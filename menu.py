from utils.input_utils import demander_choix
from chapitres.chapitre_1 import lancer_chapitre_1
from chapitres.chapitre_2 import lancer_chapitre_2
from chapitres.chapitre_3 import lancer_chapitre_3
from chapitres.chapitre_4 import lancer_chapitre4_quidditch
import sys

def afficher_menu_principal():
    print("\n" + "="*30)
    print("MENU PRINCIPAL - POUDLARD")
    print("="*30)
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
            # Chapitre 1
            joueur = lancer_chapitre_1()
            
            # Chapitre 2
            lancer_chapitre_2(joueur)
            
            # Chapitre 3
            lancer_chapitre_3(joueur, maisons)
            
            # Chapitre 4
            lancer_chapitre4_quidditch(joueur, maisons)
            
        elif choix == "2":
            print("Au revoir et à bientôt dans le monde magique !")
            break
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
