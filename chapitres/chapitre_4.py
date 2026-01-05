import sys
import os
import random
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.input_utils import load_fichier
from univers.personnage import afficher_personnage
from univers.maison import actualiser_points_maison, afficher_maison_gagnante


def creer_equipe(maison, equipe_data, est_joueur=False, joueur=None):
    equipe = {
        "nom": maison,
        "score": 0,
        "a_marque": 0,
        "a_stoppe": 0,
        "attrape_vifdor": False,
        "joueurs": list(equipe_data)
    }

    if est_joueur and joueur:

        nouveaux_joueurs = []
        nom_complet = f"{joueur['Prenom']} {joueur['Nom']} (Attrapeur)"
        nouveaux_joueurs.append(nom_complet)

        if len(equipe_data) > 0:
            nouveaux_joueurs.extend(equipe_data[1:])

        equipe["joueurs"] = nouveaux_joueurs

    return equipe


def tentative_marque(equipe_attaque, equipe_defense, joueur_est_joueur=False):
    proba_but = random.randint(1, 10)

    if proba_but >= 6:

        buteur = ""
        if joueur_est_joueur:

            buteur = equipe_attaque["joueurs"][0]
        else:
            buteur = random.choice(equipe_attaque["joueurs"])

        equipe_attaque["score"] += 10
        equipe_attaque["a_marque"] += 1
        print(f"{buteur} marque un but pour {equipe_attaque['nom']} ! (+10 points)")
    else:

        equipe_defense["a_stoppe"] += 1
        print(f"{equipe_defense['nom']} bloque l'attaque !")


def apparition_vifdor():
    return random.randint(1, 6) == 6


def attraper_vifdor(e1, e2):
    gagnant = random.choice([e1, e2])
    gagnant["score"] += 150
    gagnant["attrape_vifdor"] = True
    print(f"Le Vif d'Or a été attrapé par {gagnant['nom']} ! (+150 points)")
    return gagnant


def afficher_score(e1, e2):
    print("\nScore actuel :")
    print(f"→ {e1['nom']} : {e1['score']} points")
    print(f"→ {e2['nom']} : {e2['score']} points")


def afficher_equipe(maison, equipe):
    print(f"\nÉquipe de {maison} :")
    for j in equipe["joueurs"]:
        print(f"- {j}")


def match_quidditch(joueur, maisons):
    print("\n")
    print("MATCH DE QUIDDITCH")
    print("=")

    chemin_equipes = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "equipes_quidditch.json")
    equipes_data = load_fichier(chemin_equipes)

    if not equipes_data:
        print("Erreur : Impossible de charger les équipes.")
        return

    maison_joueur = joueur.get("Maison", "Gryffondor")

    autres_maisons = [m for m in equipes_data.keys() if m != maison_joueur]
    maison_adverse = random.choice(autres_maisons)

    print(f"Match de Quidditch : {maison_joueur} vs {maison_adverse} !")

    equipe_joueur = creer_equipe(maison_joueur, equipes_data[maison_joueur], est_joueur=True, joueur=joueur)
    equipe_adverse = creer_equipe(maison_adverse, equipes_data[maison_adverse])

    afficher_equipe(maison_joueur, equipe_joueur)
    afficher_equipe(maison_adverse, equipe_adverse)

    print(f"\nTu joues pour {maison_joueur} en tant qu'Attrapeur.")
    input("Appuyez sur Entrée pour commencer le match...")

    match_termine = False
    tour = 1

    while not match_termine and tour <= 20:
        print(f"\n--- Tour {tour} ---")

        tentative_marque(equipe_joueur, equipe_adverse, joueur_est_joueur=True)

        tentative_marque(equipe_adverse, equipe_joueur, joueur_est_joueur=False)

        afficher_score(equipe_joueur, equipe_adverse)

        if apparition_vifdor():
            print("\nLE VIF D'OR EST APERÇU !")
            gagnant_vif = attraper_vifdor(equipe_joueur, equipe_adverse)
            match_termine = True

        if not match_termine:
            input("Appuyez sur Entrée pour continuer...")
            tour += 1

    print("\n")
    print("FIN DU MATCH")
    afficher_score(equipe_joueur, equipe_adverse)

    vainqueur = None
    if equipe_joueur["score"] > equipe_adverse["score"]:
        vainqueur = equipe_joueur
    elif equipe_adverse["score"] > equipe_joueur["score"]:
        vainqueur = equipe_adverse
    else:
        print("Match nul !")

    if vainqueur:
        print(f"La maison gagnante est {vainqueur['nom']} avec {vainqueur['score']} points !")
        print(f"{vainqueur['nom']} remporte le match...")
        print(f"+500 points pour {vainqueur['nom']} !")
        actualiser_points_maison(maisons, vainqueur['nom'], 500)

    afficher_maison_gagnante(maisons)


def lancer_chapitre4_quidditch(joueur, maisons):
    match_quidditch(joueur, maisons)

    print("\n")
    print("Fin du Chapitre 4 — Quelle performance incroyable sur le terrain !")

    afficher_maison_gagnante(maisons)
    afficher_personnage(joueur)

    print("\nFÉLICITATIONS ! VOUS AVEZ TERMINÉ L'AVENTURE POUDELARD (PARTIE 1 & 2) !")
