
from utils.input_utils import demander_nombre

def actualiser_points_maison(maisons, nom_maison, points):

    if nom_maison in maisons:
        maisons[nom_maison] += points
        print(f'{points:+} points pour {nom_maison}. Total actuel : {maisons[nom_maison]} points.')
    else:
        print(f'Erreur : la maison {nom_maison} est introuvable.')


def afficher_maison_gagnante(maisons):

    if not maisons:
        print('Aucune maison à afficher.')
        return


    max_points = max(maisons.values())

    maisons_gagnantes = [nom for nom, points in maisons.items() if points == max_points]

    if len(maisons_gagnantes) == 1:
        print(f'La maison gagnante est {maisons_gagnantes[0]} avec {max_points} points !')
    else:
        maisons_str = ", ".join(maisons_gagnantes)
        print(f'Égalité ! Les maisons ex aequo sont : {maisons_str} avec {max_points} points chacune.')



def repartition_maison(joueur, questions):


    maisons_scores = {
        "Gryffondor": 0,
        "Serpentard": 0,
        "Poufsouffle": 0,
        "Serdaigle": 0
    }


    maisons_scores["Gryffondor"] += joueur.get("Attributs", {}).get("courage", 0) * 2
    maisons_scores["Serpentard"] += joueur.get("Attributs", {}).get("ambition", 0) * 2
    maisons_scores["Poufsouffle"] += joueur.get("Attributs", {}).get("loyauté", 0) * 2
    maisons_scores["Serdaigle"] += joueur.get("Attributs", {}).get("intelligence", 0) * 2


    for texte, choix, maisons_corresp in questions:
        print(texte)
        for i, option in enumerate(choix, start=1):
            print(f'{i}. {option}')
        

        reponse = demander_nombre('Votre choix : ', 1, len(choix))
        

        maison_choisie = maisons_corresp[reponse - 1]
        maisons_scores[maison_choisie] += 3


    max_points = max(maisons_scores.values())
    maisons_gagnantes = [nom for nom, pts in maisons_scores.items() if pts == max_points]


    maison_finale = maisons_gagnantes[0]  
    print(f'\nVous êtes réparti(e) dans la maison : {maison_finale} !')
    return maison_finale



questions = [
    (
        "Tu vois un ami en danger. Que fais-tu ?",
        ["Je fonce l'aider", "Je réfléchis à un plan", "Je cherche de l’aide", "Je reste calme et j’observe"],
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


