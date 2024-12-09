import os

# Nom du répertoire à parcourir
repertoire = "."  # Utilisez "." pour le répertoire courant ou spécifiez un chemin absolu ou relatif

# Lister tous les éléments dans le répertoire
try:
    elements = os.listdir(repertoire)
except OSError as e:
    print(f"Erreur lors de la lecture du répertoire : {e}")
    elements = []

# Séparer les fichiers et les dossiers
fichiers = []
dossiers = []

for element in elements:
    chemin_complet = os.path.join(repertoire, element)
    if os.path.isfile(chemin_complet):
        fichiers.append(element)
    elif os.path.isdir(chemin_complet):
        dossiers.append(element)

# Afficher les fichiers
if fichiers:
    print("Fichiers dans le répertoire :")
    for fichier in fichiers:
        print(fichier)
else:
    print("Aucun fichier trouvé dans le répertoire.")

# Afficher les dossiers
if dossiers:
    print("Dossiers dans le répertoire :")
    for dossier in dossiers:
        print(dossier)
else:
    print("Aucun dossier trouvé dans le répertoire.")
