import json
import os


def demander_texte(message):
    while True:
        texte = input(message).strip()
        if texte:
            return texte
        print("Veuillez entrer un texte valide (non vide).")


def demander_nombre(message, min_val=None, max_val=None):
    while True:
        saisie = input(message).strip()

        if not (saisie.isdigit() or (saisie.startswith('-') and saisie[1:].isdigit())):
            print("Veuillez entrer un nombre entier valide.")
            continue

        nombre = int(saisie)

        if min_val is not None and nombre < min_val:
            print(f"Le nombre doit être supérieur ou égal à {min_val}.")
            continue

        if max_val is not None and nombre > max_val:
            print(f"Le nombre doit être inférieur ou égal à {max_val}.")
            continue

        return nombre

def demander_choix(message, options):
    print(message)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    choix_idx = demander_nombre("Votre choix : ", 1, len(options))
    return options[choix_idx - 1]


def load_fichier(chemin_fichier):
    if not os.path.exists(chemin_fichier):
        print(f"Erreur : Le fichier {chemin_fichier} est introuvable.")
        return None

    try:
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Erreur : Impossible de décoder le fichier {chemin_fichier}.")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {chemin_fichier} : {e}")
        return None
