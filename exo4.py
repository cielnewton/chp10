import os
import shutil

# Dossier source et dossier de destination
dossier_source = "."
dossier_destination = "newDirectory/text"

# Vérifier si le dossier de destination existe, sinon le créer
if not os.path.exists(dossier_destination):
    os.makedirs(dossier_destination)

# Lister tous les fichiers dans le dossier source
try:
    fichiers = os.listdir(dossier_source)
except OSError as e:
    print(f"Erreur lors de la lecture du dossier source : {e}")
    fichiers = []

# Copier les fichiers .txt vers le dossier de destination
for fichier in fichiers:
    if fichier.endswith(".txt"):
        chemin_source = os.path.join(dossier_source, fichier)
        chemin_destination = os.path.join(dossier_destination, fichier)
        try:
            shutil.copy2(chemin_source, chemin_destination)
            print(f"Copié : {chemin_source} -> {chemin_destination}")
        except OSError as e:
            print(f"Erreur lors de la copie de {chemin_source} : {e}")

