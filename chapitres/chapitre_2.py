import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_utils import demander_choix, load_fichier
from univers.maison import repartition_maison
from univers.personnage import afficher_personnage

def rencontrer_amis(joueur):
    print("\n" + "*"*50)
    print("Vous montez à bord du Poudlard Express. Le train démarre lentement en direction du Nord...")
    print("*"*50)
    

    print("\nUn garçon roux entre dans votre compartiment, l'air amical.")
    print("– Salut ! Moi c'est Ron Weasley. Tu veux bien qu'on s'assoie ensemble ?")
    
    choix_ron = demander_choix("Que répondez-vous ?", ["Bien sûr, assieds-toi !", "Désolé, je préfère voyager seul."])
    
    if choix_ron == "Bien sûr, assieds-toi !":
        print("Ron sourit : — Génial ! Tu verras, Poudlard, c'est incroyable !")
        joueur['Attributs']['loyauté'] += 1
    else:
        print("Ron hausse les épaules et s'en va.")
        joueur['Attributs']['ambition'] += 1
        

    print("\nUne fille entre ensuite, portant déjà une pile de livres.")
    print("— Bonjour, je m'appelle Hermione Granger. Vous avez déjà lu 'Histoire de la Magie' ?")
    
    choix_hermione = demander_choix("Que répondez-vous ?", ["Oui, j'adore apprendre de nouvelles choses !", "Euh… non, je préfère les aventures aux bouquins."])
    
    if choix_hermione == "Oui, j'adore apprendre de nouvelles choses !":
        print("Hermione sourit : — C'est fascinant, n'est-ce pas ?")
        joueur['Attributs']['intelligence'] += 1
    else:
        print("Hermione fronce les sourcils : — Il faudrait pourtant s'y mettre un jour !")
        joueur['Attributs']['courage'] += 1
        

    print("\nPuis un garçon blond entre avec un air arrogant.")
    print("— Je suis Drago Malefoy. Mieux vaut bien choisir ses amis dès le départ, tu ne crois pas ?")
    
    choix_drago = demander_choix("Comment réagissez-vous ?", ["Je lui serre la main poliment.", "Je l'ignore complètement.", "Je lui réponds avec arrogance."])
    
    if choix_drago == "Je lui serre la main poliment.":
        print("Drago hoche la tête avec satisfaction.")
        joueur['Attributs']['ambition'] += 1
    elif choix_drago == "Je l'ignore complètement.":
        print("Drago semble vexé par votre indifférence.")
        joueur['Attributs']['loyauté'] += 1
    else:
        print("Drago fronce les sourcils, vexé. — Tu le regretteras !")
        joueur['Attributs']['courage'] += 1
        
    print("\nLe train continue sa route. Le château de Poudlard se profile à l'horizon...")
    print(f"Tes attributs mis à jour : {joueur['Attributs']}")

def mot_de_bienvenue():
    print("\n" + "="*50)
    print("Vous arrivez enfin à Poudlard !")
    print("Le Professeur Dumbledore se lève pour son discours de bienvenue :")
    print("« Bienvenue à tous ! Que cette année soit riche en apprentissage et en magie ! »")
    print("="*50 + "\n")
    input("Appuyez sur Entrée pour commencer la Répartition...")

def ceremonie_repartition(joueur):
    print("\nLa cérémonie de répartition commence dans la Grande Salle...")
    
    questions = [
        (
            "Tu vois un ami en danger. Que fais-tu ?",
            ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l'aide", "Je reste calme et j'observe"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Quel trait te décrit le mieux ?",
            ["Courageux et loyal", "Rusé et ambitieux", "Patient et travailleur", "Intelligent et curieux"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        ),
        (
            "Face à un défi difficile, tu...",
            ["Fonces sans hésiter", "Cherches la meilleure stratégie", "Comptes sur tes amis", "Analyses le problème"],
            ["Gryffondor", "Serpentard", "Poufsouffle", "Serdaigle"]
        )
    ]
    
    maison = repartition_maison(joueur, questions)
    joueur['Maison'] = maison
    
    print(f"\nLe Choixpeau s'exclame : {maison.upper()} !!!")
    print(f"Tu rejoins les élèves de {maison} sous les acclamations !")
    return maison

def installation_salle_commune(joueur):
    print("\nVous suivez les préfets à travers les couloirs du château...")
    
    chemin_maisons = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "maisons.json")
    maisons_data = load_fichier(chemin_maisons)
    
    if maisons_data and joueur['Maison'] in maisons_data:
        info = maisons_data[joueur['Maison']]
        print(info['description'])
        print(f"Les couleurs de votre maison : {info['couleurs']}")
    else:
        print(f"Bienvenue dans la salle commune de {joueur['Maison']}.")

def lancer_chapitre_2(joueur):
    rencontrer_amis(joueur)
    mot_de_bienvenue()
    ceremonie_repartition(joueur)
    installation_salle_commune(joueur)
    
    print("\n" + "*"*50)
    print("Fin du Chapitre 2 ! Les cours vont bientôt commencer...")
    print("*"*50 + "\n")
    
    afficher_personnage(joueur)
    input("Appuyez sur Entrée pour continuer vers le Chapitre 3...")
