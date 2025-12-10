from utils.input_utils import demander_texte, demander_nombre, demander_choix, load_fichier
from univers.personnage import initialiser_personnage, afficher_personnage, modifier_argent, ajouter_object
import time
import sys
import os

def introduction():
    print("\n" + "*"*50)
    print("CHAPITRE 1 : L'ARRIVÉE DANS LE MONDE MAGIQUE")
    print("*"*50)
    print("\nBienvenue, jeune sorcier(e). Votre aventure est sur le point de commencer.")
    input("Appuyez sur Entrée pour continuer...")

def creer_personnage():
    print("\n--- CRÉATION DU PERSONNAGE ---")
    nom = demander_texte("Entrez le nom de votre personnage : ")
    prenom = demander_texte("Entrez le prénom de votre personnage : ")
    
    print("\nChoisissez vos attributs (1-10) :")
    courage = demander_nombre("Niveau de courage (1-10) : ", 1, 10)
    intelligence = demander_nombre("Niveau d'intelligence (1-10) : ", 1, 10)
    loyaute = demander_nombre("Niveau de loyauté (1-10) : ", 1, 10)
    ambition = demander_nombre("Niveau d'ambition (1-10) : ", 1, 10)
    
    attributs = {
        "courage": courage,
        "intelligence": intelligence,
        "loyauté": loyaute,
        "ambition": ambition
    }
    
    joueur = initialiser_personnage(nom, prenom, attributs)
    afficher_personnage(joueur)
    return joueur

def recevoir_lettre():
    print("\nUne chouette traverse la fenêtre et vous apporte une lettre scellée du sceau de Poudlard...")
    print("« Cher élève,")
    print("Nous avons le plaisir de vous informer que vous avez été admis à l'école de sorcellerie de Poudlard ! »")
    
    choix = demander_choix("\nSouhaitez-vous accepter cette invitation et partir pour Poudlard ?", 
                           ["Oui, bien sûr !", "Non, je préfère rester avec l'oncle Vernon..."])
    
    if choix == "Non, je préfère rester avec l'oncle Vernon...":
        print("\nVous déchirez la lettre, l'oncle Vernon pousse un cri de joie:")
        print("« EXCELLENT ! Enfin quelqu'un de NORMAL dans cette maison ! »")
        print("Le monde magique ne saura jamais que vous existiez... Fin du jeu.")
        sys.exit(0)
    else:
        print("\nVous préparez vos affaires avec excitation !")

def rencontrer_hagrid(personnage):
    print("\nSoudain, quelqu'un frappe à la porte avec force !")
    print("Un géant barbu entre en fracassant presque l'encadrement.")
    print("Hagrid : 'Salut ! Je suis venu t'aider à faire tes achats sur le Chemin de Traverse.'")
    
    choix = demander_choix("\nVoulez-vous suivre Hagrid ?", ["Oui", "Non"])
    
    if choix == "Non":
        print("\nHagrid insiste gentiment et vous entraîne quand même avec lui !")
    
    print("\nVous suivez Hagrid vers Londres et le Chaudron Baveur...")

def acheter_fournitures(personnage):
    print("\n--- LE CHEMIN DE TRAVERSE ---")
    print("Bienvenue sur le Chemin de Traverse !")
    
    # Chargement de l'inventaire
    chemin_inventaire = os.path.join(os.path.dirname(__file__), "..", "data", "inventaire.json")
    donnees_inventaire = load_fichier(chemin_inventaire)
    
    if not donnees_inventaire:
        print("Erreur critique : Impossible de charger l'inventaire.")
        return

    # Adaptation au nouveau format : "ID": ["Nom", Prix]
    # On reconstruit un dictionnaire {Nom: Prix} pour la logique d'achat
    fournitures = {}
    # Le fichier peut être une liste ou un dict selon le format exact, ici on gère le dict "1": [...]
    if isinstance(donnees_inventaire, dict):
        for key, val in donnees_inventaire.items():
            if isinstance(val, list) and len(val) >= 2:
                fournitures[val[0]] = val[1]
    
    # Animaux (absents du nouveau JSON, on les définit ici)
    animaux = {
        "Chouette": 20,
        "Chat": 15,
        "Rat": 10,
        "Crapaud": 5
    }
    
    objets_obligatoires = ["Baguette magique", "Robe de sorcier", "Manuel de potions"]
    achats_effectues = []
    
    # Achat des fournitures
    while True:
        restant = [obj for obj in objets_obligatoires if obj not in achats_effectues]
        if not restant:
            print("\nTous les objets obligatoires ont été achetés !")
            break
            
        print(f"\nVous avez {personnage['Argent']} gallions.")
        print(f"Objets obligatoires restant à acheter : {', '.join(restant)}")
        
        print("\nCatalogue des objets disponibles :")
        liste_objets = list(fournitures.keys())
        for i, obj in enumerate(liste_objets, 1):
            print(f"{i}. {obj} – {fournitures[obj]} gallions")
            
        choix_idx = demander_nombre("\nEntrez le numéro de l'objet à acheter : ", 1, len(liste_objets))
        objet_choisi = liste_objets[choix_idx - 1]
        prix = fournitures[objet_choisi]
        
        if objet_choisi in achats_effectues:
            print(f"Vous avez déjà acheté {objet_choisi}.")
            continue
            
        if personnage['Argent'] >= prix:
            modifier_argent(personnage, -prix)
            ajouter_object(personnage, "Inventaire", objet_choisi)
            achats_effectues.append(objet_choisi)
            print(f"Vous avez acheté : {objet_choisi} (-{prix} gallions).")
        else:
            print("Vous n'avez pas assez d'argent !")
            if objet_choisi in objets_obligatoires:
                 print("C'est un objet obligatoire ! Vous ne pouvez pas continuer sans.")
                 if personnage['Argent'] < min([fournitures[o] for o in restant]):
                     print("Vous n'avez plus assez d'argent pour acheter vos fournitures scolaires.")
                     print("Poudlard ne peut pas vous accepter sans équipement. Fin du jeu.")
                     sys.exit(0)

    # Achat de l'animal
    print("\nIl est temps de choisir votre animal de compagnie pour Poudlard !")
    print(f"Vous avez {personnage['Argent']} gallions.")
    print("Voici les animaux disponibles :")
    
    liste_animaux = list(animaux.keys())
    animal_choisi_nom = demander_choix("Quel animal voulez-vous ?", liste_animaux)
    prix_animal = animaux[animal_choisi_nom]
    
    if personnage['Argent'] >= prix_animal:
        modifier_argent(personnage, -prix_animal)
        ajouter_object(personnage, "Inventaire", animal_choisi_nom)
        print(f"Vous avez choisi : {animal_choisi_nom} (-{prix_animal} gallions).")
    else:
        print("Vous n'avez pas assez d'argent pour cet animal. Vous partirez sans animal de compagnie.")

    print("\nTous les achats sont terminés !")
    afficher_personnage(personnage)

def lancer_chapitre_1():
    introduction()
    joueur = creer_personnage()
    recevoir_lettre()
    rencontrer_hagrid(joueur)
    acheter_fournitures(joueur)
    
    print("\n" + "*"*50)
    print("Fin du Chapitre 1 ! Votre aventure commence à Poudlard...")
    print("*"*50)
    input("Appuyez sur Entrée pour continuer...")
    
    return joueur
