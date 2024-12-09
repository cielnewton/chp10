import os

# Nom du répertoire à parcourir
repertoire = "."  # Utilisez "." pour le répertoire courant ou spécifiez un chemin absolu ou relatif

# Préfixe à ajouter aux noms de fichiers
prefixe = "prefixe_"

# Lister tous les fichiers dans le répertoire
try:
    fichiers = os.listdir(repertoire)
except OSError as e:
    print(f"Erreur lors de la lecture du répertoire : {e}")
    fichiers = []

# Renommer les fichiers en ajoutant le préfixe
for fichier in fichiers:
    ancien_chemin = os.path.join(repertoire, fichier)
    nouveau_nom = prefixe + fichier
    nouveau_chemin = os.path.join(repertoire, nouveau_nom)

    # Vérifier si l'élément est un fichier avant de le renommer
    if os.path.isfile(ancien_chemin):
        try:
            os.rename(ancien_chemin, nouveau_chemin)
            print(f"Renommé : {ancien_chemin} -> {nouveau_chemin}")
        except OSError as e:
            print(f"Erreur lors du renommage de {ancien_chemin} : {e}")
    else:
        print(f"{ancien_chemin} n'est pas un fichier, ignoré.")
