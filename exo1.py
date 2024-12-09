import os

def lister_contenu_recursif(chemin_dossier):
    contenu = os.listdir(chemin_dossier)
    print(contenu)
    for element in contenu:
        chemin_complet = os.path.join(chemin_dossier, element)
        if os.path.isdir(chemin_complet):
            print(f"Dossier : {chemin_complet}")
    #         # Appel récursif pour parcourir les sous-dossiers
            lister_contenu_recursif(chemin_complet)
        else:
            print(f"Fichier : {chemin_complet}")
