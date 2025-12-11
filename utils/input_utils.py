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
