def initialiser_personnage(nom, prenom, attributs):
    joueur = {
        "Nom": nom,
        "Prenom": prenom,
        "Argent": 100,
        "Inventaire": [],
        "Sortilèges": [],
        "Attributs": attributs,
        "Maison": None
    }
    return joueur


def afficher_personnage(joueur):
    print("\n" + "=" * 30)
    print("PROFIL DU PERSONNAGE")
    print("=" * 30)
    print(f"Nom : {joueur['Nom']}")
    print(f"Prénom : {joueur['Prenom']}")
    print(f"Argent : {joueur['Argent']} gallions")

    print("Inventaire :")
    if joueur['Inventaire']:
        print(", ".join(joueur['Inventaire']))
    else:
        print("(Vide)")

    print("Sortilèges :")
    if joueur['Sortilèges']:

        if all(isinstance(s, str) for s in joueur['Sortilèges']):
            print(", ".join(joueur['Sortilèges']))

        else:
            print(", ".join([s['nom'] for s in joueur['Sortilèges']]))
    else:
        print("(Aucun)")

    print("Attributs :")
    for attr, val in joueur['Attributs'].items():
        print(f"- {attr} : {val}")

    if joueur.get("Maison"):
        print(f"Maison : {joueur['Maison']}")
    print("=" * 30 + "\n")

def modifier_argent(joueur, montant):

    joueur['Argent'] += montant


def ajouter_object(joueur, cle, objet):

    if cle in ["Inventaire", "Sortilèges"]:
        joueur[cle].append(objet)
    else:
        print(f"Erreur : Clé '{cle}' invalide pour l'ajout d'objet.")

