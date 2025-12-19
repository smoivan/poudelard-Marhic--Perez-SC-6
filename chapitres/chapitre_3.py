import sys
import os
import random
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_utils import demander_texte, load_fichier
from univers.personnage import afficher_personnage, ajouter_object
from univers.maison import actualiser_points_maison, afficher_maison_gagnante


def apprendre_sorts(joueur, chemin_fichier=None):
    if chemin_fichier is None:
        chemin_fichier = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "sorts.json")

    sorts_data = load_fichier(chemin_fichier)
    if not sorts_data:
        print("Erreur : Impossible de charger les sorts.")
        return

    print("\n")
    print("Tu commences tes cours de magie à Poudlard...")


    offensifs = [s for s in sorts_data if s['type'] == 'Offensif']
    defensifs = [s for s in sorts_data if s['type'] == 'Défensif']
    utilitaires = [s for s in sorts_data if s['type'] == 'Utilitaire']

    sorts_appris = []

    if offensifs:
        sorts_appris.append(random.choice(offensifs))
    if defensifs:
        sorts_appris.append(random.choice(defensifs))

    if len(utilitaires) >= 3:
        sorts_appris.extend(random.sample(utilitaires, 3))
    else:
        sorts_appris.extend(utilitaires)

    for sort in sorts_appris:
        ajouter_object(joueur, "Sortilèges", sort)
        print(f"\nTu viens d'apprendre le sortilège : {sort['nom']} ({sort['type']})")
        input("Appuie sur Entrée pour continuer...")

    print("\nTu as terminé ton apprentissage de base à Poudlard !")
    print("Voici les sortilèges que tu maîtrises désormais :")
    for sort in sorts_appris:
        print(f"- {sort['nom']} ({sort['type']}) : {sort['description']}")


def quiz_magie(joueur, chemin_fichier=None):
    if chemin_fichier is None:
        chemin_fichier = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "quiz_magie.json")

    questions_data = load_fichier(chemin_fichier)
    if not questions_data:
        print("Erreur : Impossible de charger le quiz.")
        return 0

    print("\n")
    print("Bienvenue au quiz de magie de Poudlard !")
    print("Réponds correctement aux 4 questions pour faire gagner des points à ta maison.")


    questions_posees = []
    if len(questions_data) >= 4:
        questions_posees = random.sample(questions_data, 4)
    else:
        questions_posees = questions_data

    score_quiz = 0

    for i, q in enumerate(questions_posees, 1):
        print(f"\n{i}. {q['question']}")
        reponse_joueur = demander_texte("> ")

        if reponse_joueur.lower().strip() == q['reponse'].lower().strip():
            print("Bonne réponse ! +25 points pour ta maison.")
            score_quiz += 25
        else:
            print(f"Mauvaise réponse. La bonne réponse était : {q['reponse']}")

    print(f"\nScore obtenu au quiz : {score_quiz} points")
    return score_quiz


def lancer_chapitre_3(joueur, maisons):
    apprendre_sorts(joueur)

    points_gagnes = quiz_magie(joueur)

    if joueur.get('Maison'):
        actualiser_points_maison(maisons, joueur['Maison'], points_gagnes)

    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)

    print("\n" +)
    print("Fin du Chapitre 3 ! Préparez-vous pour le Quidditch...")
    print("\n")
    input("Appuyez sur Entrée pour continuer vers le Chapitre 4...")
